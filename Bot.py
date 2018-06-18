import threading
from weather import Weather, Unit
from InitDB import DataBaseChatRoom
import socket


class Bot():
   def __init__(self, host, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock
        self.sock.connect((host, port))
        self.sock.send(b'1')
        self.peonum = 0
        self.speech="?"
   def sendThreadFunc(self):
        try:
            myword = "bot : " + self.speech
            print(myword)
            self.sock.send(myword.encode())
        except ConnectionAbortedError:
            print('Server closed this connection!')
        except ConnectionResetError:
            print('Server is closed!')

   def recvThreadFunc(self):
        while True:
            try:
                otherword = self.sock.recv(1024).decode() # socket.recv(recv_size)
                systemlogin = otherword.split()
                print(systemlogin[1]+"!")
                if (systemlogin[1]=="bot"):
                    self.sendThreadFunc()
            except ConnectionAbortedError:
                print('Server closed this connection!')

            except ConnectionResetError:
                print('Server is closed!')
   def login(self):
        loginSuc = db.queryByuname("bot", "bot")
        if(loginSuc):
            online = db.onoffline("bot", "bot")
            if(online == False):
                global recvlog
                db.updataUser("bot", "bot",True)

def main():
    th0 = threading.Thread(target=bot.recvThreadFunc)
    th0.setDaemon(True)
    th0.start()
    th0.join()

if __name__ == "__main__":
    bot=Bot('localhost', 5550)
    db = DataBaseChatRoom()
    bot.login()
    main()



weather = Weather(unit=Unit.CELSIUS)

location = weather.lookup_by_location('Taoyuan City')
condition = location.condition

print(condition.text)
print(condition.temp)
