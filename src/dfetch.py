import os
import psutil
from winreg import *
import ctypes

aReg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
aKey = OpenKey(aReg, r"HARDWARE\DESCRIPTION\System\CentralProcessor\0")
name = QueryValueEx(aKey, 'ProcessorNameString')[0]

print('''                                      
`7MM"""Yb. `7MMF'`7MMF'   `7MF'MMM"""AMV 
  MM    `Yb. MM    MM       M  M'   AMV  
  MM     `Mb MM    MM       M  '   AMV   
  MM      MM MM    MM       M     AMV    
  MM     ,MP MM    MM       M    AMV   , 
  MM    ,dP' MM    YM.     ,M   AMV   ,M 
.JMMmmmdP' .JMML.   `bmmmmd"'  AMVmmmmMM
''')

print('\t\tMain:')
print('\t\t\tOS:\t\tDiuz 0.2 version')
print('\t\t\tkernel:\t\tDiuz 0.2 version')
print('\t\t\tGraphic:\t\tCLI')
print('\t\t\tLanguage:\t\tEnglish')

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
