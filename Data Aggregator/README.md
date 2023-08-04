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