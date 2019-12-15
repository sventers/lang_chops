# ubuntu terminal notes
This contains stuff for efficiency or system level common fuck ups correction

## -> filesystem exploring / navigation

ranger - vim keys navigating filesystem
ncdu - shows size of all files sorted navigate with arrow keys

## -> network management

ip route
systemd-resolve --status

sometimes you can check the dns of a page if your phone connects to and then add it to you /etc/resolv.conf file ahead of 8.8.8.8 or your normal dns

## -> for package management

```bash
type PACKAGE   #shows install path
apt-cache policy PACKAGE     #
```

sudo service network-manager restart

## -> storage, disk space

fdisk
df
ds
ps
conky

## -> networking

nmcli
wget
curl
ping
ifconfig

## -> navigation

tree

## output

cat
head
tail
echo

## environment, .bashrc, .bashprofile, .zsh

env

## grep, find, awk, sed

grep
find
awk
sed
locate

## loops

for
while
if

## regex

[a-z]*
[0-9]*
^
.*

## pipes

|

## tmux

## hibernation issues

systemctl hibernate
cd /sys/power
man busctl
lsblk
parted
cat /proc/swaps
cat /etc/fstab
fdisk -l

## 3rd party bootable usb creation

## custom history

history

## python installation management pip, pip3, virtualenv, conda

pip3 --user

## node, npm, npx

npm
npx

## For ubuntu swapfiles, disk management, partitions, .rcfiles, navigation

apt-get
apt
sudo

## docker, docker-compose

## move mv, copy cp, touch, remove rm, make directory mkdir

## chown, permissions, octal rwx, drwxr-xr-x, chmod, chgrp
