# Ubuntu 20.04 cheat sheet

## Graphics card issue

If you have issues with the display ports, it is an UBUNTU driver issue.
To solve it, follow the instructions on: https://www.murhabazi.com/install-nvidia-driver

This consists of:
  - sudo apt-get purge nvidia-*
  - sudo apt install nvidia-driver-(xxx)  (mine is nvidia-driver-470 )

  
  
## open window from terminal

 - xdg-open


## Linux CHMOD In general

 - r = 4
 - w = 2
 - x = 1

 chmod Owner, group, rest
 
 ## List and mounted disk
 
  - Command `lsblk` list all the disks
  - mkdir /media/my_disk
  - sudo mount -t ext4 /dev/MY_DISK_DEVICE /media/my_disk
  -  # Add this line to /etc/fstab 
  -  /dev/MY_DISK_DEVICE       /media/my_disk ext4    defaults        0       0

## Check which process is using a particular port

netstat -nlp|grep :5000

## Kill screen session

First, list the sessions with `screen -ls`

Then, kill it by id with `screen -XS [ID] quit`

