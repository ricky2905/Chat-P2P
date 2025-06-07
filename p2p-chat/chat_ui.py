import tkinter as tk
from tkinter import Frame, Text, Button, Label, Canvas
from PIL import Image, ImageTk  # PIL per gestione immagini
from datetime import datetime  # per timestamp dei messaggi
import os
import re

class ChatUI:
    def __init__(self, root, on_send,
                 me_avatar_path, peer_avatar_path,
                 history_file="chat_history.txt"):
        # Inizializza l'interfaccia grafica della chat
        self.root = root
        self.on_send = on_send               # callback per invio messaggi
        self.history_file = history_file     # file per salvare la cronologia

        self.root.title("P2P Chat")
        self.root.configure(bg="#e5ddd5")  # colore di sfondo stile WhatsApp

        # Carica avatar utente e peer (40×40 px)
        self.avatar_me = ImageTk.PhotoImage(
            Image.open(me_avatar_path).resize((40,40), Image.LANCZOS)
        )
        self.avatar_peer = ImageTk.PhotoImage(
            Image.open(peer_avatar_path).resize((40,40), Image.LANCZOS)
        )

        # Container principale con scrollbar per i messaggi
        container = Frame(root, bg="#e5ddd5")
        container.pack(fill=tk.BOTH, expand=True)
        self.canvas = Canvas(container, bg="#e5ddd5", bd=0, highlightthickness=0)
        scrollbar = tk.Scrollbar(container, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Frame interno alla canvas per disporre i messaggi
        self.msg_frame = Frame(self.canvas, bg="#e5ddd5")
        self.canvas.create_window((0,0), window=self.msg_frame, anchor='nw')
        self.msg_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # Prepara le emoji: lista, immagini per barra e chat, riferimenti per GC
        self.emoji_list = ['😀','😂','😍','😎','😢','👍','🙏','🎉','💡','🔥']
        self.emoji_bar_images = {}  # grandi nella barra
        self.chat_emoji_images = {} # piccole nei messaggi
        self.emoji_refs = []        # mantiene vivo il PhotoImage
        self._create_emoji_bar(root)

        # Frame di input: widget Text per testo+emoji + bottone Invia
        input_frame = Frame(root, bg="#f0f0f0", padx=10, pady=10)
        self.entry = Text(input_frame, font=("Helvetica",12), bd=0,
                          relief=tk.FLAT, height=1, wrap='word')
        self.entry.bind("<Return>", self.send_event)
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=10)
        send_btn = Button(input_frame, text="Invia", command=self.send,
                          bd=0, bg="#075E54", fg="white",
                          padx=20, pady=5)
        send_btn.pack(side=tk.RIGHT, padx=(10,0))
        input_frame.pack(fill=tk.X)

        # Carica cronologia dei messaggi salvati (ultimo 200)
        self._loading = True
        self.load_history()
        self._loading = False

        # Scrolla fino in fondo
        self.canvas.update_idletasks()
        self.canvas.yview_moveto(1.0)

    def _create_emoji_bar(self, parent):
        # Crea la barra orizzontale con i pulsanti delle emoji
        bar = Frame(parent, bg="#f0f0f0", pady=5)
        bar.pack(fill=tk.X)
        bar_size = 24  # dimensione icone barra
        chat_size = 16 # dimensione icone messaggio
        for emoji_char in self.emoji_list:
            # Genera nome file da codepoint unicode
            codepoint = '-'.join(f"{ord(c):x}" for c in emoji_char)
            image_path = os.path.join("emoji_png", f"{codepoint}.png")
            try:
                img = Image.open(image_path)
                # Barra emoji (24×24)
                photo_bar = ImageTk.PhotoImage(img.resize((bar_size, bar_size), Image.LANCZOS))
                self.emoji_bar_images[emoji_char] = photo_bar
                # Chat emoji (16×16)
                photo_chat = ImageTk.PhotoImage(img.resize((chat_size, chat_size), Image.LANCZOS))
                self.chat_emoji_images[emoji_char] = photo_chat
                # Pulsante nella barra
                btn = Button(bar, image=photo_bar, bd=0, relief=tk.FLAT,
                             bg="#ffffff", activebackground="#e0e0e0",
                             command=lambda emo=emoji_char: self._insert_emoji(emo))
                btn.pack(side=tk.LEFT, padx=4)
            except FileNotFoundError:
                print(f"Emoji non trovata: {image_path}")

    def _insert_emoji(self, emo):
        # Inserisce l'immagine emoji e uno spazio nel Text di input
        photo = self.emoji_bar_images.get(emo)
        if not photo:
            return
        self.emoji_refs.append(photo)
        self.entry.image_create(tk.INSERT, image=photo)
        self.entry.insert(tk.INSERT, " ")
        self.entry.focus()

    def _get_text_with_emoji_from_entry(self):
        # Estrae dal widget Text il testo, sostituendo le immagini con i caratteri emoji
        text, index = '', '1.0'
        end_index = self.entry.index(tk.END)
        while self.entry.compare(index, '<', end_index):
            try:
                img = self.entry.image_cget(index, "image")
            except tk.TclError:
                img = None
            if img:
                # Trova il char corrispondente
                emo_char = next((k for k,v in self.emoji_bar_images.items() if str(v)==img), '?')
                text += emo_char
                index = self.entry.index(f"{index} +2c")
            else:
                text += self.entry.get(index)
                index = self.entry.index(f"{index} +1c")
        return text.strip()

    def load_history(self):
        # Legge file di cronologia e riporta i messaggi in chat
        if os.path.exists(self.history_file):
            with open(self.history_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
            for line in lines[-200:]:
                head, msg = line.strip().split(': ',1)
                is_me = head.startswith("🧑‍💻")
                timestamp = head[head.find('['):head.find(']')+1] if '[' in head else ''
                self._add_message(msg, is_me, timestamp)

    def send_event(self, event):
        # Gestisce invio premendo Enter
        self.send()
        return "break"

    def send(self):
        # Invia messaggio: legge testo+emoji, salva su file, callback e UI
        msg = self._get_text_with_emoji_from_entry()
        if not msg:
            return
        self.entry.delete("1.0", tk.END)
        timestamp = datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
        self._add_message(msg, True, timestamp)
        self.on_send(f"{msg} {timestamp}")
        with open(self.history_file, "a", encoding="utf-8") as f:
            f.write(f"🧑‍💻 {timestamp}: {msg}\n")

    def append_message(self, display):
        # Riceve messaggio dal peer e lo aggiunge in UI + file
        idx = display.rfind('[')
        msg, timestamp = (display[:idx].strip(), display[idx:]) if idx!=-1 else (display, '')
        self._add_message(msg, False, timestamp)
        with open(self.history_file, "a", encoding="utf-8") as f:
            f.write(f"👤 {timestamp}: {msg}\n")

    def _add_message(self, text, is_me, timestamp):
        # Costruisce il bubble e lo inserisce nella chat
        side = 'e' if is_me else 'w'
        bg_color = '#dcf8c6' if is_me else '#f0f0f0'
        avatar = self.avatar_me if is_me else self.avatar_peer
        # Frame del messaggio
        msg_container = Frame(self.msg_frame, bg="#e5ddd5", pady=5)
        msg_container.pack(fill=tk.BOTH, anchor=side)
        # Avatar
        Label(msg_container, image=avatar, bg="#e5ddd5").pack(
            side=('right' if is_me else 'left'), padx=5)
        # Bubble
        bubble = Frame(msg_container, bg=bg_color, bd=1, relief=tk.FLAT)
        bubble.pack(side=('right' if is_me else 'left'), padx=5)
        # Testo + emoji
        text_widget = Text(bubble, bg=bg_color, font=("Helvetica",12),
                           wrap='word', bd=0, relief=tk.FLAT)
        text_widget.pack(padx=10, pady=5)
        text_widget.config(state=tk.NORMAL)
        self._insert_text_with_emoji(text_widget, text)
        # Regola altezza dinamicamente
        lines = int(text_widget.index('end-1c').split('.')[0])
        text_widget.configure(height=lines)
        text_widget.config(state=tk.DISABLED)
        # Timestamp sotto il bubble
        Label(bubble, text=timestamp.strip('[]'), bg=bg_color,
              font=("Helvetica",8), anchor='e').pack(
            fill=tk.X, padx=(0,5), pady=(0,2))
        # Scroll automatico se non in caricamento
        if not getattr(self, '_loading', False):
            self.canvas.update_idletasks()
            self.canvas.yview_moveto(1.0)

    def _insert_text_with_emoji(self, text_widget, text):
        # Inserisce in un Text widget testo e emoji (immagini piccole)
        emojis_pattern = '|'.join(re.escape(e) for e in self.chat_emoji_images)
        regex = re.compile(emojis_pattern)
        last_idx = 0
        for match in regex.finditer(text):
            start, end = match.span()
            if start>last_idx:
                text_widget.insert(tk.END, text[last_idx:start])
            emo = match.group()
            photo = self.chat_emoji_images.get(emo)
            if photo:
                self.emoji_refs.append(photo)
                text_widget.image_create(tk.END, image=photo)
                text_widget.insert(tk.END, " ")
            else:
                text_widget.insert(tk.END, emo)
            last_idx = end
        if last_idx < len(text):
            text_widget.insert(tk.END, text[last_idx:])
