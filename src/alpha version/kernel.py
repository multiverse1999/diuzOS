# SPDX-License-Identifier: GPL-3.0 
'''*
   * diuz/alpha version/boot.py
   *
   * Copyright (C) 2022 novem, HISEDOC, Zotep 
   *
   * This file is the big programm setup for the Diuz kernel
   *'''
import cmd
import os
import time
import sys
import psutil
from winreg import *
import ctypes

aReg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
aKey = OpenKey(aReg, r"HARDWARE\DESCRIPTION\System\CentralProcessor\0")
name = QueryValueEx(aKey, 'ProcessorNameString')[0]
def Disk(operation: str, disk: dict, args: dict):
    if operation == "FCREATE":
        disk[args["razdel"]]["file"] = {"1": args["desc"], "2": "FILE"}
    elif operation == "CONFCREATE":
        disk["reg"][args["param"]] = {"1": args["desc"], "2": "CONF"}
    elif operation == "RCREATE":
        disk[args["razdel"]] = {}
    elif operation == "FREMOVE":
        disk[args["razdel"]][args["file"]] = None
    elif operation == "DRESET":
        disk = {"C": {}, "reg": {}}
file_system = {"C": {}, "reg": {}}
def uExpRun():
    global file_system
    print("Help: \n file create (partition name)/(file) (content) - create file")
    print(" file remove (Partition name)/(file name) - remove file \n partition create (partition name) - create partition")
    print(f"Hello, {name}")
    while True:
        action = input(">> ")

        sa = action.split()
        if sa[0] == "file":

            if sa[1] == "create":
                ss = sa[2].replace("/", " ")
                ss = ss.split()
                Disk("FCREATE", file_system, {"file": ss[1], "razdel": ss[0], "desc": sa[3]})
                print(f"File {ss[1]} succesfully created! ")
            elif sa[1] == "remove":
                sa = sa[2].replace("/", " ")
                sa = sa.split()
                Disk("FREMOVE", file_system, {"file": sa[1], "razdel": sa[0]})
                print(f"File {sa[1]} succesfully removed! ")
        elif sa[0] == "partition":
            if sa[1] == "create":
                Disk("RCREATE", file_system, {"razdel": sa[2]})
                print("Partition created!")
pkg = [[],[]]


time.sleep(3)
print('Welcome to Diuz alpha version Setup!')
print('Copyright 2022 All rights reserved.')
time.sleep(3)
print('Loading...')
time.sleep(5)

print('\tInformation:')
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
time.sleep(3)
print('Loading...')
time.sleep(5)

input('Press to key "ENTER" to enter: ')
name = input('Name: ')
password = input('Password: ')
rename = input('Repeat name: ')
repassword = input('Repeat password: ')
while (name != rename or password != repassword):
    name = input('Name: ')
    password = input('Password: ')
    rename = input('Repeat name: ')
    repassword = input('Repeat password: ')
while True:
    try:
        command = input(f"[diuz]:[{os.environ['COMPUTERNAME']}]:[{name}]/ ")
        cmd_split = command.split()
        if cmd_split[0] == 'exit':
            break

        if cmd_split[0] == 'bitl':
            if cmd_split[1] == 'install':
                pkg_name = cmd_split[3]
                partition_of_pkg = cmd_split[2]
                pkg[0].append(pkg_name)
                pkg[1].append(file_system[partition_of_pkg][pkg_name]["1"])
                
                print(f"Succefully installed package {pkg_name} ({len(pkg[0])}th package)")
            elif cmd_split[1] == 'list':
                for i in range(len(pkg[0])):
                    print(f"[{i}] {pkg[0][i]}")
        elif cmd_split[0] == 'uexp':
            try:
                uExpRun()
            except:
                pass
        elif cmd_split[0] == "start_app":
            try:
                exec(pkg[1][int(cmd_split[1])])
            except:
                pass
    except:
        pass
    
    
    
        
        

            
