import os


def isMultipleof3(n): 
	
	while ( n > 0 ): 
		n = n - 3

	if ( n == 0 ): 
		return 1

	return 0
	
i = int(os.environ['NUM'])
if ( isMultipleof3(i) == 1 ): 
	print (i, "is multiple of 3" + ' ' + os.environ['JOB']) and exit(0)
	
else: 
	print (i, "is not a multiple of 3") and exit(1)