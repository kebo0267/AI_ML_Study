from datetime import datetime, timedelta
import json

class TaskRecord:
    def __init__(self):
        self._taskId = int(0)
        self._userId = int(0)
        self._title = ""
        self._description = ""
        self._dueDate = datetime.now()
        self._createDate = datetime.now()
        self._startDate = datetime.now()
        self._completeData = datetime.now()

    @property
    def taskId(self):
        return self._taskId
    
    @taskId.setter
    def taskId(self,new_taskId):
        self._taskId = new_taskId

    @property
    def userId(self):
        return self._userId
    
    @userId.setter
    def userId(self,new_userId):
        self._userId = new_userId

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,new_title):
        self._title = new_title

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self,new_desc):
        self._description = new_desc

    @property
    def dueDate(self):
        return self._dueDate
    
    @dueDate.setter
    def dueDate(self,new_dueDate):
        self._dueDate = new_dueDate

    @property
    def createDate(self):
        return self._createDate
    
    @createDate.setter
    def createDate(self,new_createDate):
        self._createDate = new_createDate

    @property
    def startDate(self):
        return self._startDate
    
    @startDate.setter
    def startDate(self,new_startDate):
        self._startDate = new_startDate

    @property
    def completeData(self):
        return self._completeData
    
    @createDate.setter
    def completeData(self,new_completeData):
        self._completeData = new_completeData