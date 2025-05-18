# P2P Chat Application 🇮🇹

Questo progetto implementa una chat peer-to-peer con interfaccia grafica Tkinter e crittografia simmetrica (AES via `cryptography.Fernet`). Le emoji vengono visualizzate come immagini.

---

## 📁 Struttura delle directory

p2p_chat/
├── emoji_png/ # immagini emoji
├── avatar1.png # avatar utente1
├── avatar2.png # avatar utente2
├── chat_history.txt # cronologia chat
├── chat_ui.py # interfaccia grafica
├── p2p_core.py # logica P2P e crittografia
├── peer1.py # avvio peer 1 (server)
├── peer2.py # avvio peer 2 (client)
└── requirements.txt # dipendenze Python


---

## 🧰 Requisiti di sistema

- Python 3.8+
- Pacchetto di sistema `python3-tk`
- `git`, `pip`, `virtualenv`

---

## 📦 Installazione su Ubuntu/Debian

bash
sudo apt-get update
sudo apt-get install python3-tk python3-venv 

## ⚙️ Setup ambiente virtuale

cd ~/progetto/p2p_chat
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

## Contenuto di requirements.txt:

Pillow
cryptography

## 😀 Emoji

Inserisci in emoji_png/ i PNG con il nome del codepoint Unicode.
Per le emoji predefinite (['😀','😂','😍','😎','😢','👍','🙏','🎉','💡','🔥']) servono i seguenti file:

1f600.png  1f602.png  1f60d.png  1f60e.png  1f622.png
1f44d.png  1f64f.png  1f389.png  1f4a1.png  1f525.png

## 🔐 Chiave crittografia

Chiave predefinita in p2p_core.py:

key = b'WnXYeB4X_QJDIDktc9x0YgZz8zAkAO8ODHdxHZMROj8='

Per generarne una nuova:

python3 - << 'EOF'
from cryptography.fernet import Fernet
print(Fernet.generate_key().decode())
EOF

Sostituisci il valore nel codice.

## 🚀 Avvio dell’applicazione

Apri due terminali distinti, in entrambi:

source venv/bin/activate

Nel primo terminale (server):

python3 peer1.py

Nel secondo terminale (client):

python3 peer2.py

## ✅ Funzionalità

    Messaggi: inviati e ricevuti in chiaro nell'interfaccia, criptati in transito.

    Emoji: cliccabili e integrate nei messaggi.

    Cronologia: salvata in chat_history.txt (max 200 messaggi).

## 🧹 Pulizia

deactivate
rm -rf venv __pycache__ chat_history.txt

❓ FAQ
Perché non usare pip install tkinter?

Tkinter è incluso in Python ma fornito come pacchetto di sistema.
Come aggiungo nuove emoji?

Aggiungile a emoji_list in chat_ui.py e inserisci il PNG in emoji_png/.
# P2P Chat Application 🇬🇧

This project implements a peer-to-peer chat app using a Tkinter GUI and symmetric encryption (AES via cryptography.Fernet). Emojis are displayed as images.
## 📁 Directory Structure

p2p_chat/
├── emoji_png/         # emoji image files
├── avatar1.png        # avatar for peer 1
├── avatar2.png        # avatar for peer 2
├── chat_history.txt   # chat log
├── chat_ui.py         # GUI interface
├── p2p_core.py        # P2P and encryption logic
├── peer1.py           # starts peer 1 (server)
├── peer2.py           # starts peer 2 (client)
└── requirements.txt   # Python dependencies

## 🧰 System Requirements

    Python 3.8+

    System package python3-tk

    git, pip, virtualenv

## 📦 Install on Ubuntu/Debian

sudo apt-get update
sudo apt-get install python3-tk python3-venv

## ⚙️ Virtual Environment Setup

cd ~/project/p2p_chat
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

## requirements.txt should contain:

Pillow
cryptography

## 😀 Emoji Setup

In the emoji_png/ folder, add PNG files named after the Unicode codepoint.
For the default set (['😀','😂','😍','😎','😢','👍','🙏','🎉','💡','🔥']), make sure these exist:

1f600.png  1f602.png  1f60d.png  1f60e.png  1f622.png
1f44d.png  1f64f.png  1f389.png  1f4a1.png  1f525.png

## 🔐 Encryption Key Configuration

Default Fernet key in p2p_core.py:

key = b'WnXYeB4X_QJDIDktc9x0YgZz8zAkAO8ODHdxHZMROj8='

To generate a new key:

python3 - << 'EOF'
from cryptography.fernet import Fernet
print(Fernet.generate_key().decode())
EOF

Replace the value in the code.
## 🚀 Running the Application

Open two terminals, and in both:

source venv/bin/activate

In the first terminal:

python3 peer1.py

In the second terminal:

python3 peer2.py

Two Tkinter windows will appear—one for each peer.
## ✅ Features

    Messaging: type and send text with Enter or Send. Messages are encrypted in transit.

    Emojis: click to insert into messages.

    Chat History: saved to chat_history.txt, up to 200 messages, auto-loaded at startup.

## 🧹 Cleanup

deactivate
rm -rf venv __pycache__ chat_history.txt

## ❓ FAQ
Why not install Tkinter via pip?

Tkinter is part of Python but installed via the system package python3-tk.
How can I add more emojis?

Add the Unicode emoji to emoji_list in chat_ui.py and the corresponding PNG in emoji_png/.

Happy coding! 🚀
