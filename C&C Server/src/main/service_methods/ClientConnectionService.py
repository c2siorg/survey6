from datetime import datetime
import imp
from sqlite3 import OperationalError
import sqlite3

from .grpc_bin import survey6_pb2_grpc as pb2_grpc        
from .grpc_bin import survey6_pb2 as pb2

from data.ClientDao import ClientDao
from data import DataUtils
import Utils
import datetime




class ClientConnectionService(pb2_grpc.ClientConnectionServicer):
        
    def __init__(self):
        filename = "Server_"+ datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
        self.LOGGER = Utils.getLogger(filename)     
        
        
    def ClientConnect(self, request, context):
        
        client_db = ClientDao()  
        time = request.request_epoch_time.seconds
        uid,_ = client_db.addClient({'hostname': request.host_name,'registrationEpochTime': time,'lastActiveTime': time,'currentStatus': 1})

        self.LOGGER.info("Client connected with host name : {}".format(request.host_name))
        
        return pb2.ClientConnectResponse(connection_status = 1,uid = uid)

    def ClientDisconnect(self, request, context):        
        
        client_db = ClientDao()  
        
        try: 
            removed_client_details = client_db.removeClient(request.uid)
        except sqlite3.OperationalError as e:
            self.LOGGER.error(e)
            return pb2.ClientDisconnectResponse(disconnection_status = 0)
        
        else:
            if (len(removed_client_details) == 0):
                self.LOGGER.info("No Client {} found".format(request.host_name))
                return pb2.ClientDisconnectResponse(disconnection_status = 0)
            else: self.LOGGER.info("Client {} deleted from clients db".format(request.host_name))
            
        try:
            client_archive = DataUtils.clientToArchive(removed_client_details)
        except Exception as e:
            self.LOGGER.error("Client to Archive error: {}".format(e))
            return pb2.ClientDisconnectResponse(disconnection_status = 0)
            
        try:
            client_db.addArchive(client_archive)            
        except sqlite3.OperationalError as e:
            self.LOGGER.error(e)
            return pb2.ClientDisconnectResponse(disconnection_status = 0)
        else:
            self.LOGGER.info("CLient {} added from archives db".format(request.host_name))
            
        return pb2.ClientDisconnectResponse(disconnection_status = 1)
        
        
        
        
    def Heartbeat(self, request, context):
        client_db = ClientDao()  
        time = request.request_epoch_time.seconds

        try: 
            rowsAffected = client_db.updateClientLastActiveTime(request.uid,request.request_epoch_time.seconds)
        except sqlite3.OperationalError as e: 
            self.LOGGER.error(e)
            return pb2.HeartbeatAck(ack = 0)

        return pb2.HeartbeatAck(ack = 1)

    def GrantReceiveData(self, request, context):
        pass
         