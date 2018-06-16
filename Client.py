import socket
import threading
from InitDB import DataBaseChatRoom
from PyQt5.QtWidgets import QMainWindow,QApplication
import mainwindow_ui
import sys
sendBtnPushed = False
recvlog ="systeM==!!"
class Main(QMainWindow,mainwindow_ui.Ui_MainWindow):
    def __init__(self):
        super(self.__class__,self).__init__()
        self.setupUi(self)
        self.show()
        self.login_button.clicked.connect(self.Login)
        self.send_button.clicked.connect(self.Send)
        self.updatepass_button.clicked.connect(self.ChangePass)
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
        loginSuc = db.queryByuname(self.nickname, self.password)
        if(loginSuc):
            online = db.onoffline(self.nickname, self.password)
            if(online == 'False'):
                global recvlog
                c.sock.send(recvlog.encode())
                self.chat_line.append("Welcome, " + self.nickname)
                self.chat_line.append("Lets Chat, " + self.nickname)
                senick = "SYSTEM: " + self.nickname + " is in the chat room"
                c.sock.send(senick.encode())
                self.nickname_line.setEnabled(False)
                self.password_line.setEnabled(False)
                self.login_button.setEnabled(False)
                self.send_button.setEnabled(True)
                self.message_line.setEnabled(True)
                self.changepass_line.setEnabled(True)
                self.updatepass_button.setEnabled(True)
                db.updataUser(self.nickname, self.password,'True')
                #MainWindow.onlinenum_label.setText(strpeonum)
            else:
                self.chat_line.append("This account has been logined")
        else:
            self.chat_line.append("Wrong name or password, please login again")

    def ChangePass(self):
        if(self.changepass_line.text() != ""):
            newpass = self.changepass_line.text()
            result = db.updataUser(self.nickname,newpass,'True')
            self.changepass_line.setText("")
            self.chat_line.append(result)

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
        self.peonum = 0

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
        global recvlog
        while True:
            try:
                otherword = self.sock.recv(1024).decode() # socket.recv(recv_size)
                systemlogin = otherword.split()
                if(systemlogin[0] == recvlog):
                    MainWindow.onlinenum_label.setText("目前連天室有 " + str(systemlogin[1]))
                else:
                    MainWindow.chat_line.append(otherword)

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
    db = DataBaseChatRoom()
    app=QApplication(sys.argv)
    MainWindow = Main()
    main()
