# SPDX-License-Identifier: GPL-3.0 
'''*
   * diuz/version 0.1/boot.py
   *
   * Copyright (C) 2022 Zotep 
   *
   * This file is the bootloader for the Diuz kernel
   *'''
import kernel
import os.path
import time
from progress.bar import IncrementalBar

def text_to_bits(text, encoding = '''utf-8''', errors = '''surrogatepass'''):
    bits = bin(int.from_bytes(text.encode(encoding, errors), '''big'''))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))
def install():
   nameu = input('''\nYour own name: ''')
   passu = input('''Your own pass: ''')
   ynn = input('''Do you want to install an OS? [y/n]: ''')
   text_to_bits(nameu)
   text_to_bits(passu)

   if ynn == '''y''':
      with open('''user\\name.nu''', '''w''') as file:
         file.write(text_to_bits(nameu))
      with open('''user\\pass.pu''', '''w''') as file:
         file.write(text_to_bits(passu))

      bar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
      binarys = IncrementalBar('''binarys''', max = len(bar))
      for item in bar:
         binarys.next()
         time.sleep(1)
      binarys.finish()

      bar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
      explorer = IncrementalBar('''explorer''', max = len(bar))
      for item in bar:
         explorer.next()
         time.sleep(2)
      explorer.finish()

      bar = [1, 2, 3, 4, 5, 6]
      antivirus = IncrementalBar('''antivirus''', max = len(bar))
      for item in bar:
         antivirus.next()
         time.sleep(1.5)
      antivirus.finish()

      bar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13]
      ubrowser = IncrementalBar('''browser''', max = len(bar))
      for item in bar:
         ubrowser.next()
         time.sleep(0.3)
      ubrowser.finish()

      kernel.main(1, 0, nameu)
   elif ynn == '''n''':
      menu()

def menu():
   print('''\nWelcome to boot menu for Diuz kernel version 0.1\n''')
   print('''Boot menu:''')
   print('''[0] Live''')
   print('''[1] Install''')
   print('''[2] Continue''')
   print('''[3] Exit''')

   act = input('''[?]: ''')
   if act == '''0''':
      kernel.main(1, 0, '''live''')
   elif act == '''1''':
      if os.path.isfile('''user\\pass.pu''') == False or os.path.isfile('''user\\name.nu''') == False:
         install()
      else:
         print('''\nYou have already installed the OS''')
         menu()
   elif act == '''2''':
      if os.path.isfile('''user\\pass.pu''') == False or os.path.isfile('''user\\name.nu''') == False:
         print('''\nYou cannot continue because you have not installed the OS''')
         install()
      else:
         f = open('''user\\name.nu''')
         fd = f.read()
         f1 = open('''user\\pass.pu''')
         fd1 = f1.read()

         renameu = input('''\nRepeat your own name: ''')
         repassu = input('''Repeat your own pass: ''')
         text_to_bits(renameu)
         text_to_bits(repassu)
         while fd != text_to_bits(renameu) or fd1 != text_to_bits(repassu):
            renameu = input('''\nRepeat your own name: ''')
            repassu = input('''Repeat your own pass: ''')
         kernel.main(1, 0, renameu)
   else:
      exit()
menu()
