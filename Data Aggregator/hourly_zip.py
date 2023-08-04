import os
import zipfile
import datetime
import time
import config
import sys

input_directory = config.BACKUP_PATH
output_directory = config.RAW_PCAP_FILES

def create_hourly_zip():
    for clientDir in os.listdir(input_directory):
        clientInputDir = os.path.join(input_directory,clientDir) 
        clientProcessDir = os.path.join(output_directory,clientDir) 
        hourly_zip_directory = os.path.join(clientProcessDir,"hourly")

        if not os.path.exists(hourly_zip_directory):  
            try: 
                os.makedirs(hourly_zip_directory)
            except OSError as e:
                sys.exit(0)

        now = datetime.datetime.now()
        zip_filename = f"{now.strftime('%Y-%m-%d_%H-%M')}.zip"

        if(len(os.listdir(clientInputDir)) == 0):
             print("empty dir")
             return

        with zipfile.ZipFile(os.path.join(hourly_zip_directory, zip_filename), "w") as zipf:
            for file in os.listdir(clientInputDir):
                if(file.startswith(now.strftime('f%d-%m-%Y-%H'))):
                    file_path = os.path.join(clientInputDir,file)
                    zipf.write(file_path,file)
                    os.remove(file_path)



if __name__ == "__main__":
    create_hourly_zip()