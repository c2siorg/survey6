from datetime import datetime

import service_methods.grpc_bin.survey6_pb2_grpc as pb2_grpc        
import service_methods.grpc_bin.survey6_pb2 as pb2
from data.ClientDao import ClientDao


class ClientConnectionService(pb2_grpc.ClientConnectionServicer):
    
    # def __init__(self,*args, **kwargs):
    #     self.client_db = ClientDao()
        
        
    def ClientConnect(self, request, context):
        
        client_db = ClientDao()  
        time = request.request_epoch_time.seconds
        client_db.addClient({'hostname': request.host_name,'registrationEpochTime': time,'lastActiveTime': time,'currentStatus': 1})
        return pb2.ClientConnectResponse(connection_status = 1)

    def ClientDisconnect(self, request, context):
        pass
        
    def Heartbeat(self, request, context):
        pass

    def GrantReceiveData(self, request, context):
        pass
        