from dotenv import load_dotenv
import os

load_dotenv()


CAPTURE_PATH = "/tmp/survey6/capture"

if "CAPTURED_PACKET_PATH" in os.environ:
    CAPTURE_PATH = os.getenv('CAPTURED_PACKET_PATH')


LOG_PATH = "/tmp/survey6/logs"

if "LOG_PATH" in os.environ:
    LOG_PATH = os.getenv('LOG_PATH')


BACKUP_PATH = "dhruvi@dhruvi-HP-Pavilion-Laptop-15-cs2xxx:/tmp/survey6/backup"

if "BACKUP_PATH" in os.environ:
    BACKUP_PATH = os.getenv('BACKUP_PATH')

    