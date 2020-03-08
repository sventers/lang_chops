# ubuntu terminal notes

- [useful cli utilies](#cliTOOLS)
- [network | wifi](#network)
- [packages | apt-get | ppa](#packages)
- [sound](#sound)

---

## -> cliTOOLS

- fzf --- fuzzy search in file directory
- cloc -- count lines of code
- ranger --- explorer / finder in 
- ncdu --- shows size of all files sorted navigate with arrow keys
- jq --- cli for editing json

---

## -> Packages

```bash
type PACKAGE   #shows install path
apt-cache policy PACKAGE
apt-get    #
ppa-purge
aptitude
```

---

## -> Network Management

difficults connecting to unsecured wifi networks with login pages

    sudo service network-manager restart
    ip route
    systemd-resolve --status

    iwconfig # check wifi speed

sometimes you can check the dns of a page if your phone connects to and then add it to you /etc/resolv.conf file ahead of 8.8.8.8 or your normal dns

---

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

## loops

for
while
if

## regex

[a-z]_
[0-9]_
^
.\*

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
