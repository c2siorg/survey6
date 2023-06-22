import grpc
from grpc_bin import survey6_pb2_grpc as pb2_grpc        
from grpc_bin import survey6_pb2 as pb2
from datetime import datetime
import os
import logging
import config
import utils


filename = "disconnection_request_"+ datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
logger = utils.getLogger(filename)

hostname = os.uname().nodename

# Read the probe uid that was stored in the system
uid = ""
with open(config.UID_FILE_PATH, 'r') as f:
    uid = f.read()

# Connecting to the GRPC server
with grpc.insecure_channel(config.GRPC_SERVER) as channel: 

    stub = pb2_grpc.ClientConnectionStub(channel)

    # generating request
    req = pb2.ClientDisconnectRequest()
    req.request_epoch_time.FromDatetime(datetime.now())
    req.host_name = hostname
    req.uid = uid 

    # sending request
    res = stub.ClientDisconnect(req)
    logger.info("Disconnection request sent")
    logger.info("Disconnection status: {}".format(res.disconnection_status))





