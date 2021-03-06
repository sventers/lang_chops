# Bash Snippets

*links to sections on this page*

- [search grep find](#searchgrepfind)
- [networking/admin](#networking)
- [basic advice](#basicadvice)
- [filesystem](#filesystem)
- [pipes](#pipes)
- [loops](#loops)
- [scripts](#scripts)
- [customizing](#customizing)

*outlinks*

- [good cheatsheat 1](#https://github.com/LeCoupa/awesome-cheatsheets/blob/master/languages/bash.sh)

---

## -> Searching 

{ grep find sed }

```bash
# look through current directory's hieracrhy for text in file
grep -rnw '/path/to/somewhere/' -e 'pattern'

# recursively delete all files of a single extension
find . -name "*.bak" -type f -delete

# recursive print all file with extension .py
find $directory -type f -name "*.in" 

#
find ./ -name '*article*' | xargs -I '{}' mv {} ../backup

#
find ./ -name '*article*' | xargs mv -t ../backup
```

operators
```bash
A; B    # Run A and then B, regardless of success of A
A && B  # Run B if and only if A succeeded
A || B  # Run B if and only if A failed
A &     # Run A in background.

*  # wildcard for array of chars
?  # wildcard for single char
>  # redirect shell output to file appends
>> # redirect shell output to file overwrites
!  # boolean NOT 
&& # boolean AND 
|| # boolean OR
** # exponentiation
%  # modulo
;  # separate lines in terminal prompt
```

---

## -> Networking



```bash
# show list of all http port connections active, use sudo with lsof to include system connections
netstat -ap tcp || grep -i “listen”
lsof -PiTCP -sTCP:LISTEN

# make an http request and trace out what happens on the way

curl 
	-verbose 
	-trace-ascii debugdumplog.txt   
	-o redirect output
	URL = 
```

---

## -> Regex

```
[a-z]_
[0-9]_
^
.\*
```

---


```bash
# show address of version in use
which {package}

# restart shell
exec bash

# show all env variables
printenv

#run command from history
!histnum

# change shell zsh bash etc
chsh -s 
```
---

## -> Filesystem

```bash
# show disk files on machine
df

# what is present working directory
pwd

# prints modified col output
ls -lG

# lots of good stuff
stat --help

# shows information about the current processes running in shell
ps -Eafx::
```

---

## -> Customizing

```bash
# PS1 is the environment variable that contains the shell prompt. 

# '\e[0;31m' is the terminal escape sequence to change color to red. # '\u' is the user name
# '\h' is the host name
# '\W' is the current working directory
# '\e[m' means "return to the default text color"

PS1="\e[0;32m\h \W\:~ \e[m "  

#to yellow
PS1="\e[0;33mjaja@ny-vid;~ \e[m "

PS1=‘{what the prompt should be}’ ex - $

# display user name
whoami

chmod



# makes a directory with a name
mkdir {name}

# move files to new directory
mv
```
---

## -> Pipes

```bash
# word count

wc
dip lays word -c, line -l, character -m, bytes -w
cat 
less
sort -n
head -n {how many} {file}
tail -n {num} {file}
file name {*[ab].*}   ——> prints files with a or b in that position
uniq {file}   —> removes adjacent duplicated lines
cut   —>  removes portions of lines from a file
w   —> prints current user and what they are doing

# wc all text files in current  directory
wc *.txt
```
---

## -> Loops

need to review that

```bash
# starts by expanding *.filetype
for {x} in {*.filetype};  do blah;  done ;

# prints to output
echo {text for anything to output}

!!   ———> last run command

!$  ————> run last word of previous command
```

---

## -> Scripts

```bash
bash {script.sh} {$inputvar1}
```
