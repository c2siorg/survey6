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
│   │   ├── __init__.py
│   │   └── README.md
│   ├── README.md
│   ├── service_methods
│   │   ├── ClientConnectionService.py
│   │   ├── grpc_bin
│   │   │   ├── README.md
│   │   │   ├── survey6_pb2_grpc.py
│   │   │   └── survey6_pb2.py
│   │   ├── __init__.py
│   │   ├── README.md
│   │   └── UtilsService.py
│   └── Utils.py
├── test
│   └── test_server.py
│   └── README.md
└── __init__.py
```
* `main` : server code
* `test` : test suite
