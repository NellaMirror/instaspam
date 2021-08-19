# coding=utf-8
#!/usr/bin/env python3

import sys

def check_modules():
    try:
        import requests
    except:
        print("[-] 'requests' The package is not installed!")
        print("[*] To install 'pip install requests[socks]' yazın!")
        sys.exit(0)

    try:
        import colorama
    except Exception as e:
        print("[-] 'colorama' The package is not installed!")
        print("[*] To install 'pip install colorama' yazın!")
        print(e)
        sys.exit(0)

    try:
        import asyncio
    except:
        print("[-] 'asyncio' The package is not installed!")
        print("[*] To install 'pip install asyncio' yazın!")
        sys.exit(0)

    try:
        import proxybroker
    except:
        print("[-] 'proxybroker' The package is not installed!")
        print("[*] To install 'pip install proxybroker' yazın!")
        sys.exit(0)

    try:
        import warnings
    except:
        print("[-] 'warnings' The package is not installed!")
        print("[*] To install 'pip install warnings' yazın!")
        sys.exit(0)

    import warnings
    warnings.filterwarnings("ignore")

    from colorama import init
    init()
