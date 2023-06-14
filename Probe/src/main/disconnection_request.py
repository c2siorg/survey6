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

# Read the probe uid that was stored in the system
uid = ""
with open(os.path.expanduser(UID), 'r') as f:
    uid = f.read()

# Connecting to the GRPC server
server_ip = os.getenv('GRPC_SERVER')
with grpc.insecure_channel(server_ip) as channel: 

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





