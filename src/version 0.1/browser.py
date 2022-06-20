# SPDX-License-Identifier: GPL-3.0 
'''*
   * diuz/version 0.1/kernel.py
   *
   * Copyright (C) 2022 Zotep 
   *
   * This file is the browser Diuz kernel
   *'''
import webbrowser

print(''''link <line_url>' open url in browser''')

start = 1
while start:
	try:
		search = input('''Search: ''')
		searchst = search.split()
		if searchst[0] == '''link''':
			ln = ''''''
			for i in range(1, len(searchst)):
				ln += searchst[i]
				ln += ''' '''
			webbrowser.open(ln)
		elif searchst[0] == '''back''':
			print('''\n''')
			start = 0
	except:
	    pass 