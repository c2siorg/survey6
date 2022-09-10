from datetime import datetime
from unittest.mock import MagicMock
from mock import patch
import unittest
  
import sys
sys.path.append("../main")

from data.ClientDao import ClientDao
from data.DbHelper import DbHelper
from service_methods.ClientConnectionService import ClientConnectionService
from service_methods.grpc_bin import survey6_pb2 as pb2

def __init__(self):
    self.db = DbHelper('test.db')
    self.db.query("CREATE TABLE IF NOT EXISTS CurrentClients (id BINARY(16) PRIMARY KEY, hostname TEXT, registrationEpochTime TIMESTAMP, lastActiveTime TIMESTAMP, currentStatus BOOLEAN, lastDataReceivedTime TIMESTAMP)",{})
    self.db.query("CREATE TABLE IF NOT EXISTS ClientArchives (id BINARY(16) PRIMARY KEY, hostname TEXT , lastActiveTime TIMESTAMP)",{})

class test_application(unittest.TestCase):
    
    @classmethod
    def tearDownClass(cls):
        db = DbHelper('test.db')
        db.query("DROP TABLE IF EXISTS CurrentClients",{})
        db.query("DROP TABLE IF EXISTS ClientArchives",{})
        
    
    def test_client_connect(self):
        
        with patch.object(ClientDao, '__init__', __init__):
            
            context = MagicMock()
            service = ClientConnectionService()
            
            request = pb2.ClientConnectRequest(host_name = "User Test 2")
            request.request_epoch_time.FromDatetime(datetime.now())
            
            response = service.ClientConnect(request,context)
            
            self.assertEqual(response.connection_status,pb2.SUCCESS)
            self.assertIsNotNone(response.uid)

    
    def test_duplicate_client_connect(self):
        with patch.object(ClientDao, '__init__', __init__):
            context = MagicMock()
            service = ClientConnectionService()
            
            request = pb2.ClientConnectRequest(host_name = "User Test 3")
            request.request_epoch_time.FromDatetime(datetime.now())
            
            response = service.ClientConnect(request,context)
            self.assertEqual(response.connection_status,pb2.SUCCESS)
            
            # Server should not process multiple connection requests from same client. 
            # This gives an easy way for flood attacks
            # Fix this
            response = service.ClientConnect(request,context)
            self.assertEqual(response.connection_status,pb2.FAILURE)
    
    def test_client_disconnect_correct_uid(self):

        with patch.object(ClientDao, '__init__', __init__):
            
            request = pb2.ClientConnectRequest(host_name = "User Test 2")
            request.request_epoch_time.FromDatetime(datetime.now())
            context = MagicMock()
            service = ClientConnectionService()
            response = service.ClientConnect(request,context)
            self.assertEqual(response.connection_status,pb2.SUCCESS)
            
            request = pb2.ClientDisconnectRequest(host_name = "User Test 2", uid = response.uid)
            response = service.ClientDisconnect(request,context)
            self.assertEqual(response.disconnection_status,pb2.SUCCESS)

    
    def test_client_disconnect_incorrect_uid(self):
        
        with patch.object(ClientDao, '__init__', __init__):
            context = MagicMock()
            service = ClientConnectionService()
            
            request = pb2.ClientConnectRequest(host_name = "User Test 4")
            request.request_epoch_time.FromDatetime(datetime.now())

            response = service.ClientConnect(request,context)
            self.assertEqual(response.connection_status,pb2.SUCCESS)
            
            request = pb2.ClientDisconnectRequest(host_name = "User Test 4", uid = "fcefce")
            response = service.ClientDisconnect(request,context)
            self.assertEqual(response.disconnection_status,pb2.FAILURE)
    

    
if __name__ == "__main__":
    unittest.main()
    
    