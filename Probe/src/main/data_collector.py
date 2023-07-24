import re
import scapy.all as scapy
import os
import sys
import datetime
import json
import utils
import config


class DataCollector():


    def __init__(self,noOfPackets = 5) -> None:

        self.logfilename = "capture_"+ datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
        self.logger = utils.getLogger(self.logfilename)

        self.capture_path = config.CAPTURE_PATH

        if not os.path.exists(self.capture_path):  
            try: 
                os.makedirs(self.capture_path)
            except OSError as e:
                self.logger.error(e)
                sys.exit(0)
        
        self.noOfPackets = noOfPackets
        self.myhost = os.uname().nodename

        try: 
            with open(config.UID_FILE_PATH, 'r') as f:
                self.uid = f.read()
        except:
            self.logger.error("No UID found, abborting data collection")
            sys.exit(0)

    def writeMetaData(self):
        

        posix = os.uname()
        with open('/proc/meminfo') as f:
            meminfo = f.read()
        matched = re.search(r'^MemTotal:\s+(\d+)', meminfo)
        if matched: 
            mem_total_kB = int(matched.groups()[0])

            
        metadata = {
            'UID': self.uid,
            'sysname':posix.sysname,
            'nodename':posix.nodename,
            'release':posix.release,
            'version':posix.version,
            'machine':posix.machine,
            # 'Number of packets captured per .pcap': self.noOfPackets,
            'CPU Count':os.cpu_count(),
            'total memory': mem_total_kB,
            'all interfaces': scapy.get_if_list(),
            'sniff interface': str(scapy.conf.iface),
            'ip4 address': scapy.get_if_addr(scapy.conf.iface),
            'mac address': scapy.get_if_hwaddr(scapy.conf.iface),
        }

        metadata_json = json.dumps(metadata, indent=4)

        
        metadata_path = "{}/{}.json".format(self.capture_path,self.uid)
        try:
            with open(metadata_path,"w") as f:
                f.write(metadata_json)
        except FileNotFoundError as e:
            self.logger.error(e)
            sys.exit(0)

    def dataCapture(self,filename):
        ''' 
        - Captures {noOfPackets} IPv6 data packets from all interfaces of the probe
        - Stores the captured packets in a single .pcap file of name {filename}
        - Annotates the .pcap file with hostname & date of capture
        - Input: 
            * noOfPackets : number of packets to be captured
            * filename : the name by which the .pcap file is stored
        - Output:
            * none 
        '''


        packet_path = "{}/{}.pcap".format(self.capture_path,filename)

        try:
            capture = scapy.sniff(filter="ip6", count = self.noOfPackets)
        except PermissionError as e:
            self.logger.error(e)
            sys.exit(0)
        except Exception as e:
            self.logger.error(e)
            sys.exit(0)
        else:
            self.logger.info("captured {} packets".format(self.noOfPackets))

        
        try:
            scapy.wrpcap(packet_path,capture)
        except OSError as e:
            self.logger.error(e)
            sys.exit(0)
        else:
            self.logger.info("Saved the captured packets as {}.pcap".format(filename))
        
        now = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S") 

        self.logger.info("captured by: {}".format(self.myhost))
        self.logger.info("captured on {}".format(now))


            
       


if __name__ == '__main__':


    dataCollector = DataCollector(noOfPackets=5)
    dataCollector.writeMetaData()
    while True:
        dataCollector.dataCapture(filename="f{}".format(datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")))