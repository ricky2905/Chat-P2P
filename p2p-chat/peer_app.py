import tkinter as tk
from chat_ui import ChatUI           # UI della chat
from p2p_core import P2PCore         # Logica di comunicazione P2P

class PeerApp:
    def __init__(self, my_port, peer_port, me_avatar, peer_avatar):
        self.root = tk.Tk()  # Crea finestra principale Tkinter

        # Inizializza l'interfaccia grafica della chat
        self.ui = ChatUI(
            self.root,
            self.send_message,
            me_avatar_path=me_avatar,
            peer_avatar_path=peer_avatar
        )

        # Inizializza il modulo P2P con callback per ricezione messaggi
        self.p2p = P2PCore(
            host="127.0.0.1", port=my_port,
            peer_host="127.0.0.1", peer_port=peer_port,
            on_message=self.on_message_received
        )

        # Gestione chiusura finestra
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        # Avvia ciclo principale GUI
        self.root.mainloop()

    def send_message(self, msg):
        # Invia messaggio al peer
        self.p2p.send(msg)

    def on_message_received(self, msg):
        # Riceve messaggio da peer → visualizza in UI
        self.ui.append_message(msg)

    def on_close(self):
        # Chiusura ordinata: chiude socket e GUI
        self.p2p.close()
        self.root.destroy()

# Avvio app in base al parametro da riga di comando
if __name__ == "__main__":
    import sys
    peer_id = sys.argv[1] if len(sys.argv) > 1 else "1"
    if peer_id == "1":
        PeerApp(my_port=5000, peer_port=5001,
                me_avatar="avatar1.png", peer_avatar="avatar2.png")
    else:
        PeerApp(my_port=5001, peer_port=5000,
                me_avatar="avatar2.png", peer_avatar="avatar1.png")

