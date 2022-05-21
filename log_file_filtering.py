#!/usr/bin/env python3

import sys
import re

logfile = sys.argv[1]

with open(logfile) as f: # returns a file object that can be acted upon
    for line in f:
    	if "INFO" not in line: # filter out only logs with this in the line
    		continue
    	pattern = r'\d{4}\w*\d{6} .*)'
    	print(line.strip())