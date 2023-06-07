import subprocess
import time
from dotenv import load_dotenv
from datetime import datetime
import os
import logging
import sys


load_dotenv()

capture_path = os.getenv('CAPTURED_PACKET_PATH')
backup_path = "kali@kali:tmp/survey6/backup"
tarnsfer_log_path = os.getenv('TRANSFER_LOG_PATH')

if not os.path.exists(tarnsfer_log_path):  
    try: 
        os.makedirs(tarnsfer_log_path)
    except OSError as e:
        logging.error(e)
        print(e)
        sys.exit(0)

logfilepath = "{}/{}.log".format(tarnsfer_log_path,"survey6_backup_log"+ datetime.now().strftime("%m-%d-%Y-%H-%M-%S"))
print(logfilepath)

if __name__ == '__main__':

    f = open(logfilepath, "w")
    while True:
        # Transfer files to the server using RSync
        cmd = "rsync -partial -z -e 'ssh -p 22' {} {}".format(capture_path,backup_path)
        try: 
	        return_code = subprocess.call(cmd,shell=True,stdout=f)
	        if return_code == 0:
	            print("Command executed successfully.")
	        else:
	            print("Command failed with return code", return_code)
        except Exception as e:
            print("error", e)
	    # Wait for some time before transferring files again
        time.sleep(60)
        
