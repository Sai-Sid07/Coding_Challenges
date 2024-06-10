# Build Your Own wc Tool
This challenge is to build your own version of the Unix command line tool wc!

The functional requirements for wc are concisely described by it’s man page - give it a go in your local terminal now:

``man wc``

The TL/DR version is: wc – word, line, character, and byte count.

#### Link : https://codingchallenges.fyi/challenges/challenge-wc

## wc tool
The wc tool in Linux is a command-line utility for counting the number of lines, words, and bytes in a file. It can also be used to count the number of characters in a file. The wc tool is a very useful tool for text processing and can be used in a variety of ways.

### Usage:

 - `python3 wc.py [-h] [-l] [-c] [-w] [-m] [filename]`
 - `cat [Text] | python3 wc.py[-h] [-l] [-c] [-w] [-m]`

### Example:
 - `python3 wc.py text.txt -c -w`
 - `cat test.txt | python wc.py -w`

### Tip:
Create a bash alias ccwc or cwc = python3 wc.py to make your tool even more authentic. 