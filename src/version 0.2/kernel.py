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
import psutil
from winreg import *
import ctypes

aReg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
aKey = OpenKey(aReg, r"HARDWARE\DESCRIPTION\System\CentralProcessor\0")
name = QueryValueEx(aKey, 'ProcessorNameString')[0]

def help():
   print(''''echo <line_text>' - for print your own line\n''')
   print(''''exit' - exit from system\n''')
   print(''''date' - show now date\n''')
   print(''''time' - show now time\n''')
   print(''''clear' - clear all terminal\n''')
   print(''''uexp' - open uni file system\n''')
   print(''''browser' - open browser\n''')
   print(''''net' - check network connection\n''')
dt = datetime.datetime.now()   

def main(start, exit, user):
   print('''\n''')
   while start:
      try:
         cmd = input(f'''[{user}]@[{os.environ['COMPUTERNAME']}]:~$ ''')
         echo = cmd.split()
         if cmd == '''exit''':
            start = exit
         elif cmd == '''help''':
            help()
         elif echo[0] == '''echo''':
            line = ''''''
            for i in range(1, len(echo)):
               line += echo[i]
               line += ''' '''
            print(f'''{line}\n''')
         elif cmd == '''clear''':
            os.system('cls')
         elif cmd == '''date''':
            print(f'''{dt.year}-{dt.month}-{dt.day}\n''')
         elif cmd == '''time''':
            print(f'''{dt.hour}-{dt.minute}-{dt.second}\n''')
         elif cmd == '''uexp''':
            fs.uExpRun()
         elif cmd == '''browser''':
            import browser
         elif cmd == '''net''':
            import net
            net.test('http://www.ya.ru')
         elif cmd == '''dfetch''':
            print('\t\tMain:')
            print('\t\t\tOS:\t\tDiuz alpha version')
            print('\t\t\tkernel:\t\tDiuz alpha version')
            print('\t\t\tGraphic:\t\tNone')
            print('\t\t\tLanguage:\t\tEnglish')
            print('\t\t\tPackages:\t\t0')
            print('\t\t\tDrivers:\t\t0')
            print('\t\tOther:')
            user32 = ctypes.windll.user32
            screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
            print(f'\t\t\tResolution:\t\t{screensize}')
            print(f'\t\t\tCPU name:\t\t{name}')
            print(f'\t\t\tCPU consumption(GHz):\t\t{psutil.cpu_percent()}')
            psutil.virtual_memory()
            dict(psutil.virtual_memory()._asdict())
            print(f'\t\t\tRAM consumption(%):\t\t{psutil.virtual_memory().percent}')
            print(f'\t\t\tCPU consumption(%):\t\t{psutil.virtual_memory().available * 100 / psutil.virtual_memory().total}')
            print('\t\t\tTerminal:\t\tTC (Terminal version: DEV1)')
            print(f"\t\t\tHostname PC:\t\t{os.environ['COMPUTERNAME']}")
      except:
         pass
