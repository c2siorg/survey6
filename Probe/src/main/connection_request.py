import grpc
from grpc_bin import survey6_pb2_grpc as pb2_grpc        
from grpc_bin import survey6_pb2 as pb2
from datetime import datetime
import os
import logging
from dotenv import load_dotenv



load_dotenv()


log_path = os.path.expanduser(os.getenv('LOG_PATH'))

if not os.path.exists(log_path):  
    try: 
        os.makedirs(log_path)
    except OSError as e:
        logging.error(e)
        print(e)
        sys.exit(0)
    
logfile_path = "{}/{}.log".format(log_path,"log1")

try:
    logging.basicConfig(filename=logfile_path,filemode = "a",format='%(asctime)s %(levelname)s: %(message)s',level=logging.INFO)
    logging.basicConfig(filename=logfile_path,filemode = "a",format='%(asctime)s %(levelname)s: %(message)s %(lineno)d',level=logging.ERROR)
except PermissionError as e:
    logging.error(e)
    print(e)
    sys.exit(0)

logger = logging.getLogger()

hostname = os.uname().nodename
UID = os.getenv('UID')

# Connecting to the GRPC server
with grpc.insecure_channel('[::]:32001') as channel: 

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
    with open(os.path.expanduser(UID), 'w') as f:
        f.write(res.uid)

    logger.info("UID is stored in: {}".format(UID))