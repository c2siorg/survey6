import os
import logging   
import config




    
def getLogger(logfilename):
    
    log_path = config.LOG_PATH


    if not os.path.exists(log_path):  
        try: 
            os.makedirs(log_path)
        except OSError as e:
            logging.error(e)
            sys.exit(0)
        
    logfile_path = "{}/{}.log".format(log_path,logfilename)

    try:
        logging.basicConfig(filename=logfile_path,filemode = "a",format='%(asctime)s %(levelname)s: %(message)s',level=logging.INFO)
        logging.basicConfig(filename=logfile_path,filemode = "a",format='%(asctime)s %(levelname)s: %(message)s %(lineno)d',level=logging.ERROR)
    except PermissionError as e:
        logging.error(e)
        sys.exit(0)

    return logging.getLogger()