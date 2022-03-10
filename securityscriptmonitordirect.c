#include <stdio.h>
#include <sys/inotify.h>
#include<unistd.h>
//LEN will be used to define the length of the buffer of data
#define LEN (sizeof (struct inotify_event)*16*1024)


//This program uses inotify header in C to monitor a certain direcotry for any changes
//This was more complciated to excute in Python, so this script was wiriten in C
int main(void) {
  int fd, 
  wd,
  infosize;
  //use inotify 
  fd = inotify_init ();
  //Watch /var/log
  wd = inotify_add_watch (fd, "/var/log", IN_MODIFY | IN_CREATE | IN_DELETE);
  //create buffer
  char buffer[LEN];

  //read in buffer of events (stored as structs but we don't care about the event info only count)
  infosize = read(fd,buffer,LEN);

  //if there are events this means changed have been made so print that a change has been detcted
  if (infosize>0){
    printf("Chnages have been detected to this directory\n")
  }
  
  return 0;
}
