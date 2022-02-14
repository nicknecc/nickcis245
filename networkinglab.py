import os
import time

#open file to output w ith wiring privlage
fo = open("networkingoutput.txt","w")
#redirect to file string for writing CL to file
rds = " >> networkingoutput.txt"


#Display IP info
fo.write("Information listed in this text file\n\nIP information\n\n")
os.system("ip link show")
os.system("ip link show" + rds)
fo.write("\n\n")
os.system("ifconfig")
os.system("ifconfig" + rds)
fo.write("\n\n")

#Display DNS info
fo.write("DNS information\n\n")
os.system("dig")
os.system("dig" + rds)
fo.write("\n\n")

#Display Open Port Info
fo.write("OnenPort information\n\n")
os.system("netstat -tulpn")
os.system("netstat -tulpn" + rds)
fo.write("\n\n")

#Ping test
fo.write("Ping test (google.com)\n\n")
os.system("ping -c 5 google.com")
os.system("ping -c 5 google.com"+rds)
fo.write("\n\n")

#Routing table
fo.write("Routing Table\n\n")
os.system("route -n")
os.system("route -n"+rds)
fo.write("\n\n")
