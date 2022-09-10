import grpc
from concurrent import futures
import time

from service_methods.ClientConnectionService import ClientConnectionService
from service_methods.grpc_bin import survey6_pb2_grpc as pb2_grpc
import Utils



def serve():
    
    LOGGER = Utils.getLogger('log4')

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_ClientConnectionServicer_to_server(ClientConnectionService(), server)
    
    server.add_insecure_port('[::]:32001')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()