from datetime import datetime

import service_methods.grpc_bin.survey6_pb2_grpc as pb2_grpc        
import service_methods.grpc_bin.survey6_pb2 as pb2

from data.ClientDao import ClientDao
from data.ArchiveDao import ArchiveDao
from data import DataUtils



class ClientConnectionService(pb2_grpc.ClientConnectionServicer):
        
        
    def ClientConnect(self, request, context):
        
        client_db = ClientDao()  
        time = request.request_epoch_time.seconds
        client_db.addClient({'hostname': request.host_name,'registrationEpochTime': time,'lastActiveTime': time,'currentStatus': 1})
        return pb2.ClientConnectResponse(connection_status = 1)

    def ClientDisconnect(self, request, context):
        
        client_db = ClientDao()  
        archive_db = ArchiveDao()
        
        removed_client_details = client_db.removeClient(request.host_name)
        
        client_archive = DataUtils.clientToArchive(removed_client_details)
        
        archive_db.addArchive(client_archive)
        
        return pb2.ClientDisconnectResponse(disconnection_status = 1)
        
        
        
        
    def Heartbeat(self, request, context):
        pass

    def GrantReceiveData(self, request, context):
        pass
        
        