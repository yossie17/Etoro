import os
import sys


def isMultipleof3(n): 
	
	while ( n > 0 ): 
		n = n - 3

	if ( n == 0 ): 
		return 1

	return 0
	
i = int(os.environ['BUILD_NUMBER'])
if ( isMultipleof3(i) == 1 ): 
	print ("Job Name is" + ' ' + os.environ['JOB_NAME']) 
	
else: 
	print (i, "is not a multiple of 3") 
	sys.exit(1)

