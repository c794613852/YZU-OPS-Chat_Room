import socket
import threading
import InitDB
from PyQt5.QtWidgets import QMainWindow,QApplication
import mainwindow_ui
import sys
sendBtnPushed = False

class Main(QMainWindow,mainwindow_ui.Ui_MainWindow):
    def __init__(self):
        super(self.__class__,self).__init__()
        self.setupUi(self)
        self.show()
        self.login_button.clicked.connect(self.Login)
        self.send_button.clicked.connect(self.Send)
        self.send_button.setEnabled(False)
        self.message_line.setEnabled(False)
        self.changepass_line.setEnabled(False)
        self.updatepass_button.setEnabled(False)
        self.chat_line.append("Welcome to chat room!")
        self.chat_line.append("Input your nickname: ")
    def Login(self):
        self.nickname = self.nickname_line.text()
        self.password = self.password_line.text()
        print("name : "+self.nickname)
        print("password : "+self.password)
        #InitDB.queryByuname(self , self.nickname , self.password)
        #self.c = Client('140.138.145.39', 5550,text)
        self.chat_line.append("Welcome, " + self.nickname)
        self.chat_line.append("Lets Chat, " + self.nickname)
        senick = "SYSTEM: " + self.nickname + " is in the chat room"
        c.sock.send(senick.encode())
        self.nickname_line.setEnabled(False)
        self.login_button.setEnabled(False)
        self.send_button.setEnabled(True)
        self.message_line.setEnabled(True)
        self.changepass_line.setEnabled(True)
        self.updatepass_button.setEnabled(True)
    def Send(self):
        global sendBtnPushed
        sendBtnPushed = True
        meg = self.message_line.text()
        c.sendThreadFunc()

class Client:
    def __init__(self, host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.connect((host, port))
        self.sock.send(b'1')

    def sendThreadFunc(self):
        global sendBtnPushed
        while sendBtnPushed:
            try:
                myword = MainWindow.nickname + ": " + MainWindow.message_line.text()
                MainWindow.chat_line.append(myword.rjust(150-len(myword)))
                self.sock.send(myword.encode())
                MainWindow.message_line.setText("")
                sendBtnPushed = False
            except ConnectionAbortedError:
                print('Server closed this connection!')
            except ConnectionResetError:
                print('Server is closed!')

    def recvThreadFunc(self):
        while True:
            try:
                otherword = self.sock.recv(1024) # socket.recv(recv_size)
                MainWindow.chat_line.append(otherword.decode())
            except ConnectionAbortedError:
                print('Server closed this connection!')

            except ConnectionResetError:
                print('Server is closed!')

def main():
    th0 = threading.Thread(target=ui)
    th0.setDaemon(True)
    th0.start()
    #th0.join()
    sys.exit(app.exec_())

def ui():
    th1 = threading.Thread(target=c.sendThreadFunc)
    th2 = threading.Thread(target=c.recvThreadFunc)
    threads = [th1, th2]
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()


if __name__ == "__main__":
    c = Client('localhost', 5550)
    app=QApplication(sys.argv)
    MainWindow = Main()
    main()
