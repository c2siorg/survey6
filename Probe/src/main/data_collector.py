import scapy.all as scapy
import os
import sys
import datetime
import json
import utils
import config




def dataCapture(noOfPackets = 2,filename = "f"):
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

    logfilename = "capture_"+ datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
    logger = utils.getLogger(logfilename)

    capture_path = config.CAPTURE_PATH

    if not os.path.exists(capture_path):  
        try: 
            os.makedirs(capture_path)
        except OSError as e:
            logger.error(e)
            sys.exit(0)
    
    packet_path = "{}/{}.pcap".format(capture_path,filename)

    try:
        capture = scapy.sniff(filter="ip6", count = noOfPackets)
    except PermissionError as e:
        logger.error(e)
        sys.exit(0)
    except Exception as e:
        logger.error(e)
        sys.exit(0)
    else:
        logger.info("captured {} packets".format(noOfPackets))

    
    try:
        scapy.wrpcap(packet_path,capture)
    except OSError as e:
        logger.error(e)
        sys.exit(0)
    else:
        logger.info("Saved the captured packets as {}.pcap".format(filename))
    

    myhost = os.uname().nodename
    logger.info("captured by: {}".format(myhost))

    now = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")    #change
    logger.info("captured on {}".format(now))

    metadata = {'hostname': myhost,'date':now, 'filename':"{}.pcap".format(filename)}
    metadata_json = json.dumps(metadata, indent=4)
    
    metadata_path = "{}/{}.json".format(capture_path,filename)
    try:
        with open(metadata_path,"w") as f:
            f.write(metadata_json)
    except FileNotFoundError as e:
        logger.error(e)
        sys.exit(0)
        
       


if __name__ == '__main__':

    i = 0
    while True:
        # Capture files
        dataCapture(noOfPackets=5,filename="f{}".format(i))
        i+=1


