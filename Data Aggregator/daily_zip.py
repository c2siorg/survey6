import os
import zipfile
import datetime
import time
import config
import sys

input_directory = config.BACKUP_PATH
output_directory = config.RAW_PCAP_FILES

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
                        os.remove(file_path)


if __name__ == "__main__":
    create_daily_zip()