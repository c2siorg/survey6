# survey6

[![Join the chat at https://gitter.im/web-telescope/survey6](https://badges.gitter.im/survey6/community.svg)](https://gitter.im/survey6/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

ipv6 survey Tool (survey6)
#### Brief explanation:  
Ipv6 is the internet's future, and it necessitated a more scalable survey tool to comprehend how routing and DNS function. The purpose of this project is to create an IPv6 listener that will passively collect IPv6 traffic data as a passive data collection tool for cyber security research.
#### Expected results: 
* Develop a Linux network probe to intercept ipv6 traffic 
* To centralize the data being intercepted by the probe, develop a geo-distributed grid application that integrated with the probe. 
#### Knowledge Prerequisite:  
* C++
* Linux
* * *
## Survey6 tool has three main components, follow describes each component and its functionalities.

## Probe

Intercept and collect all the ipv6 traffics (regardless of the protocol) therefore libpcap is preferable. probe binaries must run as a service of the operating system (OS could be Linux host).  Moreover, the probe cast a heartbeat to the C&C server for its heath checks mechanisms. This must be implemented using grpc.  Probe identifies ideal states of the host network interface and uses those time windows to send the collected ipv6 pcap.  For this. This data must be annotated with meta-information for aggregation purposes (meta information could be discussed)   

### Probe CLI
Probe CLI is a sub-component of Probe that allows starting (passing the registering string from C&C server, eg- How you add new nodes to Kubernetes ), suspending the probe's execution in the host machine. 

#### Stack
C/C++, GRPC,  libpcap, Linux Kernel Drivers Development,  

## C&C server

C&C server should have the Probe registering mechanism. And it listens to registered Prob's heartbeats.  WebUI shows the active states of Probes in a list view. 

#### Stack
Python, GRPC, Redis queue, SQL Lite, Flask

## Data Aggregator.

Data Aggregator is a series of scheduled Apache Airflow Dags

* DAG 1 - USe dpkt or scapy to parse the pcap files along with metadata.
* DAG2 - Spak Jobs to clean and aggregate the data and write to parquet.
* DAG3 - Error handling and cleansing temp data

#### Stack
Python, AirFlow, Spark, PySpark, scapy

* * *
## Component Weight

<table>
  <tr>
    <th>Component</th>
    <th>Component Weight</th>
  </tr>
    <tr>
    <th>Probe</th>
    <th>50%</th>
  </tr>
    <tr>
    <th>C&C server</th>
    <th>30%</th>
  </tr>
  <tr>
    <th>Data Aggregator</th>
    <th>20%</th>
  </tr>
 <table>
