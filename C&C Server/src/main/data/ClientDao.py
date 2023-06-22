from .DbHelper import DbHelper
import uuid

class ClientDao(object):
   db = None;
    
   def __init__(self):
      self.db = DbHelper('clients.db')
      self.db.query("CREATE TABLE IF NOT EXISTS CurrentClients (id BINARY(16) PRIMARY KEY, hostname TEXT, registrationEpochTime TIMESTAMP, lastActiveTime TIMESTAMP, currentStatus BOOLEAN, lastDataReceivedTime TIMESTAMP)",{})
      self.db.query("CREATE TABLE IF NOT EXISTS ClientArchives (id BINARY(16) PRIMARY KEY, hostname TEXT , lastActiveTime TIMESTAMP)",{})

    
   def addClient(self,client):
      client['uid']= uuid.uuid4().bytes.hex()
      self.db.query("INSERT INTO CurrentClients (id,hostname,registrationEpochTime, lastActiveTime, currentStatus) VALUES(:uid,:hostname,:registrationEpochTime, :lastActiveTime, :currentStatus)",client)
      return client['uid'], client
      
      
   def removeClient(self,uid):
      
      removed_client =  self.db.query("SELECT * FROM CurrentClients WHERE id = :uid;",{'uid' : uid}).fetchall()
      self.db.query("DELETE FROM CurrentClients WHERE id = :uid;",{'uid' : uid})
      return removed_client
      
      
   def showClients(self):
      return self.db.query("SELECT * FROM CurrentClients",{}).fetchall()
   
   def addArchive(self, archive):
      self.db.query("INSERT INTO ClientArchives (id,hostname, lastActiveTime) VALUES(:uid,:hostname,:lastActiveTime)",archive)
      
   def updateClientLastActiveTime(self,uid,lastActiveTime):
      # UPDATE COMPANY SET ADDRESS = 'Texas' WHERE ID = 6;
      result = self.db.query("UPDATE CurrentClients SET lastActiveTime = (:lastActiveTime) WHERE id = :uid;",{'lastActiveTime': lastActiveTime,'uid' : uid})
      return result.rowcount


  
    
