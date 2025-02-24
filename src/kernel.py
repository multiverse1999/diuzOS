# SPDX-License-Identifier: GPL-3.0 
'''*
   * diuz/version 0.2/kernel.py
   *
   * Copyright (C) 2022 multiverse1999
   *
   * this file is kernel
   *'''
import os
import datetime
import exp
import cmd
import time
import sys
from winreg import *
import ctypes

dt = datetime.datetime.now()  

def help():
   print("'echo <line_text>' - for print your own line\n")
   print("'exit' - exit from system\n")
   print("'date' - show now date\n")
   print("'time' - show now time\n")
   print("'clean' - clear all terminal\n")
   print("'dfs' - open uni file system\n")
   print("'curl' - open links\n")
   print("'ping' - check network connection\n") 

def main(start, exit, user):
   print("\n")
   while start:
      try:
         cmd = input(f"[{user}]@[{os.environ['COMPUTERNAME']}]:~$ ")
         echo = cmd.split()
         if cmd == "exit":
            start = exit
         elif cmd == "help":
            help()
         elif echo[0] == "echo":
            line = ""
            for i in range(1, len(echo)):
               line += echo[i]
               line += " "
            print(f"{line}\n")
         elif cmd == "clean":
            os.system("cls")
         elif cmd == "date":
            print(f"{dt.year}-{dt.month}-{dt.day}")
         elif cmd == "time":
            print(f"{dt.hour}-{dt.minute}-{dt.second}")
         elif cmd == "dexp":
            exp.dexp()
         elif cmd == "curl":
            import browser
         elif cmd == "ping":
            import net
            net.test("http://www.ya.ru")
         elif cmd == "dfetch":
            import fetch
      except:
         pass
