# Data Aggregator

## Description
Data Collection server. Collects, cleans and stores IPv6 packets for future study.

## Implemeted Functionalities
* Receive IPv6 packets from clients
* Hourly and daily zipping of data files

## Technology stack
* python
* cron jobs

## Folder Structure
```
.
├── config.py
├── daily_zip.py
├── hourly_zip.py
└── README.md
```

## Data Aggregator Setup
1. Clone the repository
```
git clone https://github.com/web-telescope/survey6.git
```
2. Move to C&C Server
```
cd ../Data\ Aggregator/
```
3. Create cron jobs
1. Edit Crontab 
`sudo crontab -e`
2. Select your editor
3. Add following two lines
```
0 * * * * sudo /usr/bin/python3 [Path to survey6]/Data\ Aggregator/hourly_zip.py
0 0 * * * sudo /usr/bin/python3 [Path to survey6]/Data\ Aggregator/daily_zip.py
```
Such as,
```
0 * * * * sudo /usr/bin/python3 /home/dhruvi/survey6/Data\ Aggregator/hourly_zip.py
0 0 * * * sudo /usr/bin/python3 /home/dhruvi/survey6/Data\ Aggregator/daily_zip.py
```
4. To check
```
sudo crontab -l
```
![Alt text](https://github.com/c2siorg/GSoC/assets/61967013/0a15753d-f5e4-4343-8e26-4a8b262d9172)
5. To view sys logs
```
grep CRON /var/log/syslog
```
## Data Aggregator Server Directory
```
.
├── clientEnd
│   └── dhruvi-HP-Pavilion-Laptop-15-cs2xxx //client dumps the files here
│       ├── f23-07-2023-16-32-19.json
│       ├── f23-07-2023-16-32-19.pcap
│       ├── f23-07-2023-16-32-34.pcap
│       └── f23-07-2023-16-32-38.pcap
└── processedFiles
    └── dhruvi-HP-Pavilion-Laptop-15-cs2xxx 
        ├── daily
        │   ├── 2023-07-21.zip
        │   └── 2023-07-22.zip
        └── hourly
            ├── 2023-07-23_15-33.zip
            ├── 2023-07-23_14-29.zip
            .
            .
            
```
