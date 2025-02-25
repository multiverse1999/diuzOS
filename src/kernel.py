# SPDX-License-Identifier: BSD 3-Clause License
'''*
   * diuz/version 0.6/kernel.py
   *
   * Copyright (C) 2022, multiverse1999
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
   print("'echo <line_text>' - for print your own line")
   print("'exit' - exit from system")
   print("'date' - show now date")
   print("'time' - show now time")
   print("'clean' - clear all terminal")
   print("'dexp' - open uni file system")
   print("'curl' - open links")
   print("'ping' - check network connection")
   print("'dfetch' - fetch")
   print("'dpkg' - package manager")

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
            print(f"{line}")
         elif cmd == "clean":
            os.system("cls")
         elif cmd == "date":
            print(f"{dt.year}-{dt.month}-{dt.day}")
         elif cmd == "time":
            print(f"{dt.hour}-{dt.minute}-{dt.second}")
         elif cmd == "dexp":
            exp.dexp()
         elif cmd == "curl":
            import curl
         elif cmd == "ping":
            import net
            net.test("http://www.ya.ru")
         elif cmd == "dfetch":
            import fetch
            fetch.dfetch()
         elif cmd == "dpkg":
           import psh
           psh.open_multiple_powershell_windows()
      except:
         pass
