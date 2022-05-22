# sudo chmod +x find_errors_in_fishy_log.py
#./find_errors_in_fishy_log.py fishy.log
# when prompted, enter 'CRON ERROR Failed to start'

#!/usr/bin/env python3
import sys
import os
import re

def error_search(log_file):
    error = input("What is the error? ")  # user input
    returned_errors = [] # matching logs that meet user specified criteria
    with open(log_file, mode='r',encoding='UTF-8') as file:  #open the file
        for log in file.readlines():  # read through the file line by line
            error_patterns = ["error"] # the errors that the user want to search for
            for i in range(len(error.split(' '))):
                error_patterns.append(r"{}".format(error.split(' ')[i].lower())) # the error search terms
            if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                returned_errors.append(log)
        file.close()
    return returned_errors
  
def file_output(returned_errors):
    with open(os.path.expanduser('~') + '/Documents/python/python_scripts/errors_found.log', 'w') as file: # we use the os.path.expanduser('~') which returns the home directory of my system instance
    	# then concatenate to the file for output
        for error in returned_errors:
            file.write(error)
        file.close()
if __name__ == "__main__":
    log_file = sys.argv[1]
    returned_errors = error_search(log_file)
    file_output(returned_errors)
    sys.exit(0)