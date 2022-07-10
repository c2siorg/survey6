import service_methods.grpc_bin.survey6_pb2_grpc as pb2_grpc        
import service_methods.grpc_bin.survey6_pb2 as pb2
from data.ClientDao import ClientDao

class ClientConnectionService(pb2_grpc.ClientConnectionServicer):
    
    # def __init__(self,*args, **kwargs):
    #     self.client_db = ClientDao()
        
        
    def ClientConnect(self, request, context):
        
        print(request)
        client_db = ClientDao()  
        client_db.addClient({'hostname': request.host_name,'registrationEpochTime': "5",'lastActiveTime': "5",'currentStatus': 1})
        
        return pb2.ClientConnectResponse(connection_status = 1)

    def ClientDisconnect(self, request, context):
        pass
        
    def Heartbeat(self, request, context):
        pass

    def GrantReceiveData(self, request, context):
        pass
        