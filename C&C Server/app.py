import grpc
from concurrent import futures
import time


def serve():
    

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server.add_insecure_port('[::]:32000')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()