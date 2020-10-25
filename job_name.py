import os
import sys

build_num = int(os.environ['BUILD_NUMBER'])
devsion = 3
modulo = build_num%devsion
if modulo > 0:
	print ("is not a multiple of 3")
	sys.exit(1)
else:
	print ("Job Name is" + ' ' + os.environ['JOB_NAME'])




