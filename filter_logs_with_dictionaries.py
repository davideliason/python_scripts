import os
import re
import sys

logfile = sys.argv[1]
usernames = {}
with open(logfile) as f:
	for line in f:
		pattern = r'(^[A-Z]\w*) ([A-Z]\w*)'
		result = re.search(pattern, line)
		if result is None:
			continue
		first_name = result[1]
		last_name = result[2]
		usernames[last_name] = usernames.get(last_name,0) +1
		usernames[first_name] = usernames.get(first_name,0) +1
print(usernames)