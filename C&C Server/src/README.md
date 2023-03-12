# src
## Structure
```
.
├── main
│   ├── App.py
│   ├── data
│   │   ├── ClientDao.py
│   │   ├── DataUtils.py
│   │   ├── DbHelper.py
│   │   └── __init__.py
│   ├── logs
│   ├── service_methods
│   │   ├── ClientConnectionService.py
│   │   ├── grpc_bin
│   │   │   ├── survey6_pb2_grpc.py
│   │   │   └── survey6_pb2.py
│   │   ├── __init__.py
│   │   └── UtilsService.py
│   └── Utils.py
├── test
│   └── test_server.py
└── __init__.py
```
* `main` : server code
* `test` : test suite
