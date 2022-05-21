#!/usr/bin/env python3

import sys
logfile = sys.argv[1]

with open(logfile) as f: # returns a file object that can be acted upon
    for line in f:
    	if "INFO" not in line: # filter out only logs with this in the line
    		continue
    	print(line.strip())