from weather import Weather, Unit
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




weather = Weather(unit=Unit.CELSIUS)

location = weather.lookup_by_location('Taoyuan City')
condition = location.condition

print(condition.text)
print(condition.temp)
