from weather import Weather, Unit
from currency_converter import CurrencyConverter


class Bot():
   def __init__(self):
        self.speech="?"
        self.name=' '
   def send(self):
        try:
            myword = "bot : " + self.speech
            print(myword)
            return myword
        except ConnectionAbortedError:
            print('Server closed this connection!')
        except ConnectionResetError:
            print('Server is closed!')
   def kick(self,yn):
       if(yn):
           self.speech=self.name+' leave chatroom'
       else:
           self.speech='you have not permittion'
       return self.name
   def recv(self,msg):
            try:
                emty=[' ',' ']
                commmand=msg.split()
                commmand.extend(emty)
                if(commmand[2]!=""):
                   if(commmand[2]=="weather"):
                        weather = Weather(unit=Unit.CELSIUS)
                        if(commmand[3]==" "):
                            commmand[3]="桃園"
                        location = weather.lookup_by_location(commmand[3])
                        print(location)
                        condition = location.condition
                        self.speech=location.location.city+" "+condition.text+" "+condition.temp
                   elif(commmand[2]=="date"):
                       weather = Weather(unit=Unit.CELSIUS)
                       if(commmand[3]==" "):
                            commmand[3]="桃園"
                       location = weather.lookup_by_location(commmand[3])
                       condition = location.condition
                       self.speech=location.location.city+" "+condition.date
                   elif(commmand[2]=="convert"):
                       try:
                          c = CurrencyConverter()
                          result=c.convert(float(commmand[3]),commmand[4], commmand[5])
                          self.speech=commmand[3]+' '+commmand[4]+"="+str(result)+' '+commmand[5]
                       except ValueError:
                           print("ValueError")
                           self.speech="please input correct value"
                       except TypeError:
                           print("ValueError")
                           self.speech="please input correct value"
                   elif(commmand[2]=="kick"):
                       self.name=commmand[3]
                       return True

                return False


            except ConnectionAbortedError:
                print('Server closed this connection!')

            except ConnectionResetError:
                print('Server is closed!')






