import socket
import threading
from cryptography.fernet import Fernet  # Crittografia simmetrica

class P2PCore:
    def __init__(self, host, port, peer_host, peer_port, on_message):
        # Parametri di connessione
        self.host = host
        self.port = port
        self.peer_host = peer_host
        self.peer_port = peer_port
        self.on_message = on_message  # callback da chiamare quando ricevi un messaggio

        # Crea socket TCP
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn = None
        self.running = True

        # Chiave di cifratura condivisa (simmetrica)
        key = b'WnXYeB4X_QJDIDktc9x0YgZz8zAkAO8ODHdxHZMROj8='
        self.cipher = Fernet(key)

        # Thread paralleli per ascolto e connessione
        threading.Thread(target=self._listen, daemon=True).start()
        threading.Thread(target=self._connect_to_peer, daemon=True).start()

    def _listen(self):
        # Server: ascolta connessioni in arrivo
        try:
            self.sock.bind((self.host, self.port))
            self.sock.listen(1)
            self.conn, _ = self.sock.accept()  # accetta una connessione
            self._recv_loop()
        except Exception as e:
            print(f"Errore ascolto: {e}")

    def _connect_to_peer(self):
        # Client: tenta di connettersi al peer
        while self.running and self.conn is None:
            try:
                temp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                temp_sock.connect((self.peer_host, self.peer_port))
                self.conn = temp_sock
                self._recv_loop()
                break
            except Exception:
                import time
                time.sleep(2)  # ritenta dopo 2 secondi

    def _recv_loop(self):
        # Ciclo di ricezione messaggi
        while self.running:
            try:
                data = self.conn.recv(4096)
                if not data:
                    break
                # Decifra messaggio e invoca callback
                msg = self.cipher.decrypt(data).decode('utf-8')
                self.on_message(msg)
            except Exception as e:
                print(f"Errore ricezione: {e}")
                break

    def send(self, msg):
        # Invia messaggio cifrato
        if self.conn:
            try:
                encrypted = self.cipher.encrypt(msg.encode('utf-8'))
                self.conn.sendall(encrypted)
            except Exception as e:
                print(f"Errore invio: {e}")

    def close(self):
        # Chiude connessioni in modo sicuro
        self.running = False
        if self.conn:
            self.conn.close()
        self.sock.close()

