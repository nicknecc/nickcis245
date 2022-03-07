import datetime
import time
import os

#Log ins between the hours of 12 am and 5am are considered potentially suspicious because "the company" is not open
begin = datetime.time(0,0,0)
end = datetime.time(5,0,0)

#IP/MAC addresses for sepcific users that are considered suspicious are listed here (Examples only in this array as suspicion would be added from IT admin discrestion)
badip = ["192.168.0.0","10.0.0.0"]

#Used for first iteration, lines0/lines00 represents what lines are already in flagged file
lines0 = []
lines00=[]

#Array to remove formatting 
badformat = ["Interface", "Format"]

#while loop to run between 12am and 5 am
while datetime.datetime.now().time() <= end and datetime.datetime.now().time() >= begin:
  #arp command to find all IPs on LAN and store in txt file
  os.system("arp.exe -a >> securityone.txt")
  #open file where arp info temp stored
  fo = open("securityone.txt","w")
  #read in all lines into array
  lines = fo.readlines()
  #open file with red flag IPs
  fo2 = open("flaggedip.txt", "w")
  #For loop to write in flagged IPs
  for l in lines:
    #Stop repition of lines and fix formatting
    if l not in lines0 and badformat not in l:
      fo2.write(l)
  lines0 = fo2.readines()
  #clear out temp file
  fo.truncate(0)
  #Repeat only every 10 mins
  time.sleep(600)

#Inf while loop to contiuous check throughout all hours
while True:
    #arp command to find all IPs on LAN and store in another txt file
  os.system("arp.exe -a >> securityone1.txt")
  #open file where arp info temp stored
  fo3 = open("securityone1.txt","w")
  #read in all lines into array
  lines1 = fo3.readlines()
  #open file with red flag IPs
  fo2 = open("flaggedip.txt", "w")

  #iterate through all IPs 
  for l1 in lines1:
    #to avoid double coutning and fix format
    if l1 not in lines00 and badformat not in l1:
      #record if in flagged IPs
      if badip in lines1:
        fo2.write(l1)
  #For double coutning formatting 
  lines00 = fo2.readines()
  #clear out temp file
  fo3.truncate(0)
  #Only run every 20 mins
  time.sleep(1200)
