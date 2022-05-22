#!/usr/bin/env python3

import sys
import re

logfile = sys.argv[1]
num =0

with open(logfile) as f: # returns a file object that can be acted upon
    for line in f:
    	if "INFO" not in line: # filter out only logs with this in the line
    		continue
    	pattern = r'terminating$'
    	result = re.search(pattern,line)
    	if result == None:
    		continue
    	else:
    		print('Here is a result: {} time:{}'.format(result,num))
    		num+=1
    		print(num)