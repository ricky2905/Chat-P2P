# P2P Chat Application

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

