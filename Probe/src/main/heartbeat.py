import grpc
from grpc_bin import survey6_pb2_grpc as pb2_grpc        
from grpc_bin import survey6_pb2 as pb2
from datetime import datetime
import os
import logging
import config
import utils
import time


filename = "health_"+ datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
logger = utils.getLogger(filename)

hostname = os.uname().nodename

# Read the probe uid that was stored in the system
uid = ""
try: 
    with open(config.UID_FILE_PATH, 'r') as f:
        uid = f.read()
except:
    uid = ""

# Connecting to the GRPC server
with grpc.insecure_channel(config.GRPC_SERVER) as channel: 

    stub = pb2_grpc.ClientConnectionStub(channel)

    # generating request
    req = pb2.HeartbeatSender()
    req.host_name = hostname
    req.uid = uid 
    logger.info("Kick off sending of heart beats")

    while(True):
        time_ = datetime.now()
        req.request_epoch_time.FromDatetime(time_)

        # sending request
        res = stub.Heartbeat(req)
        logger.info("Server response to heartbeat is {}".format(res))

        time.sleep(3)