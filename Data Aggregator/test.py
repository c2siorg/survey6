import os
import zipfile
import datetime
import time
import config
import sys

input_directory = config.BACKUP_PATH
output_directory = config.RAW_PCAP_FILES

def create_hourly_zip2():
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
                
def create_daily_zip():

    yesterday = datetime.datetime.now() - datetime.timedelta (days=1)
    # yesterday = datetime.datetime.now()

    for clientDir in os.listdir(output_directory):

        zip_filename = f"{yesterday.strftime('%Y-%m-%d')}.zip"
        clientProcessDir = os.path.join(output_directory,clientDir) 
        hourly_zip_directory = os.path.join(clientProcessDir,"hourly")
        daily_zip_directory = os.path.join(clientProcessDir,"daily")

        if not os.path.exists(daily_zip_directory):  
            try: 
                os.makedirs(daily_zip_directory)
            except OSError as e:
                sys.exit(0)

        with zipfile.ZipFile(os.path.join(daily_zip_directory, zip_filename), "w") as zipf:
            for root, _, files in os.walk(hourly_zip_directory):
                for file in files:
                    if file.endswith(".zip") and file.startswith(yesterday.strftime('%Y-%m-%d')):
                        file_path = os.path.join(root, file)
                        zipf.write(file_path, os.path.relpath(file_path, hourly_zip_directory))



# create_hourly_zip2()
create_daily_zip()
# print(os.walk(input_directory))