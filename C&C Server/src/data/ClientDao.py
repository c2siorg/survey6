from data.DbHelper import DbHelper

class ClientDao(object):
   __db = None;
    
   def __init__(self):
      self.__db = DbHelper()
      self.__db.query("CREATE TABLE IF NOT EXISTS Clients (id INTEGER PRIMARY KEY AUTOINCREMENT, hostname TEXT, registrationEpochTime TIMESTAMP, lastActiveTime TIMESTAMP, currentStatus BOOLEAN, lastDataReceivedTime TIMESTAMP)",{})
    
   def addClient(self,client):
      self.__db.query("INSERT INTO Clients (hostname,registrationEpochTime, lastActiveTime, currentStatus) VALUES(:hostname,:registrationEpochTime, :lastActiveTime, :currentStatus)",client)
      
   def showClients(self):
      return self.__db.query("SELECT * FROM Clients",{}).fetchall()
      
    
