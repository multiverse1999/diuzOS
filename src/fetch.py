import os
import psutil
from winreg import *
import ctypes

reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
key = OpenKey(reg, r"HARDWARE\DESCRIPTION\System\CentralProcessor\0")
name = QueryValueEx(key, 'ProcessorNameString')[0]

print('''                                      
`7MM"""Yb. `7MMF'`7MMF'   `7MF'MMM"""AMV 
  MM    `Yb. MM    MM       M  M'   AMV  
  MM     `Mb MM    MM       M  '   AMV   
  MM      MM MM    MM       M     AMV    
  MM     ,MP MM    MM       M    AMV   , 
  MM    ,dP' MM    YM.     ,M   AMV   ,M 
.JMMmmmdP' .JMML.   `bmmmmd"'  AMVmmmmMM
''')

print('main:')
print('\tos:\t\tdiuz 0.6 version')
print('\tkernel:\t\tdiuz 0.1 version')
print('\tgraphic:\t\tcli')
print('\tlanguage:\t\tenglish')

print('other:')
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
print(f'\tresolution:\t\t{screensize}')
print(f'\tcpu name:\t\t{name}')
print(f'\tcpu consumption(ghz):\t\t{psutil.cpu_percent()}')
psutil.virtual_memory()
dict(psutil.virtual_memory()._asdict())
print(f'\tram consumption(%):\t\t{psutil.virtual_memory().percent}')
print(f'\tcpu consumption(%):\t\t{psutil.virtual_memory().available * 100 / psutil.virtual_memory().total}')
print('\tterminal:\t\tdt 0.2 version')
print(f"\thostname pc:\t\t{os.environ['COMPUTERNAME']}")
