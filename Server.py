# -*- encoding: utf-8 -*-
import socket
import threading
from time import gmtime, localtime, strftime
from InitDB import DataBaseChatRoom
from PyQt5.QtWidgets import QMainWindow,QApplication
import severwindow_ui
import sys
recvlogin="systeM==!!"

class Main(QMainWindow,severwindow_ui.Ui_SeverWindow):
    def __init__(self):
        super(self.__class__,self).__init__()
        self.setupUi(self)
        self.show()
        self.add_button.clicked.connect(self.register)
    def register(self):
        user=self.nickname_line.text()
        password=self.password_line.text()
        result=db.checkUserExist(user)
        if(result=="User is not exist"):
            db.insertUser(user,password,False)
            print("user : " + user)
            print("password : " + password)
        else:
            print(result)

class Server:
    def __init__(self, host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.bind((host, port))
        self.sock.listen(5)
        print('Server', socket.gethostbyname(host), 'listening ...')
        self.mylist = list()
        self.nicknameList = {}
        self.peonum = 0


    def checkConnection(self):
        connection, addr = self.sock.accept()
        print('Accept a new connection', connection.getsockname(), connection.fileno())
        try:
            buf = connection.recv(1024).decode()
            if buf == '1':
                # start a thread for new connection
                mythread = threading.Thread(target=self.subThreadIn, args=(connection, connection.fileno()))
                mythread.setDaemon(True)
                mythread.start()

            else:
                connection.send(b'please go out!')
                connection.close()
        except:
            pass

    # send whatToSay to every except people in exceptNum
    def tellOthers(self, exceptNum, whatToSay ):
        for c in self.mylist:
            if c.fileno() != exceptNum:
                try:
                    currentTime = strftime("%Y-%m-%d %H:%M:%S", localtime())
                    num=str(exceptNum)
                    c.send((whatToSay + "            " + currentTime + " [ " + num + " ] ").encode())
                    print(whatToSay)
                except:
                    pass
    #tell every one the new peonum
    def peonumToClient(self):
        for c in self.mylist:
            global recvlogin
            try:
                c.send((recvlogin + " " + str(self.peonum)).encode())
            except:
                pass

    def subThreadIn(self, myconnection, connNumber):
        self.mylist.append(myconnection)
        while True:
            global recvlogin
            try:
                recvedMsg = myconnection.recv(1024).decode()
                if recvedMsg == recvlogin:
                    self.peonum += 1 #plus one to num of people in room
                    self.peonumToClient() #tell everyone the new num of people in the room
                elif recvedMsg:
                    if connNumber not in self.nicknameList:
                        self.nicknameList[connNumber] = recvedMsg.split()[1]
                    else:
                        pass
                    self.tellOthers(connNumber, recvedMsg )
            except (OSError, ConnectionResetError):
                try:
                    self.mylist.remove(myconnection)
                    self.peonum -= 1
                    leaveinfor = db.findone_information(self.nicknameList[connNumber])
                    print(leaveinfor)
                    print('user:' + leaveinfor['uname'])
                    print('password' + leaveinfor['upwd'])
                    db.updataUser(leaveinfor['uname'], leaveinfor['upwd'], False)
                    self.tellOthers(connNumber, "SYSTEM: " + self.nicknameList[connNumber] + " leave the room")
                    del self.nicknameList[connNumber]
                    self.peonumToClient()
                except:
                    pass

                myconnection.close()
                return


def main():
    th0=threading.Thread(target=ui)
    th0.setDaemon(True)
    th0.start()
    sys.exit(app.exec_())

def ui():
     while True:
        s.checkConnection()

if __name__ == "__main__":
    s = Server('localhost', 5550)
    db = DataBaseChatRoom()
    app=QApplication(sys.argv)
    MainWindow=Main()
    main()
