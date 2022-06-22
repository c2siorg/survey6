import scapy.all as scapy
import os
import datetime
from dotenv import load_dotenv

load_dotenv()

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

    path_capture = os.getenv('CAPTURED_PACKET_PATH')
    if not os.path.exists(path_capture):  
        try: 
            os.makedirs(path_capture)
        except(e):
            print(e)
            return e

    path_packet = "{}/{}.pcap".format(path_capture,filename)

    try:
        capture = scapy.sniff(filter="ip6", count = noOfPackets)
        print("captured {} packets".format(noOfPackets))
    except(e):
        print(e)
        return e
    
    try:
        scapy.wrpcap(path_packet,capture)
        print("Saved the captured packets as {}.pcap".format(filename))
    except(e):
        print(e)
        return e

    myhost = os.uname().nodename
    os.setxattr(path_packet,'user.hostname',myhost.encode('ascii')) #change
    print("captured by: {}".format(myhost))

    now = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")    #change
    os.setxattr(path_packet,'user.date',now.encode('ascii'))
    print("captured on {}".format(now))




