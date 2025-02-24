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
import fs
import cmd
import time
import sys
from winreg import *
import ctypes

dt = datetime.datetime.now()  

def help():
   print("'echo <line_text>' - for print your own line\n")
   print("'qt' - exit from system\n")
   print("'dt' - show now date\n")
   print("'time' - show now time\n")
   print("'cln' - clear all terminal\n")
   print("'dfs' - open uni file system\n")
   print("'curl' - open links\n")
   print("'chnet' - check network connection\n") 

def main(start, exit, user):
   print('''\n''')
   while start:
      try:
         cmd = input(f'''[{user}]@[{os.environ['COMPUTERNAME']}]:~$ ''')
         echo = cmd.split()
         if cmd == "qt":
            start = exit
         elif cmd == "help":
            help()
         elif echo[0] == '''echo''':
            line = ''''''
            for i in range(1, len(echo)):
               line += echo[i]
               line += ''' '''
            print(f'''{line}\n''')
         elif cmd == "cln":
            os.system('cls')
         elif cmd == "dt":
            print(f'''{dt.year}-{dt.month}-{dt.day}\n''')
         elif cmd == "time":
            print(f'''{dt.hour}-{dt.minute}-{dt.second}\n''')
         elif cmd == '''dfs''':
            fs.dfs()
         elif cmd == '''browser''':
            import browser
         elif cmd == '''net''':
            import net
            net.test('http://www.ya.ru')
         elif cmd == '''dfetch''':
            import dfetch
      except:
         pass
