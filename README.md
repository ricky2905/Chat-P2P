# P2P Chat Application 🇮🇹

Questo progetto implementa una chat peer-to-peer con interfaccia grafica Tkinter e crittografia simmetrica (AES via `cryptography.Fernet`). Le emoji vengono visualizzate come immagini.

---

## Struttura delle directory

```
// directory con il progetto
├── p2p_chat
│   ├── emoji_png         // directory con le immagini per le emoji
│   ├── avatar1.png       // immagine per avatar utente1
│   ├── avatar2.png       // immagine per avatar utente2
│   ├── chat_history.txt  // cronologia chat
│   ├── chat_ui.py        // file python per la grafica della chat
│   ├── p2p_core.py       // file python per la struttura della connessione e encrypting
│   ├── peer1.py          // file python per avvio utente1
│   ├── peer2.py          // file python per avvio utente2
│   └── requirements.txt  // file con dipendenze iniziali da installare
└── README.md             // file corrente
```

---

## Requisiti di sistema

* **Python 3.8+**
* Libreria di sistema **python3-tk** (per Tkinter)
* `git`, `pip`, `virtualenv` (o ambiente virtuale a tua scelta)

### Installazione dei pacchetti di sistema (Ubuntu/Debian)

```bash
sudo apt-get update
sudo apt-get install python3-tk python3-venv
```

---

## Setup ambiente virtuale

1. Posizionati nella cartella del progetto:

   ```bash
   cd ~/progetto/p2p_chat
   ```
2. Crea e attiva un ambiente virtuale:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Installa le dipendenze Python:

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

> **Nota:** Il file `requirements.txt` deve contenere:
>
> ```txt
> Pillow
> cryptography
> ```

---

## Preparazione folder emoji

Nella directory `emoji_png/` devono trovarsi le immagini PNG corrispondenti alle emoji supportate. Ogni file deve essere nominato con il codepoint Unicode dell'emoji, es. `1f600.png` per 😀.

Se utilizzi solo quelle di default (`['😀','😂','😍','😎','😢','👍','🙏','🎉','💡','🔥']`), assicurati in `emoji_png/` di avere:

```
1f600.png  1f602.png  1f60d.png  1f60e.png  1f622.png
1f44d.png  1f64f.png  1f389.png  1f4a1.png  1f525.png
```

---

## Configurazione chiave crittografia

Il file `p2p_core.py` utilizza di default una chiave Fernet hardcoded:

```python
key = b'WnXYeB4X_QJDIDktc9x0YgZz8zAkAO8ODHdxHZMROj8='
```

Se vuoi cambiarla, genera una nuova chiave con:

```bash
python3 - << 'EOF'
from cryptography.fernet import Fernet
print(Fernet.generate_key().decode())
EOF
```

E sostituisci il valore nel codice.

---

## Avvio dell'applicazione

L'applicazione è composta da due script:

* `peer1.py` avvia il peer in **modalità server**
* `peer2.py` avvia il peer in **modalità client**

Per test locale sulla stessa macchina:

1. Apri due terminali distinti.
2. In entrambi i terminali, attiva l'ambiente virtuale:

   ```bash
   source ~/progetto/p2p_chat/venv/bin/activate
   ```
3. Nel primo terminale, avvia il server:

   ```bash
   python3 peer1.py
   ```
4. Nel secondo terminale, avvia il client:

   ```bash
   python3 peer2.py
   ```
5. Si apriranno due finestre Tkinter: una per `Peer1` e una per `Peer2`.

---

## Test funzionalità

1. **Invio di un messaggio**:

   * Digita del testo nella casella di input (in basso nel UI) e premi `Invia` o `Enter`.
   * Il messaggio apparirà nella finestra opposta, crittografato in transito.

2. **Emoji**:

   * Clicca su una delle icone nella barra delle emoji per inserirla nel messaggio.
   * Le emoji compariranno correttamente sia nel campo di input che nei messaggi inviati/ricevuti.

3. **Cronologia**:

   * Al primo avvio, il file `chat_history.txt` verrà creato.
   * I messaggi inviati e ricevuti vengono salvati (ultimi 200) e ricaricati all'avvio.

