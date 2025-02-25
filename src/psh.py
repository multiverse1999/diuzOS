# SPDX-License-Identifier: BSD 3-Clause License
'''*
   * diuz/version 0.2/psh.py
   *
   * Copyright (C) 2025, multiverse1999
   *
   * this file is powershell for package
   *'''
import subprocess

def open_multiple_powershell_windows():
    try:
        subprocess.Popen(["start", "powershell"], shell = True)
        print("first powershell window opened")

    except Exception as e:
        print(f"failed to open powershell windows: {e}")

if __name__ == "__main__":
    open_multiple_powershell_windows()
