# Data

## Description
All database operations reside in this directory

## Structure
```
.
├── ClientDao.py
├── DataUtils.py
├── DbHelper.py
└── __init__.py
```

## Database schema

#### CurrentClients
<table>
<tr>
<td>id</td>
<td>hostname</td>
<td>registrationEpochTime</td>
<td>lastActiveTime</td>
<td>currentStatus</td>
<td>lastDataReceivedTime</td>
</tr>
</table>

#### ClientArchives
<table>
<tr>
<td>id</td>
<td>hostname</td>
<td>lastActiveTime</td>
</tr>
</table>


## Important classes & methods 

### class ClientDao
1. **addClient()**
> <u>Arguments</u>:
> Dict: {hostname,registrationEpochTime, lastActiveTime, currentStatus}
2. **removeClient()**
> <u>Arguments</u>: uid
> <u>Output</u>:
> List of removed clients
3. **showClients()**
> <u>Arguments</u>: -
> <u>Output</u>:List of all clients in current database

4. **addArchive()**
> <u>Arguments</u>: converted archive dictionary
> <u>Output</u>: 
