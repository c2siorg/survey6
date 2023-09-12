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

![chart2](https://github-production-user-asset-6210df.s3.amazonaws.com/61967013/263470237-21e180e0-0bb3-4248-a7a4-9af0ad1895cb.png)

You can find the setup and installation guide for each of the modules in their respective module directories and they are linked below too. 
***
## Probe

Intercept and collect all the ipv6 traffic (regardless of the protocol) therefore libpcap is preferable. probe binaries must run as a service of the operating system (OS could be Linux host).  Moreover, the probe cast a heartbeat to the C&C server for its heath checks mechanisms. This must be implemented using gRPC.  Probe identifies ideal states of the host network interface and uses those time windows to send the collected ipv6 pcap. For this, data must be annotated with meta-information for aggregation purposes (meta information could be discussed)   

### Probe CLI
Probe CLI is a sub-component of Probe that allows starting (passing the registering string from C&C server, eg- How you add new nodes to Kubernetes), suspending the probe's execution in the host machine. 

### Stack
Python, GRPC, Scapy

### Module Info, Setup \& Installation Guide
* [Probe](./Probe/README.md)

### Demo
* [Probe Video](https://drive.google.com/file/d/1fSBYXjHva7zfjUsIW2_bN7vebJO_SB8Q/view?usp=sharing)
* [Probe CLI Video]
***
## C\&C server

C&C server should have the Probe registering mechanism. And it listens to registered Prob's heartbeats.  WebUI shows the active states of Probes in a list view. 

### Stack
Python, gRPC, Redis queue, SQLite, Flask

### Module Info, Setup \& Installation Guide
* [C&C Server](./C%26C%20Server/README.md)

### Demo Video
* [Running from package](https://drive.google.com/file/d/1kmxOZZXKXUTpBfkJcs1gcroiuIDU3tys/view?usp=sharing)
* [Testing](https://drive.google.com/file/d/1mlhD5XWk1s7ELlx36w6s4_0fUfeKQu8D/view?usp=sharing)

***
## Data Aggregator.

Data Collection server. Collects, cleans and stores IPv6 packets for future study.
* Receive IPv6 packets from clients
* Hourly and daily zipping of data files

* * *

# Contributing
We are glad that you are willing to contribute. Tasks to be taken up next are:
1. Fix issue that fails one testcase - *C&C Server*
2. Display status of connected and registered probes - *C&C server*
3. Sending password pf the data aggregator from server to the probe on regisration 

Stretch goal:
1. Hosting the debian packages


Please do follow [contributing guidelines](./CONTRIBUTING.md) to help the maintainers. Thank you for your wonderful cooperation! 
