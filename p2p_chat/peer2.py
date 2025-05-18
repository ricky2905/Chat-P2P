import tkinter as tk
from chat_ui import ChatUI
from p2p_core import P2PCore

# Peer2 identico ma in modalità client (_is_server=False_)
class Peer2:
    def __init__(self):
        self.root = tk.Tk()
        self.ui = ChatUI(self.root, self.send_message,
                         me_avatar_path="avatar1.png",
                         peer_avatar_path="avatar2.png")
        self.p2p = P2PCore(
            is_server=False, host="127.0.0.1", port=5000,
            on_message=self.on_message_received
        )
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.mainloop()

    def send_message(self, msg):
        self.p2p.send(msg)

    def on_message_received(self, msg):
        self.ui.append_message(msg)

    def on_close(self):
        self.p2p.close()
        self.root.destroy()

if __name__ == "__main__":
    Peer2()
