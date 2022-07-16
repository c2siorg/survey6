from data.DbHelper import DbHelper

class ClientDao(object):
   __db = None;
    
   def __init__(self):
      self.__db = DbHelper('clients.db')
      self.__db.query("CREATE TABLE IF NOT EXISTS CurrentClients (id INTEGER PRIMARY KEY AUTOINCREMENT, hostname TEXT , registrationEpochTime TIMESTAMP, lastActiveTime TIMESTAMP, currentStatus BOOLEAN, lastDataReceivedTime TIMESTAMP)",{})
    
   def addClient(self,client):
      self.__db.query("INSERT INTO CurrentClients (hostname,registrationEpochTime, lastActiveTime, currentStatus) VALUES(:hostname,:registrationEpochTime, :lastActiveTime, :currentStatus)",client)
      
      
   def removeClient(self,host_name):
      removed_client =  self.__db.query("SELECT * FROM CurrentClients WHERE hostname = :hostname;",{'hostname' : host_name}).fetchall()
      self.__db.query("DELETE FROM CurrentClients WHERE hostname = :hostname;",{'hostname' : host_name})
      return removed_client
      
   def showClients(self):
      return self.__db.query("SELECT * FROM CurrentClients",{}).fetchall()


  
    
