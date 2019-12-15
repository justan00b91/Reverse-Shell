# Reverse Shell Using Python

* ## Requirements:
  Install python on both systems using following command:
  ```bash
  $ sudo apt-get install python3
  ```
  
* ## Usage:
   On Attacker machine:
   
  ```bash
  python attacker.py
   ____                                   ____  _          _ _    
  |  _ \ _____   _____ _ __ ___  ___     / ___|| |__   ___| | |   
  | |_) / _ \ \ / / _ \ '__/ __|/ _ \____\___ \| '_ \ / _ \ | |   
  |  _ <  __/\ V /  __/ |  \__ \  __/_____|__) | | | |  __/ | |_  
  |_| \_\___| \_/ \___|_|  |___/\___|    |____/|_| |_|\___|_|_(_)

  Connected to xxx.xxx.xxx.xxx@hostname
  $ ++++Execute your commands here.++++
  ```
  
   On Victim Machine:
   
  ```bash
  python victim.py
  ```
 
 * ## Description:
  The "victim.py" file, when executed togather, create a
  reverse shell  on the victim's machine and connects 
  it to the attacker machine  who has access to all
  the data on the victim's machine via commandline.
  The attacker is required to be on the same network as
  the victim and  change the ip address of the
  server with his/her own's.
  
  
