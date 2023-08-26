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
0 * * * * sudo /usr/bin/python3 /home/dhruvi/survey6/Data\ Aggregator/hourly_zip.py
0 0 * * * sudo /usr/bin/python3 /home/dhruvi/survey6/Data\ Aggregator/daily_zip.py
```
4. To check
```
sudo crontab -l
```
5. To view sys logs
```
grep CRON /var/log/syslog
```

## Screenshots
![](./screenshots/clientTest.png)

## System service
![](./screenshots/system_service.png)

### Testing
![](./screenshots/testcases.png)

## Video Demo
* [Running from package](https://drive.google.com/file/d/1kmxOZZXKXUTpBfkJcs1gcroiuIDU3tys/view?usp=sharing)
* [Testing](https://drive.google.com/file/d/1mlhD5XWk1s7ELlx36w6s4_0fUfeKQu8D/view?usp=sharing)