import os
import time

#This is where to put the hodden file or root exe file path, directions on how to find this is porvided in the documentation
file = "/etc/users/"
#rds creates a string to move output to txt file
rds = " >> securityscriptmonitorfiles.txt"

#inf while loop, always montir  file
while True:
  #uses audit, which must be installed as descibed in documentation
  #this ausearch command will provide the time the file was chnaged and the user who changed in the form of a user id. If the text file has no user ids, this means there were no changes. 
  #This will check the files chnages fro the last 10 mins as rececnt means 10 mins
  os.system("ausearch --format --start recent --end now -f " + file + " -i" +rds)
  #run the program every 10 mins, so this allows for the file to be continiously monitored
  time.sleep(600)  
