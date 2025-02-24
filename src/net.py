# SPDX-License-Identifier: BSD 3-Clause License
'''*
   * diuz/version 0.2/net.py
   *
   * Copyright (C) 2022 multiverse1999
   *
   * this file is internet check
   *'''
import requests
from requests.api import request

print("wait for loading")
print("your internet connection:")

def test(mstr):
        res = requests.get(mstr)
        if res.status_code == 200:        
            print("connected!!!")
        else:
            print("not connected...")
     
if __name__ == "__main__":
    print(test(mstr = "http://www.ya.ru"))
