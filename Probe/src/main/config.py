from dotenv import load_dotenv
import os

load_dotenv()


CAPTURE_PATH = "/tmp/survey6/capture/"

if "CAPTURED_PACKET_PATH" in os.environ:
    CAPTURE_PATH = os.getenv('CAPTURED_PACKET_PATH')


LOG_PATH = "/tmp/survey6/logs"

if "LOG_PATH" in os.environ:
    LOG_PATH = os.getenv('LOG_PATH')


BACKUP_PATH = "survey6@dhruvi-HP-Pavilion-Laptop-15-cs2xxx:clientEnd"

if "BACKUP_PATH" in os.environ:
    BACKUP_PATH = os.getenv('BACKUP_PATH')


UID_FILE_PATH = "/tmp/survey6/uid.id"
if "UID_FILE_PATH" in os.environ:
    UID_FILE_PATH = os.getenv('UID_FILE_PATH')

GRPC_SERVER = "[::]:32001"
if "GRPC_SERVER" in os.environ:
    GRPC_SERVER = os.getenv('GRPC_SERVER')
