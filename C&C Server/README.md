# C&C Server

## Auto Setup
```
source setup.bash 
```
### Server commands
1. To start the server
```
cncserver start
```
2. To check server status
```
cncserver status
```
3. To stop the server
```
cncserver stop
```

## In case of manual set up
1. Copy `server.service` in path ` /etc/systemd/system/ `
2. Reload the deamon 
```
systemctl daemon-reload
```
3. Starting the server
```
systemctl start server
```
4. Check Status
```
systemctl status server
```
5. Stop Server
```
systemctl stop server
```