---

## Pulizia

Per rimuovere l'ambiente virtuale e i file generati:

```bash
deactivate
rm -rf venv __pycache__ chat_history.txt
```

---

## FAQ

* **Perché non installare `tkinter` via pip?**
  Tkinter fa parte della libreria standard di Python ed è fornito dal pacchetto di sistema `python3-tk`.

* **Come aggiungere nuove emoji?**
  Aggiungi il carattere Unicode alla lista `emoji_list` in `chat_ui.py` e inserisci il PNG corrispondente in `emoji_png/`.

---

*Buon coding!*




# P2P Chat Application 🇬🇧

This project implements a peer-to-peer chat application with a Tkinter GUI and symmetric encryption (AES via `cryptography.Fernet`). Emojis are rendered as images.

## Directory Structure

├── p2p_chat
│ ├── emoji_png // directory containing emoji image files
│ ├── avatar1.png // avatar image for peer 1
│ ├── avatar2.png // avatar image for peer 2
│ ├── chat_history.txt // chat log file
│ ├── chat_ui.py // Python file for chat GUI
│ ├── p2p_core.py // Python file for connection and encryption
│ ├── peer1.py // script to launch peer 1 (server)
│ ├── peer2.py // script to launch peer 2 (client)
│ └── requirements.txt // Python dependencies
└── README.md // this file


---

## System Requirements

* **Python 3.8+**
* System package **python3-tk** (for Tkinter)
* `git`, `pip`, `virtualenv` (or your preferred Python environment tool)

### Install system packages (Ubuntu/Debian)

```bash
sudo apt-get update
sudo apt-get install python3-tk python3-venv

Virtual Environment Setup

    Navigate to the project directory:

cd ~/project/p2p_chat

Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate

Install Python dependencies:

    pip install --upgrade pip
    pip install -r requirements.txt

    Note: The requirements.txt file should contain:

    Pillow
    cryptography

Emoji Folder Preparation

The emoji_png/ directory must contain PNG files named with the emoji's Unicode codepoint, e.g. 1f600.png for 😀.

For the default set (['😀','😂','😍','😎','😢','👍','🙏','🎉','💡','🔥']), make sure the folder includes:

1f600.png  1f602.png  1f60d.png  1f60e.png  1f622.png
1f44d.png  1f64f.png  1f389.png  1f4a1.png  1f525.png

Encryption Key Configuration

The file p2p_core.py uses a hardcoded Fernet key by default:

key = b'WnXYeB4X_QJDIDktc9x0YgZz8zAkAO8ODHdxHZMROj8='

To generate a new key:

python3 - << 'EOF'
from cryptography.fernet import Fernet
print(Fernet.generate_key().decode())
EOF

Replace the old key in the code with the new one.
Running the Application

The app is composed of two scripts:

    peer1.py starts the peer in server mode

    peer2.py starts the peer in client mode

To test locally:

    Open two terminal windows.

    In both, activate the virtual environment:

source ~/project/p2p_chat/venv/bin/activate

In the first terminal, run the server:

python3 peer1.py

In the second terminal, run the client:

    python3 peer2.py

    Two Tkinter windows will appear: one for Peer1 and one for Peer2.

Feature Testing

    Message sending:

        Type a message in the input field and press Enter or click Send.

        Messages are securely transmitted and appear in the opposite window.

    Emojis:

        Click an emoji button to insert it into the message field.

        Emojis appear correctly in both sent and received messages.

    Chat history:

        A chat_history.txt file is created on first launch.

        Messages (up to the last 200) are stored and reloaded at startup.

Cleanup

To remove the virtual environment and generated files:

deactivate
rm -rf venv __pycache__ chat_history.txt

FAQ

    Why not install tkinter via pip?
    Tkinter is part of the standard Python library but provided via system package python3-tk.

    How do I add more emojis?
    Add the Unicode emoji character to the emoji_list in chat_ui.py and place the corresponding PNG in emoji_png/.

Happy coding!
