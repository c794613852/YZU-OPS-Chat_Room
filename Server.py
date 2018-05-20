# -*- encoding: utf-8 -*-
import socket
import threading
from time import gmtime, localtime, strftime


class Server:
    def __init__(self, host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.bind((host, port))
        self.sock.listen(5)
        print('Server', socket.gethostbyname(host), 'listening ...')
        self.mylist = list()
        self.nicknameList = {}

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
    def tellOthers(self, exceptNum, whatToSay, connNumber ):
        for c in self.mylist:
            if c.fileno() != exceptNum:
                try:
                    currentTime = strftime("%Y-%m-%d %H:%M:%S", localtime())
                    num=str(connNumber)
                    c.send((whatToSay + "            " + currentTime + " [ " + num + " ] ").encode())
                except:
                    pass

    def subThreadIn(self, myconnection, connNumber):
        self.mylist.append(myconnection)
        while True:
            try:
                recvedMsg = myconnection.recv(1024).decode()
                if recvedMsg:
                    if connNumber not in self.nicknameList:
                        self.nicknameList[connNumber] = recvedMsg.split()[1]
                    else:
                        pass
                    self.tellOthers(connNumber, recvedMsg, connNumber )
                else:
                    pass

            except (OSError, ConnectionResetError):
                try:
                    self.mylist.remove(myconnection)
                    self.tellOthers(connNumber, "SYSTEM: " + self.nicknameList[connNumber] + " leave the room")
                    del self.nicknameList[connNumber]
                except:
                    pass

                myconnection.close()
                return


def main():
    s = Server('localhost', 5550)
    while True:
        s.checkConnection()


if __name__ == "__main__":
    main()

