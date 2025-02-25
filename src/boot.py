# SPDX-License-Identifier: BSD 3-Clause License
'''*
   * diuz/version 0.2/boot.py
   *
   * Copyright (C) 2022, multiverse1999
   *
   * this file is boot
   *'''
import kernel
import os.path
import time
from progress.bar import IncrementalBar

def text_to_bits(text, encoding = "utf-8", errors = "surrogatepass"):
    bits = bin(int.from_bytes(text.encode(encoding, errors), "big"))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))
  
def install():
   nameu = input("\nyour own name: ")
   passu = input("your own password: ")
   ynn = input("do you want to install a diuz os? [y/n]: ")
   text_to_bits(nameu)
   text_to_bits(passu)

   if ynn == "y":
      with open("name.nu", "w") as file:
         file.write(text_to_bits(nameu))
      with open("pass.pu", "w") as file:
         file.write(text_to_bits(passu))

      bar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
      binarys = IncrementalBar("installing libraries", max = len(bar))
      for item in bar:
         binarys.next()
         time.sleep(1)
      binarys.finish()

      bar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
      explorer = IncrementalBar("installing explorer", max = len(bar))
      for item in bar:
         explorer.next()
         time.sleep(2)
      explorer.finish()

      bar = [1, 2, 3, 4, 5, 6]
      antivirus = IncrementalBar("installing commands", max = len(bar))
      for item in bar:
         antivirus.next()
         time.sleep(1.5)
      antivirus.finish()

      bar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13]
      ubrowser = IncrementalBar("installing os", max = len(bar))
      for item in bar:
         ubrowser.next()
         time.sleep(0.3)
      ubrowser.finish()

      kernel.main(1, 0, nameu)
   elif ynn == "n":
      menu()

def menu():
   import fetch
   fetch.dfetch()
   print("\nwelcome to boot menu for diuz os version 0.2\n")
   print("boot menu:")
   print("[0] live")
   print("[1] install")
   print("[2] continue")
   print("[3] exit")

   act = input("[]: ")
   if act == "0":
      kernel.help()
      kernel.main(1, 0, "live")
   elif act == "1":
      if os.path.isfile("pass.pu") == False or os.path.isfile("name.nu") == False:
         install()
         kernel.help()
      else:
         print("\nyou have already installed the diuz os")
         menu()
   elif act == "2":
      if os.path.isfile("pass.pu") == False or os.path.isfile("name.nu") == False:
         print("\nyou cannot continue because you have not installed the diuz os")
         install()
         kernel.help()
      else:
         f = open("name.nu")
         fd = f.read()
         f1 = open("pass.pu")
         fd1 = f1.read()
        
         renameu = input("\nrepeat your own name: ")
         repassu = input("repeat your own password: ")
         text_to_bits(renameu)
         text_to_bits(repassu)
         while fd != text_to_bits(renameu) or fd1 != text_to_bits(repassu):
            renameu = input("\nrepeat your own name: ")
            repassu = input("repeat your own password: ")
         kernel.help()
         kernel.main(1, 0, renameu)
   else:
      exit()
menu()
