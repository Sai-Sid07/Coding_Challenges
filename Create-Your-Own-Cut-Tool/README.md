# Build Your Own cut Tool
This challenge is to build your own version of the Unix command line tool cut!

The functional requirements for wc are concisely described by it’s man page - give it a go in your local terminal now:

``man cut``

The TL/DR version is: cut - cuts out the selected portions from each line in a file.

#### Link : https://codingchallenges.fyi/challenges/challenge-cut

## cut tool
The cut command in linux is a command for cutting out the sections from each line of files and writing the result to standard output. It can be used to cut parts of a line by byte position, character, and field. The cut command slices a line and extracts the text. It is necessary to specify an option with a command otherwise it gives an error. If more than one file name is provided then data from each file is not preceded by its file name. 

### Usage:

 - `python3 cut.py [-f] [-d] [filename]`
 - `cat [Text] | python3 cut.py [-f] [-d]`

### Example:
 - `python3 cut.py -f1,2 sample.tsx`
 - `python3 cut.py -f"1,2" -d, fourchords.csv`
 - `head -n5 fourchords.csv | python3 cut.py -d, -f"1 2"`

### Tip:
Create a bash alias cccut or ccut = python3 cut.py to make this tool even more authentic. 
