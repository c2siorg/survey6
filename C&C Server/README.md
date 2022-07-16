C&C Server

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