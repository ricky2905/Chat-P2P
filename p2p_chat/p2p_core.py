import socket
import threading
from cryptography.fernet import Fernet  # Libreria crittografia simmetrica

class P2PCore:
    def __init__(self, is_server, host, port, on_message):
        # Parametri di configurazione
        self.is_server = is_server    # True per peer server, False per client
        self.host = host              # IP o hostname
        self.port = port              # porta TCP
        self.on_message = on_message  # callback per gestione ricezione

        # Socket TCP
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn = None              # socket connesso (server o client)
        self.running = True           # flag loop di ricezione

        # Chiave Fernet hardcoded (32 byte base64)
        key = b'WnXYeB4X_QJDIDktc9x0YgZz8zAkAO8ODHdxHZMROj8='
        self.cipher = Fernet(key)

        # Avvia thread di ascolto o connessione
        if self.is_server:
            self.sock.bind((host, port))
            self.sock.listen(1)
            threading.Thread(target=self._accept_loop, daemon=True).start()
        else:
            threading.Thread(target=self._connect_loop, daemon=True).start()

    def _accept_loop(self):
        # Server: aspetta una connessione entrante
        self.conn, addr = self.sock.accept()
        print(f"Connessione accettata da {addr}")
        self._recv_loop()

    def _connect_loop(self):
        # Client: prova a connettersi finché non riesce
        while self.running:
            try:
                self.sock.connect((self.host, self.port))
                self.conn = self.sock
                print(f"Connesso a {(self.host, self.port)}")
                self._recv_loop()
                break
            except Exception as e:
                print(f"Errore connessione, ritento: {e}")
                import time; time.sleep(3)

    def _recv_loop(self):
        # Loop di ricezione: decripta e chiama callback
        while self.running:
            try:
                data = self.conn.recv(4096)
                if not data:
                    break
                # Decripta il payload
                decrypted = self.cipher.decrypt(data).decode('utf-8')
                self.on_message(decrypted)
            except Exception as e:
                print(f"Errore ricezione: {e}")
                break

    def send(self, msg):
        # Cripta e invia messaggio se connesso
        if self.conn:
            try:
                encrypted_msg = self.cipher.encrypt(msg.encode('utf-8'))
                self.conn.sendall(encrypted_msg)
            except Exception as e:
                print(f"Errore invio: {e}")

    def close(self):
        # Chiude socket e arresta loop
        self.running = False
        if self.conn:
            self.conn.close()
        self.sock.close()
