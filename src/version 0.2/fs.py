# SPDX-License-Identifier: GPL-3.0 
'''*
   * diuz/version 0.1/explorer.py
   *
   * Copyright (C) 2022 Zotep 
   *
   * This file is the file system for the Diuz kernel
   *'''
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
    print("file remove (Partition name)/(file name) - remove file \n partition create (partition name) - create partition")
    while True:
        try:
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
            elif sa[0] == "back":
               print("\n")
               break
        except:
            pass
