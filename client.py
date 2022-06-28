import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog

HOST = '127.0.0.1'
PORT = 9090

class Client:

    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        msg = tkinter.Tk
        msg.withdraw()

        self.nickname = simpledialog.askstring("Nickname", "Plz Choose The NickName")

        self.gui_done = False
        self.running = True

        gui_thread = threading.Thread(target=self.gui_loop)
        receive_thread = threading.Thread(target=self.gui_loop)

        gui_thread.start()
        receive_thread.start()

        def gui_loop(self):
            self.win = tkinter.Tk()
            self.win.configure(bg="lightgray")

            self.chat_label = tkinter.Label(self.win, text="Chat :", bg="lightgray")

        def receive(self):
            pass





