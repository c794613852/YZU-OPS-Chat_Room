import socket
import threading

from PyQt5.QtWidgets import QMainWindow,QApplication
import mainwindow_ui
import sys

class Main(QMainWindow,mainwindow_ui.Ui_MainWindow):
    def __init__(self):
        super(self.__class__,self).__init__()
        self.setupUi(self)
        self.login_button.clicked.connect(self.Login)
        self.send_button.setEnabled(False)
        self.message_line.setEnabled(False)
    def Login(self):
        text=self.nickname_line.text()
        self.c = Client('140.138.145.39', 5550,text)
        self.chat_line.append("Welcome, "+text)
        self.chat_line.append("Lets Chat, "+text)
        self.nickname_line.setEnabled(False)
        self.login_button.setEnabled(False)
        self.send_button.setEnabled(True)
        self.message_line.setEnabled(True)
    def Send(self):
        self.meg=self.message_line.text()





class Client:
    def __init__(self, host, port,name):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.connect((host, port))
        self.sock.send(b'1')
        self.username = name

    def sendThreadFunc(self):
        print("Welcome to chat room!")
        print('Input your nickname: ')
        nickname = self.username
        senick = "SYSTEM: "+ nickname + " in the chat room "
        self.sock.send(senick.encode())
        print("Now lets chat,",nickname)
        while True:
            try:
                myword = Main.meg
                myword = nickname + ": " + myword
                self.sock.send(myword.encode())
            except ConnectionAbortedError:
                print('Server closed this connection!')
            except ConnectionResetError:
                print('Server is closed!')

    def recvThreadFunc(self):
        while True:
            try:
                otherword = self.sock.recv(1024) # socket.recv(recv_size)
                print(otherword.decode())
            except ConnectionAbortedError:
                print('Server closed this connection!')

            except ConnectionResetError:
                print('Server is closed!')
def main():
    th1 = threading.Thread(target=Main.c.sendThreadFunc)
    th2 = threading.Thread(target=Main.c.recvThreadFunc)
    threads = [th1, th2]
    for t in threads:
        t.setDaemon(True)
        t.start()
        t.join()



if __name__ == "__main__":
    app=QApplication(sys.argv)
    MainWindow=Main()
    MainWindow.show()
    sys.exit(app.exec_())
    main()

