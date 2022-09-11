# survey6

[![Join the chat at https://gitter.im/web-telescope/survey6](https://badges.gitter.im/survey6/community.svg)](https://gitter.im/survey6/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

ipv6 survey Tool (survey6)
# Brief explanation:  
Ipv6 is the internet's future, and it necessitated a more scalable survey tool to comprehend how routing and DNS function. The purpose of this project is to create an IPv6 listener that will passively collect IPv6 traffic data as a passive data collection tool for cyber security research.
## Goals: 
* Develop a Linux network probe to intercept ipv6 traffic 
* To centralize the data being intercepted by the probe, develop a geo-distributed grid application that integrated with the probe. 

## Survey6 tool has three main components, follow describes each component, its functionalities and setup.
1. [Probe](#probe)
2. [C&C Server](#cc-server)
3. [Data Aggregator](#data-aggregator)

![chart2](https://user-images.githubusercontent.com/61967013/189522889-f7c20d8f-4796-4aaf-9777-f90852f91d26.png)
You can find setup and installation guide for each of the modules in their respective module directories and they are linked below too. 
***
## Probe

Intercept and collect all the ipv6 traffics (regardless of the protocol) therefore libpcap is preferable. probe binaries must run as a service of the operating system (OS could be Linux host).  Moreover, the probe cast a heartbeat to the C&C server for its heath checks mechanisms. This must be implemented using grpc.  Probe identifies ideal states of the host network interface and uses those time windows to send the collected ipv6 pcap.  For this. This data must be annotated with meta-information for aggregation purposes (meta information could be discussed)   

### Probe CLI
Probe CLI is a sub-component of Probe that allows starting (passing the registering string from C&C server, eg- How you add new nodes to Kubernetes ), suspending the probe's execution in the host machine. 

### Stack
Python, GRPC, Scapy

### Module Info, Setup \& Installation Guide
* [Probe](./Probe/README.md)

### Demo
* [Probe Video](https://drive.google.com/file/d/1fSBYXjHva7zfjUsIW2_bN7vebJO_SB8Q/view?usp=sharing)
***
## C\&C server

C&C server should have the Probe registering mechanism. And it listens to registered Prob's heartbeats.  WebUI shows the active states of Probes in a list view. 

### Stack
Python, GRPC, Redis queue, SQL Lite, Flask

### Module Info, Setup \& Installation Guide
* [C&C Server](./C%26C%20Server/README.md)

### Demo Video
* [Running from package](https://drive.google.com/file/d/1kmxOZZXKXUTpBfkJcs1gcroiuIDU3tys/view?usp=sharing)
* [Testing](https://drive.google.com/file/d/1mlhD5XWk1s7ELlx36w6s4_0fUfeKQu8D/view?usp=sharing)

***
## Data Aggregator.

Data Aggregator is a series of scheduled Apache Airflow Dags

* DAG 1 - USe dpkt or scapy to parse the pcap files along with metadata.
* DAG2 - Spak Jobs to clean and aggregate the data and write to parquet.
* DAG3 - Error handling and cleansing temp data

### Stack
Python, AirFlow, Spark, PySpark, scapy

* * *

# Contributing
We are glad that you are willing to contribute. Tasks to be taken up next are:
1. Fix issue that fails one testcase - *C&C Server*
2. Heartbeat and health status check - *both modules : Probe and C&C Server*
3. Sending packets from probe and recieving packets at server - *both modules : Probe and C&C Server*
4. Create a debian package for the probe once it has significant development. [For this one could refer packaging procedure of C&C Server: [here](https://medium.com/scorelab/packaging-overview-74aaeead3655) and [here](https://medium.com/scorelab/debian-packaging-of-a-python-project-ca4dfac9ac98)] - *Probe*
5. Display status of connected and registered probes - *C&C server*

Stretch goal:
1. Hosting the debian packages


Please do follow [contributing guidelines](./CONTRIBUTING.md) to help the maintainers. Thank you for your wonderful cooperation! 

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
