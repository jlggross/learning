# Commands
> pwd
	- Current working directory
> ls 
	- List files inside the current folder
> ls -R -F
	- '-R' list files underneath a directory in recursive way
	- '-F' puts a '/' after a directory and a '*' after a runnable program
> cd
	- Change directory
> cd ~
	- Change to home folder
> cd ..
	- Change to the parent folder
> cp original.txt destination.txt
	- Copy file
> cp file1 file2 folder-Name
	- Copy files to the folder
> mv file1 file2 folder
	- Move files to folder
> mv filename newfilename
	- Rename file
> rm file
	- Reomve file 
> rmdir folder
	- Remove the folder
> mkdir folder
	- Creates a new folder
> history 
	- Show a list of commands recently used
> !command-name
	- Re-run the command in 'command-name' with its latest configurations
> wc filename
	- Word count
	- 'c' count number of characters
	- 'w' count number of words
	- 'l' count number of lines
> sort 
	- Order data. By default it does this in ascending alphabetical order
	- '-n' sort numerically 
	- '-r' sort in reverse order
	- '-b' tells it to ignore leading blanks
	- '-f' tells it to fold case (i.e., be case-insensitive)
> uniq
	- Remove duplicated lines
	- Works for sorted data
	- 'c' display unique lines with a count of how often each occurs

	
# View file content
> cat filename
	- Print file content
> less filename
	- Print file content
	- Type 'spacebar' to go to the next page, 'q' to quit
> less file1 file2 file3
	- Print file content
	- Type ':n' to go to the next file
	- Type ':p' to go to the previous file
	- Type ':q' to quit
> head filename
	- Print the first 10 lines of the file
> head -n 3 filename
	- Print the first 3 lines of the file
> tail filename
	- Print the last 10 lines of the file
	


> cut -f 2-5,8 -d , values.csv
	- Select columns 2 through 5 and columns 8, using comma as the 
	separator.
	- '-f' (meaning "fields") specify columns
	- '-d' (meaning "delimiter") specify the separator

> grep bicuspid seasonal/winter.csv
	- Prints lines from winter.csv that contain "bicuspid"
	- '-c' print a count of matching lines rather than the lines themselves
	- '-h' do not print the names of files when searching multiple files
	- '-i' ignore case (e.g., treat "Regression" and "regression" as matches)
	- '-l' print the names of files that contain matches, not the matches
	- '-n' print line numbers for matching lines
	- '-v' invert the match, i.e., only show lines that dont match 


# Output
> head -n 5 seasonal/summer.csv > top.csv
	- Create file top.csv with the output of the command head
> head -n 5 seasonal/summer.csv | tail -n 3
	- '-' is a pipe.
	- The pipe symbol tells the shell to use the output of the command on the
	left as the input to the command on the right.


# Wildcards
> *
	- Match zero or more characters
> ?
	- Matches a single character
	- 201?.txt will match 2017.txt or 2018.txt, but not 2017-01.txt.
> [...]
	- Matches any one of the characters inside the square brackets
	- 201[78].txt matches 2017.txt or 2018.txt, but not 2016.txt.
> {...}
	- Matches any of the comma-separated patterns inside the curly brackets
	- {*.txt, *.csv} matches any file whose name ends with .txt or .csv, but
	not files whose names end with .pdf.


# Shell variables
>  set
	- Show all shell variables
> echo $USER
	- Print the content of variable 'USER'
	-  '$' is used to access the variable content
> training=my_name
	- Creates variable 'training' with content 'my_name'


# Loops
> for filetype in gif jpg png; do echo $filetype; done
	- Produces:
		gif
		jpg
		png
> datasets=seasonal/*.csv
  for filename in $datasets; do echo $filename; done
	- Display all names inside 'datasets'
> for file in seasonal/*.csv; do head -n 2 $file | tail -n 1; done
	- Running many commands in a single loop
> for f in seasonal/*.csv; do echo $f; head -n 2 $f | tail -n 1; done
	- Running multiple commands using ';' to separeta them


# File Editor
> nano filename
	- Open filename for editing (or create it if it doesnt already exist)
	- Ctrl + K: delete a line.
	- Ctrl + U: un-delete a line.
	- Ctrl + O: save the file ('O' stands for 'output'). You will also need
	to press Enter to confirm the filename!
	- Ctrl + X: exit the editor.
	
# Scripts
> bash script.sh
	- Run script 'script.sh'

> special expression $@
	- dollar sign immediately followed by at-sign
	- all of the command-line parameters given to the script are substituted in the $@

	Example:
	
	script.sh : tail -q -n +2 $@ | wc -l
	command line : bash script.sh filename
	
	- 'filename' is substituted inside 'script.sh' where
	$@ is located
> special expression $n
	- $1 : first argument
	- $2 : second argument
	- $3 : third argument	

> script.sh
	- Looping a script
	
	# Print the first and last data records of each file.
	for filename in $@
	do
		cut -d , -f 1 $filename | grep -v Date | sort | head -n 1
		cut -d , -f 1 $filename | grep -v Date | sort | tail -n 1
	done
	
	
	
	
