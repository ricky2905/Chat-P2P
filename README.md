# 🇮🇹 P2P Chat Application

Questa applicazione implementa una chat peer-to-peer reale con interfaccia grafica Tkinter e crittografia simmetrica (AES via cryptography.Fernet). Ogni peer è autonomo: si comporta sia da server che da client, con connessione diretta.

Le emoji sono visualizzate come immagini.

---

## 📁 Struttura delle directory

p2p_chat/
├── emoji_png/         # immagini emoji
├── avatar1.png        # avatar utente 1
├── avatar2.png        # avatar utente 2
├── chat_history.txt   # cronologia chat
├── chat_ui.py         # interfaccia grafica
├── p2p_core.py        # logica P2P e crittografia
├── peer_app.py        # modulo principale dell'app peer
├── requirements.txt   # dipendenze Python

---

## 🧰 Requisiti di sistema

    Python 3.8+

    python3-tk (pacchetto di sistema per Tkinter)

    git, pip, virtualenv

---

## 📦 Installazione su Ubuntu/Debian

sudo apt-get update
sudo apt-get install python3-tk python3-venv

--- 

## ⚙️ Setup ambiente virtuale

cd ~/progetto/p2p_chat
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

---

## 🗂 Contenuto di requirements.txt

Pillow
cryptography

---

## 😀 Emoji

Inserire in emoji_png/ i file PNG con il nome del codepoint Unicode.

Per le emoji predefinite (['😀','😂','😍','😎','😢','👍','🙏','🎉','💡','🔥']), servono questi file:

1f600.png  1f602.png  1f60d.png  1f60e.png  1f622.png
1f44d.png  1f64f.png  1f389.png  1f4a1.png  1f525.png

---

## 🔐 Chiave di crittografia

Nel file p2p_core.py c'è una chiave predefinita:

key = b'WnXYeB4X_QJDIDktc9x0YgZz8zAkAO8ODHdxHZMROj8='

Per generarne una nuova:

python3 - << 'EOF'
from cryptography.fernet import Fernet
print(Fernet.generate_key().decode())
EOF

Sostituirla nel file p2p_core.py.

---

## 🚀 Avvio dell'applicazione

Apri due terminali distinti (uno per peer):
### Terminale 1:

source venv/bin/activate
python3 peer_app.py 1

### Terminale 2:

source venv/bin/activate
python3 peer_app.py 2

Ogni finestra Tkinter rappresenta un peer. La connessione è diretta e simmetrica.

---

## ✅ Funzionalità

    ✉️ Messaggi: criptati in transito, mostrati in chiaro in chat.

    😄 Emoji: cliccabili e integrate nei messaggi.

    🕓 Cronologia: salvata in chat_history.txt (fino a 200 messaggi).

---

## 🧹 Pulizia ambiente

deactivate
rm -rf venv __pycache__ chat_history.txt

--- 

## ❓ FAQ

Perché non usare pip install tkinter?
Tkinter è parte di Python, ma su Linux va installato tramite il pacchetto python3-tk.

Come aggiungo nuove emoji?
Inserisci il PNG in emoji_png/ e aggiungi il simbolo in emoji_list in chat_ui.py.

---

# 🇬🇧 P2P Chat Application

This project implements a true peer-to-peer chat app using a Tkinter GUI and symmetric encryption (AES via cryptography.Fernet). Each peer behaves as both server and client.

Emojis are rendered as PNG images.

---

## 📁 Directory Structure

p2p_chat/
├── emoji_png/         # emoji images
├── avatar1.png        # peer 1 avatar
├── avatar2.png        # peer 2 avatar
├── chat_history.txt   # chat log
├── chat_ui.py         # GUI interface
├── p2p_core.py        # P2P and encryption logic
├── peer_app.py        # main peer launcher
├── requirements.txt   # dependencies

---

## 🧰 System Requirements

    Python 3.8+

    python3-tk (GUI library)

    git, pip, virtualenv

---

## 📦 Install on Ubuntu/Debian

sudo apt-get update
sudo apt-get install python3-tk python3-venv

---

## ⚙️ Virtual Environment Setup

cd ~/project/p2p_chat
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

---

## 🗂 requirements.txt content

Pillow
cryptography

---

## 😀 Emoji Support

Place PNG emoji files inside emoji_png/ named by Unicode codepoint.

Default emoji set:

1f600.png  1f602.png  1f60d.png  1f60e.png  1f622.png
1f44d.png  1f64f.png  1f389.png  1f4a1.png  1f525.png

---

## 🔐 Encryption Key

Key defined in p2p_core.py:

key = b'WnXYeB4X_QJDIDktc9x0YgZz8zAkAO8ODHdxHZMROj8='

To generate a new one:

python3 - << 'EOF'
from cryptography.fernet import Fernet
print(Fernet.generate_key().decode())
EOF

---

## 🚀 Running the Application

Open two terminals, both with:

source venv/bin/activate

### Terminal 1:

python3 peer_app.py 1

### Terminal 2:

python3 peer_app.py 2

Each will launch a chat window connected to the other.

---

## ✅ Features

    🔒 Encrypted messaging

    😀 Emoji support

    💾 Chat history saved locally

---

## 🧹 Cleanup

deactivate
rm -rf venv __pycache__ chat_history.txt

---

## ❓ FAQ

Why not install Tkinter via pip?
Tkinter is bundled with Python, but on Linux it's provided via python3-tk.

How to add more emojis?
Add to emoji_list in chat_ui.py and the corresponding PNG to emoji_png/.

---
