import UserInfo

class UserList:
    def __init__(self):
        self.userList = []
        self.nextUserId = 0
        self.userListFileName = "userList.jsonl"

    def addUser(self,userName,password):
        user = UserInfo()
        user.userId = self.nextUserId
        user.userName = userName
        user.password = password
        self.userList.append(user)
        self.nextUserId += 1

    def removeUser(self,userName):
        for index in range(0, len(self.userList)):
            if userName == self.userList[index].userName:
                self.userList.pop(index)
                break

    def getUser(self,userName):
        retVal = None
        for index in range(0, len(self.userList)):
            if userName == self.userList[index].userName:
                retVal = self.userList[index]
                break
        return retVal
    
    def saveRecords(self):
        jFile = open(self.userListFileName,"w")
        for records in self.userList:
            jFile.write(records.getAsJson())
            jFile.write("\n")
        jFile.close()

