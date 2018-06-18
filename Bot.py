from weather import Weather, Unit


class Bot():
   def __init__(self):
        self.speech="?"
   def send(self):
        try:
            myword = "bot : " + self.speech
            print(myword)
            return myword
        except ConnectionAbortedError:
            print('Server closed this connection!')
        except ConnectionResetError:
            print('Server is closed!')

   def recv(self,msg):
            try:
                emty=[' ',' ']
                commmand=msg.split()
                commmand.extend(emty)
                if(commmand[2]!=""):
                   if(commmand[2]=="weather"):
                        weather = Weather(unit=Unit.CELSIUS)
                        if(commmand[3]==" "):
                            place="桃園"
                        location = weather.lookup_by_location(place)
                        print(location)
                        condition = location.condition
                        self.speech=location.location.city+" "+condition.text+" "+condition.temp
            except ConnectionAbortedError:
                print('Server closed this connection!')

            except ConnectionResetError:
                print('Server is closed!')






