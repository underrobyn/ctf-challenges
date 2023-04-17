#!/bin/bash

# Generate random passwords
jimmy_password=$(openssl rand -base64 12)
serveradmin_password=$(openssl rand -base64 12)

# Create the users
useradd jimmy --create-home -s /bin/bash
useradd michael --create-home -s /bin/bash
useradd kevin --create-home -s /bin/bash
useradd joseph --create-home -s /bin/bash
useradd rachel --create-home -s /bin/bash
useradd kelly --create-home -s /bin/bash
useradd lauren --create-home -s /bin/bash
useradd cronuser --create-home -s /bin/bash
useradd lizzy --create-home -s /bin/bash
useradd brian --create-home -s /bin/bash
useradd serveradmin --create-home -s /bin/bash

# Set the passwords for the users
echo "jimmy:$jimmy_password" | chpasswd
echo "serveradmin:$serveradmin_password" | chpasswd

# Allow all users to see their server permissions
echo "ALL ALL=(ALL) NOPASSWD:/usr/bin/sudo -l" >> /etc/sudoers

# Allow user to su to serveradmin
echo "user ALL=(ALL) NOPASSWD:/usr/bin/su serveradmin" >> /etc/sudoers

# Set up permissions for serveradmin
echo "# serveradmin ALL=(ALL) NOPASSWD: /usr/bin/passwd [a-z]*" >> /etc/sudoers
echo "serveradmin ALL=(ALL) NOPASSWD: /usr/bin/systemctl" >> /etc/sudoers
echo "serveradmin ALL=(ALL) NOPASSWD: /usr/bin/netstat" >> /etc/sudoers
echo "serveradmin ALL=(ALL) NOPASSWD: /usr/bin/htop" >> /etc/sudoers
echo "serveradmin ALL=(ALL) NOPASSWD: /usr/sbin/visudo" >> /etc/sudoers

# Create jimmy's files
mkdir -p /home/jimmy/folder1
touch /home/jimmy/{file1.txt,file2.txt,folder1/{file3.txt,file4.txt}}

echo "printf \"Hey there Jimmy! \n Welcome back to \$(hostname) \n Hope you're having a clamtastic day!\" | cowsay" >> /home/jimmy/.bashrc
echo "alias ls=\"sl\"" >> /home/jimmy/.bashrc

echo "export PROMPT_COMMAND=\"cd\"" >> /home/jimmy/.bashrc

echo -e "\n# Custom shortcuts" >> ~/.bashrc
echo "alias gs='git status'" >> ~/.bashrc
echo "alias ga='git add'" >> ~/.bashrc
echo "alias gc='git commit'" >> ~/.bashrc
echo "alias gco='git checkout'" >> ~/.bashrc
echo "alias gb='git branch'" >> ~/.bashrc
echo "alias gl='git log'" >> ~/.bashrc
echo "export PS1='\u@\h:\w\ > '" >> ~/.bashrc

# Create serveradmin's files
mkdir -p /home/serveradmin/{backups,config,logs}
touch /home/serveradmin/{backups/{backup1.tar.gz,backup2.tar.gz,backup3.tar.gz},config/{config1.conf,config2.conf,config3.conf},logs/{log1.txt,log2.txt,log3.txt}}

