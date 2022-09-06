import sys
import scapy.all as scapy
import os
sys.path.append("..")
from main import data_collector



if __name__ == '__main__':

    filename = 'capture2'
    data_collector.dataCapture(5,filename)

    packet_path = f"../../capture/{filename}.pcap"


    print("TEST DATA:")
    print("------------------------")

    scapy_cap = scapy.rdpcap(packet_path)
    print("Packet Capture Summary: ")
    print(scapy_cap.summary())



