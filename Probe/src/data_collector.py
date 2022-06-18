import scapy.all as scapy
import os
import datetime


def dataCapture(noOfPackets = 2,filename = "f"):
    ''' f '''


    path = "../capture"
    if not os.path.exists(path):   
        os.makedirs(path)

    path_packet = f"../capture/{filename}.pcap"

    capture = scapy.sniff(filter="ip6", count = noOfPackets)
    scapy.wrpcap(path_packet,capture)
    print(f"captured {noOfPackets} packets")

    myhost = os.uname().nodename
    os.setxattr(path_packet,'user.hostname',myhost.encode('ascii'))
    print(f"captured by: {myhost}")

    now = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    os.setxattr(path_packet,'user.date',now.encode('ascii'))
    print(f"captured on {now}")

    print("------------------------\n")



