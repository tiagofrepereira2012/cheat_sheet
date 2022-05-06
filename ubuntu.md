# Ubuntu 20.04 cheat sheet

## Graphics card issue

If you have issues with the display ports, it is an UBUNTU driver issue.
To solve it, follow the instructions on: https://www.murhabazi.com/install-nvidia-driver

This consists of:
  - sudo apt-get purge nvidia-*
  - sudo apt install nvidia-driver-(xxx)  (mine is nvidia-driver-470 )

  
  
# open window from terminal

 - xdg-open


# Linux CHMOD In general

 - r = 4
 - w = 2
 - x = 1

 chmod Owner, group, rest
