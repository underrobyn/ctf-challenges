#!/bin/bash

# Generate random passwords
jimmy_password=$(openssl rand -base64 12)
serveradmin_password=$(openssl rand -base64 12)

# Create the users
useradd jimmy --create-home -s /bin/bash
useradd serveradmin --create-home -s /bin/bash

# Set the passwords for the users
echo "jimmy:$jimmy_password" | chpasswd
echo "serveradmin:$serveradmin_password" | chpasswd

# Allow sarah to su to serveradmin
echo "user ALL=(serveradmin) /bin/su" >> /etc/sudoers

# Set up permissions for serveradmin
echo "serveradmin ALL=(ALL) NOPASSWD: /usr/bin/passwd [a-z]*" >> /etc/sudoers
echo "serveradmin ALL=(ALL) NOPASSWD: /usr/bin/apt-get" >> /etc/sudoers
echo "serveradmin ALL=(ALL) NOPASSWD: /usr/bin/systemctl" >> /etc/sudoers
echo "serveradmin ALL=(ALL) NOPASSWD: /usr/bin/netstat" >> /etc/sudoers
echo "serveradmin ALL=(ALL) NOPASSWD: /usr/bin/htop" >> /etc/sudoers

# Create jimmy's files
mkdir -p /home/jimmy/folder1
touch /home/jimmy/{flag.txt,file1.txt,file2.txt,folder1/{file3.txt,file4.txt}}

# Create serveradmin's files
mkdir -p /home/serveradmin/{backups,config,logs}
touch /home/serveradmin/{backups/{backup1.tar.gz,backup2.tar.gz,backup3.tar.gz},config/{config1.conf,config2.conf,config3.conf},logs/{log1.txt,log2.txt,log3.txt}}

