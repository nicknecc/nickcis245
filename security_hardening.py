# Scipt written by N. Leung 3/9/2022
#This script creates a text file providing a variety of information about a linux server as descibed later iin this program
import datetime
import os

#Get current date and time for documentation purposes
dstring = datetime.datetime.now().strftime("%m/%d/%Y_%H:%M:%S")
#create a string for text file unique to when moniroting program is run
rds = " >> ServerMonitoring_" + dstring +".txt"

#All os.system commands write to the command line and are then written into the dated text file as described earlier

##Script Documentation written into txt file
fo = open("ServerMonitoring_" + dstring +".txt","w")
fo.write("Server Monitoring: "+dstring)
fo.write("\nThis script provides the following info in this order: \niostat\ncat /proc/meminfo\nmpstat\nps\npstree\nuptime\nfree\nvmstat\nss -t -a\nlsof\n")
fo.write("Note: Explanations of commands are provided in comments of scripts and or documentation\n")

#Note: To run this program sysstat must be installed
# Type: sudo apt install sysstat

#iostat is used to report CPU stats and I/O stats 
os.system("iostat" + rds)
#Disp info in meminfo file 
os.system("cat /proc/meminfo" + rds)
#Activites for each processor
os.system("mpstat" + rds)
#Show all current processes
os.system("ps" + rds)
#Show a processes tree
os.system("pstree" + rds)
#Disp how long server has been on and users
os.system("uptime" + rds)
#Disp total amount of free and used memory
os.system("free" + rds)
#Disp virtual memory stats
os.system("vmstat" + rds)
#network socket stats
os.system("ss -t -a" + rds)
#list of open files
os.system("lsof" + rds)
