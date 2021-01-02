# Ubuntu Chops

- [index](#index)


---

## -> Networking

```bash
netstat -tunlp
ss -tunlp
```

```bash
nmcli
wget
curl
ping
ifconfig
```


difficults connecting to unsecured wifi networks with login pages

```bash
sudo service network-manager restart
ip route
systemd-resolve --status
iwconfig # check wifi speed
```

sometimes you can check the dns of a page if your phone connects to and then add it to you /etc/resolv.conf file ahead of 8.8.8.8 or your normal dns


---

## -> Command Line Tools

```bash
# tier 1
fzf --- fuzzy search in file directory
cloc -- count lines of code
ranger --- explorer / finder in 
ncdu --- shows size of all files sorted navigate with arrow keys

# tier 2
jq --- cli for editing json
inxi -Fxz  ---- show system profile, cpu, battery, hardware descriptions
```

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


## -> storage, disk space

```bash
fdisk
df
ds
ps
conky
```

---

## -> navigation

```
tree
tmux

```

---

## output

```
cat
head
tail
echo
```

---

## Config files

.bashrc, .bashprofile, .zsh, .profile

---

## Environment

```
env
```


---


## hibernation issues

```
systemctl hibernate
cd /sys/power
man busctl
lsblk
parted
cat /proc/swaps
cat /etc/fstab
fdisk -l
```

---

For ubuntu swapfiles, disk management, partitions, .rcfiles, navigation


---

## sections todo
move mv, copy cp, touch, remove rm, make directory mkdir

chown, permissions, octal rwx, drwxr-xr-x, chmod, chgrp

3rd party bootable usb creation
custom history

---

## index

*work in progress


- [useful cli utilies](#cliTOOLS)
- [network | wifi](#network)
- [packages | apt-get | ppa](#packages)
- [sound](#sound)

