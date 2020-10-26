# Etoro exercise
 
## In order to complete the task i did the following:
 
- Install Jenkins server on the Windows server
- Install requirements (Git, Python, etc).
- writing a simple python script that check if the Build number divided by 3
 (if not, the script will exit(1)).

 
 
### I created 3 Jenkins Jobs:
#### the first job call to the second job, the second job call to the third job.
 
- the first job - pull the project from Github
- the second job - run the python script and succeed only if build num divided by 3 (retry 3 times)
- the third job - print the first job name and build number

## Jenkins server:
Jenkins server run on localhost port 80.

user:admin  
password: will send on mail





