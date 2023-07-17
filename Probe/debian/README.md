# /debian
### Source Package

## Structure
```
.
├── source
│   └── format
├── changelog
├── cnc-server.debhelper.log
├── cnc-server.substvars
├── compat
├── control
├── files
├── install
├── postinst
├── preinst
├── README.md
├── rules
└── watch
```
## /DEBIAN
Binary Package structure
```
.
├── cnc-server
    ├── DEBIAN
    │   ├── control
    │   ├── md5sums
    │   ├── postinst
    │   └── preinst
    ├── home
    │   └── survey6
    │       └── cnc-server
    │           ├── main
    │           ├── requirements.txt
    │           └── server.service
    └── usr
        ├── bin
        │   └── cnc-server
        └── share
            └── doc
                └── cnc-server
                    └── changelog.Debian.gz
```
