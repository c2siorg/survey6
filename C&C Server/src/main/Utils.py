import os
import logging
from dotenv import load_dotenv
import sys
load_dotenv()



def getLogger(filename = 'log1'):
    log_path = os.getenv('LOG_PATH')

    if not os.path.exists(log_path):  
        try: 
            os.makedirs(log_path)
        except OSError as e:
            logging.error(e)
            sys.exit(0)
        
    logfile_path = "{}/{}.log".format(log_path,filename)

    try:
        logging.basicConfig(filename=logfile_path,filemode = "w",format='%(asctime)s %(levelname)s: %(message)s',level=logging.INFO)
        # logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',level=logging.INFO)
        
        logging.basicConfig(filename=logfile_path,filemode = "w",format='%(asctime)s %(levelname)s: %(message)s %(lineno)d',level=logging.ERROR)
        # logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s %(lineno)d',level=logging.ERROR)
    except PermissionError as e:
        logging.error(e)
        sys.exit(0)

    return logging.getLogger()