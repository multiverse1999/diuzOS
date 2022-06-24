# SPDX-License-Identifier: GPL-3.0 
'''*
   * diuz/version 0.1/kernel.py
   *
   * Copyright (C) 2022 Zotep 
   *
   * This file is the console Diuz kernel
   *'''
import os
import datetime
import fs

def help():
   print(''''echo <line_text>' for print your own line\n''')
   print(''''exit' exit from system\n''')
   print(''''date' show now date\n''')
   print(''''time' show now time\n''')
   print(''''clear' clear all terminal\n''')
   print(''''uexp' open uni file system\n''')
   print(''''browser' open browser\n''')

dt = datetime.datetime.now()   

def main(start, exit, user):
   print('''\n''')
   while start:
      try:
         cmd = input(f'''{user}> ''')
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
         elif cmd == '''net_''':
            import virus_net
      except:
         pass
