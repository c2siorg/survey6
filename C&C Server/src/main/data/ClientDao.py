from data.DbHelper import DbHelper
import uuid

class ClientDao(object):
   __db = None;
    
   def __init__(self):
      self.__db = DbHelper('clients.db')
      self.__db.query("CREATE TABLE IF NOT EXISTS CurrentClients (id BINARY(16) PRIMARY KEY, hostname TEXT, registrationEpochTime TIMESTAMP, lastActiveTime TIMESTAMP, currentStatus BOOLEAN, lastDataReceivedTime TIMESTAMP)",{})
    
   def addClient(self,client):
      client['uid']= uuid.uuid4().bytes.hex()
      self.__db.query("INSERT INTO CurrentClients (id,hostname,registrationEpochTime, lastActiveTime, currentStatus) VALUES(:uid,:hostname,:registrationEpochTime, :lastActiveTime, :currentStatus)",client)
      return client['uid'], client
      
      
   def removeClient(self,uid):
      
      removed_client =  self.__db.query("SELECT * FROM CurrentClients WHERE id = :uid;",{'uid' : uid}).fetchall()
      self.__db.query("DELETE FROM CurrentClients WHERE id = :uid;",{'uid' : uid})
      return removed_client
      
      
   def showClients(self):
      return self.__db.query("SELECT * FROM CurrentClients",{}).fetchall()
   


  
    
