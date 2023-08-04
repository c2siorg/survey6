from dotenv import load_dotenv
import os

load_dotenv()

BACKUP_PATH = "/home/survey6/clientEnd"

if "BACKUP_PATH" in os.environ:
    BACKUP_PATH = os.getenv('BACKUP_PATH')

RAW_PCAP_FILES  = "/home/survey6/processedFiles"
if "RAW_PCAP_FILES" in os.environ:
    RAW_PCAP_FILES = os.getenv('RAW_PCAP_FILES')
