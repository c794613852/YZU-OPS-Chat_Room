import socket
import threading
from PyQt5.QtWidgets import QMainWindow,QApplication
import mainwindow_ui
import sys

class Client(QMainWindow,mainwindow_ui.Ui_MainWindow):
    def __init__(self):

        super(self.__class__,self).__init__()
        self.setupUi(self)

        host='localhost'
        port=5550

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.connect((host, port))
        self.sock.send(b'1')

        th1=self.sendThreadFunc()
        #th2=self.recvThreadFunc()

        '''th1 = threading.Thread(target=self.sendThreadFunc)
        th2 = threading.Thread(target=self.recvThreadFunc)
        threads = [th1, th2]
        for t in threads:
            t.setDaemon(True)
            t.start()
        t.join()'''


    def sendThreadFunc(self):
        self.chat_line.append("Welcome to chat room!")
        self.chat_line.append('Input your nickname: ')
        #show the nickname
        self.login_button.clicked.connect(self.login)
        self.send_button.clicked.connect(self.sendmessage)
        '''
        while True:
            try:
                self.send_button.clicked.connect(self.sendmessage())
            except ConnectionAbortedError:
                self.chat_line.append('Server closed this connection!')
            except ConnectionResetError:
                self.chat_line.append('Server is closed!')
                '''
    def login(self):
        text=self.nickname_line.text()
        nickname = text
        senick = "SYSTEM: "+ nickname + " in the chat room "
        self.sock.send(senick.encode())
        str="Now lets chat,"+nickname
        self.chat_line.append(str)
        self.nickname_line.setEnabled(False)
        self.login_button.setEnabled(False)
        self.send_button.setEnabled(True)
        self.message_line.setEnabled(True)

    def sendmessage(self):
        myword =  self.message_line.text()
        self.message_line.setText("")
        myword = self.nickname_line.text() + ": " + myword
        self.chat_line.append(myword)
        self.sock.send(myword.encode())



    def recvThreadFunc(self):
        otherword = self.sock.recv(1024) # socket.recv(recv_size)
        self.chat_line.append(otherword.decode())
        '''
        while True:
            try:
                otherword = self.sock.recv(1024) # socket.recv(recv_size)
                self.chat_line.append(otherword.decode())
            except ConnectionAbortedError:
                self.chat_line.append('Server closed this connection!')

            except ConnectionResetError:
               self.chat_line.append('Server is closed!')
               '''

'''
def main():
    c = Client('localhost', 5550)
    th1 = threading.Thread(target=c.sendThreadFunc)
    th2 = threading.Thread(target=c.recvThreadFunc)
    threads = [th1, th2]
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
    '''


if __name__ == "__main__":
    app=QApplication(sys.argv)
    MainWindow=Client()
    MainWindow.show()
    sys.exit(app.exec_())
