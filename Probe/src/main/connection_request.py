import grpc
from grpc_bin import survey6_pb2_grpc as pb2_grpc        
from grpc_bin import survey6_pb2 as pb2
from datetime import datetime
import os
import config
import utils


filename = "connection_request_"+ datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
logger = utils.getLogger(filename)

hostname = os.uname().nodename

# Connecting to the GRPC server
with grpc.insecure_channel(config.GRPC_SERVER) as channel: 

    stub = pb2_grpc.ClientConnectionStub(channel)

    # generating request 
    req = pb2.ClientConnectRequest(host_name = hostname)
    req.request_epoch_time.FromDatetime(datetime.now())

    # Sending request
    res = stub.ClientConnect(req)

    logger.info("Connection request sent to the server")
    logger.info("Connection status: {}".format(res.connection_status))
    logger.info("Connection uid: {}".format(res.uid))
    
    # Saving the user id
    with open(config.UID_FILE_PATH, 'w') as f:
        f.write(res.uid)

    logger.info("UID is stored in: {}".format(config.UID_FILE_PATH))