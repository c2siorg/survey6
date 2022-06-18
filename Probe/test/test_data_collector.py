import sys
import scapy.all as scapy
import os
sys.path.insert(1, '../src')
import data_collector



if __name__ == '__main__':

    filename = 'capture1'
    data_collector.dataCapture(5,filename)

    path_packet = f"../capture/{filename}.pcap"


    print("TEST DATA:")
    print("------------------------")

    scapy_cap = scapy.rdpcap(path_packet)
    print("Packet Capture Summary: ")
    print(scapy_cap.summary())

    print("\nMeta data : ")
    print(f"Host Name: {os.getxattr(path_packet,'user.hostname').decode('ascii')}")
    print(f"Date: {os.getxattr(path_packet,'user.date').decode('ascii')}")


