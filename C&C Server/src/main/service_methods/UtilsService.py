from .grpc_bin import survey6_pb2_grpc as pb2_grpc
from .grpc_bin import survey6_pb2 as pb2

class UtilsService(pb2_grpc.UtilsServicer):

    def ViewHealthOfClient(self, request, context):
        pass 

    def ViewDataRecieved(self, request, context):
        pass