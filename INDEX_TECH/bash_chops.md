find . -name "*.bak" -type f -delete   === recursively delete all files of a single extension

find $directory -type f -name "*.in" --> recursive print all file with extension .py



find ./ -name '*article*' | xargs -I '{}' mv {} ../backup

find ./ -name '*article*' | xargs mv -t ../backup


//  show list of all http port connections active, use sudo with lsof to include system connections
netstat -ap tcp || grep -i “listen”
lsof -PiTCP -sTCP:LISTEN

// make http request and trace out what happens on the way
curl 
—verbose 
—trace-ascii debugdumplog.txt   
-o redirect output
URL = uniform resource locator. ref - RFC 3986


// show disk files on machine
df


ls -lG :: prints modified col output

stat

// shows information about the current processes running in shell
ps -Eafx::

PS1="\e[0;32m\h \W\:~ \e[m "  —> PS1 is the environment variable that contains the shell prompt. '\e[0;31m' is the terminal escape sequence to change color to red. '\u' is the user name, '\h' is the host name, '\W' is the current working directory and '\e[m' means "return to the default text color"

PS1="\e[0;33mjaja@ny-vid;~ \e[m "  ——> yellow

————NAVIGATING FILES AND DIRECTORIES————

PS1=‘{what the prompt should be}’ ex - $

whoami  —> display current username (also in title bar)

pwd  —> present working directory
\ —> home directory

ls
	-F adds / trailing to folders
	man ls  —> gives all available options
	-l long list print format

man pages -> b or spacebar to skip full page

———————WORKING WITH FILES AND DIRECTORIES————

mkdir {name} —> makes a directory with a name
	tips: don’t use whitespaces
		don’t begin with - {commands treat that as an option
		stay with letters numbers and .,-,_

nano {file.whatever} —> text only file editor
	tip: the ^ i control key

rm —> deletes file stands for remove
	doesn’t work on directory, only files
	-i interactive flag, asks if we really want to delete said file
	shell has no trash bin, things are gone

mv{old location/file} {new location/file}  —> rename move file 
	stands for move
	works on directories and files
	ex mv {dir/file} .  —> move file into current dir

cp {file} {dir/file}  —> copies files to said dir

——— PIPES AND FILTERS ———————

*  —> wildcard operator, any length string  for in a file name
	ex wc *.txt   (wc all text files in current  directory)

? —>  wildcard for single character

wc  —> word count
	dip lays word -c, line -l, character -m, bytes -w

>   —> redirect shells output to a file instead of printing in the screen
	creates or entirely overwrites file

cat {file}  —> prints file to screen
	concatenate - stands for
	always dump entire file onto screen

less {file}   —> prints screenful of file
	spacebar for next string

sort -n {file}  —> 

head -n {how many} {file}  —> prints selected num of lines to output

{command1} | {command on output of command 1}   ——> pipe
	both commands run simultaneously

tail -n {num} {file}  ——> print last num of lines in output

file name {*[ab].*}   ——> prints files with a or b in that position

command >> {file name}   ——> adds output to files
	> this rewrites the file

uniq {file}   —> removes adjacent duplicated lines

cut   —>  removes portions of lines from a file

boolean  ! not; && AND; || OR

only integers 16 bit, 32 bit after 2.05

** exponentiation

% modulo

w   —> prints current user and what they are doing

———————— LOOPS———————————

for {line} in {file1} {file2}
do
	ex. head -n 3 $line
done
	— this shows the first three lines in file1, followed by file2
	$line makes it reference the variable

;   —> will separate two lines in terminal prompt

for {x} in {*.filetype};  do blah;  done
	————> starts by expanding *.filetype

echo {text for anything to output}  ——> prints to output

if there is whitespace in a filename put “” marks around it

to rerun command from history {!histnum}

!!   ———> last run command

!$  ————> run last word of previous command

——————	SHELL SCRIPTS —————

bash {script.sh} {input 1= $1}….

comment in the beginning of a script to advise what 

———————  FINDING THINGS  ———————————————

grep {word or “phrase a”} {filename}  —> 
	-w flag word
	-n line number
	-i case insensitive
	-v lines that do not contain search parameter
	^ in “phrase” anchors to start of line
	. in “phrase” is single char wildcard

find .  —> displays all files in current directories substructure
	. means in the pwd

which {python}  —>   show address of version in use

exec bash  —> restart shell

printenv ——> show all env variables

tr string1 string2  ——> replace string one with string 
2

