import sys
import scapy.all as scapy
import os
sys.path.insert(1, '../src')
import data_collector



if __name__ == '__main__':

    filename = 'capture3'
    data_collector.dataCapture(2,filename)

    # packet_path = f"../capture/{filename}.pcap"


    # print("TEST DATA:")
    # print("------------------------")

    # scapy_cap = scapy.rdpcap(packet_path)
    # print("Packet Capture Summary: ")
    # print(scapy_cap.summary())

    # print("\nMeta data : ")
    # print(f"Host Name: {os.getxattr(packet_path,'user.hostname').decode('ascii')}")
    # print(f"Date: {os.getxattr(packet_path,'user.date').decode('ascii')}")


