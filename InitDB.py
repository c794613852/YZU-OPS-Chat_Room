from pymongo import MongoClient
from bson.objectid import ObjectId 


# 通訊類型
# from enum import Enum, IntEnum, unique
#
# try:
#     @unique
#     class OPERATION(Enum):
#         MSG = 0
#         NUMCHANGE = 1
#         ISALIVE = 2
#         CONNECT = 3
#         CHANGEPWD = 4
#         PWDCHANGE = 5
#         LOGIN = 6
# except ValueError as e:
#     print(e)
#
# spliteTag = '$@~&*^$'


class DataBaseChatRoom:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)  # 比较常用
        self.database = self.client["ChatRoom"]  # SQL: Database Name
        self.collection = self.database["user"]  # SQL: Table Name

    def loadData(self):
        pass
        return None

    # delete user by uname
    # dbChatRoom.deleteUser(['A'])
    def deleteUser(self, unameList):
        accoutexist=self.checkUserExist(unameList)
        print(accoutexist)
        if(accoutexist):
            self.collection.remove({'uname': unameList})
            print("delete successfully")
        else:
            print("this account is not exist")
        pass
        return 'successful'

    # insert user
    # dbChatRoom.insertUser(uname='A', upwd='A')
    def insertUser(self, uname, upwd):
        self.collection.insert_one({'uname': uname, 'upwd': upwd})
        print("insert successfully")
        pass
        return 'successful'

    def updataUser(self, uname, upwd,online):
        accountsame=self.queryByuname(uname, upwd)
        dbonline=self.onoffline(uname,upwd)
        temp=""
        if(accountsame) and (dbonline != online):
            temp = self.collection.update({'uname': uname},{'$set':{'upwd': upwd, 'online': online}})
        else:
            temp = self.collection.update({'uname': uname},{'$set':{'upwd': upwd}})

        if(temp["updatedExisting"]):
            result = "Update Successfull"
        else:
            result = "Update Fail"
        return result

    # check checkUserExist
    def checkUserExist(self, uname):
        accoutexist=False
        for account in self.collection.find({'uname': uname}).limit(1):
            print(account)
            accoutexist=True
        if(accoutexist):
            result="User is exist"
        else:
            result="User is not exist"
        return result

    # query user bu uname
    # dbChatRoom.queryByuname(uname='A', upwd='A')
    def queryByuname(self, uname, upwd):
        accountsame=False
        for account in self.collection.find({'uname': uname, 'upwd': upwd}):
            print (account)
            print("the name is find")
            accountsame=True
        return accountsame

    def onoffline(self,uname, upwd):
        for account in self.collection.find({'uname': uname, 'upwd': upwd}):
            print(account['online'])
        return account['online']

    def findone_information(self, uname):
        account=None
        for account in self.collection.find({'uname': uname}):
            print (account)
        return account

    # Init database
    # dbChatRoom.Initdatabase()
    def Initdatabase(self):
        userList = []
        userList.append({'uname': 'A', 'upwd': 'A', 'online': 'False'})
        userList.append({'uname': 'B', 'upwd': 'B', 'online': 'False'})
        userList.append({'uname': 'C', 'upwd': 'C', 'online': 'False'})
        userList.append({'uname': 'D', 'upwd': 'D', 'online': 'False'})
        userList.append({'uname': 'E', 'upwd': 'E', 'online': 'False'})
        self.collection.insert_many(userList)

    def colseClient(self):
        self.client.close()

def main():
    dbChatRoom = DataBaseChatRoom()
    dbChatRoom.Initdatabase()
    #dbChatRoom.insertUser('Q','Q')
    #dbChatRoom.deleteUser('A','A')
    #dbChatRoom.queryByuname('A','A')
    #dbChatRoom.updataUser('B','B','False')
    #dbChatRoom.onoffline('C','C')
    #dbChatRoom.checkUserExist('B')
    #if you fell too many data , you can use this instruction
    #dbChatRoom.findone_information('A')
    #dbChatRoom.collection.remove()
    dbChatRoom.colseClient()


if __name__ == "__main__":
    main()
