import sys
import os
from typing import Optional, IO
import argparse


def get_bytes(data:Optional[str]="", file_path:Optional[str]="") -> int:
    if file_path != "":
        return os.path.getsize(file)
    
    assert data != ""

    data = "\n".join(data)

    return len(data.encode('utf-8'))

def get_lines(data:Optional[str]="", file_ptr:Optional[IO]=None) -> int:
    if file_ptr is not None:
        lines = 0
        for _ in file_ptr:
            lines += 1
        return lines

    return len(data)

def get_words(data:Optional[str]="", file_ptr:Optional[IO]=None) -> int:
    words = 0
    if file_ptr is not None:
        for line in file_ptr:
            word = line.rstrip("\n").split(" ")
            words += len(word)
        return words

    for line in data:
        words += len(line.split())
    return words

def get_characters(data:Optional[str]="", file_ptr:Optional[IO]=None) -> int:
    chars = 0
    if file_ptr is not None:
        for line in file_ptr:
            chars += len(line)
        return chars
    
    for line in data:
        chars += len(line)
    return chars


parser = argparse.ArgumentParser(
                    prog='Create your own WC - python',
                    description='Python implementation of the Linux Command WC. This is a part of Coding Challenge #1 by John Cricket',
                    epilog='''
                        Example : cat test.txt | python ccwc.py -l
                        python ccwc.py text.txt -l -w

                        Tip - You can create an alias ccwc or cwc (custom wc).
                        ccwc=python3 wc.py
                    '''
                    )

parser.add_argument("-l", "--lines", action="store_true", help="number of lines")
parser.add_argument("-c", "--count", action="store_true", help="number of bytes")
parser.add_argument("-w", "--words", action="store_true", help="number of words")
parser.add_argument("-m", "--chars", action="store_true", help="number of characters")
parser.add_argument("filename" , nargs="?")

args = parser.parse_args()


if __name__ == "__main__":

    output = ""

    if not (args.count or args.lines or args.words or args.chars):
        args.count = True
        args.lines = True
        args.words = True

    file = args.filename

    if file is not None:
        try:
            with open(file=file, mode="r", encoding="utf8") as file_ptr:
                if args.count:
                    output += str(get_bytes(file_path=file))
                    output += " "
                
                if args.lines:
                    file_ptr.seek(0)
                    output += str(get_lines(file_ptr=file_ptr))
                    output += " "
                
                if args.words:
                    file_ptr.seek(0)
                    output += str(get_words(file_ptr=file_ptr))
                    output += " "
                
                if args.chars:
                    file_ptr.seek(0)
                    output += str(get_characters(file_ptr=file_ptr))
                    output += " "
                
            output += (file + "\n")

            sys.stdout.write(output)
            sys.exit(0)
        except FileNotFoundError:
            output += f"file {file} not found.\n"
            sys.stdout.write(output)
            sys.exit(0)
    
    else:
        data = sys.stdin.readlines()
        data = "".join(data)

        if args.count:
            output += str(get_bytes(data=data))
            output += " "
        
        if args.lines:
            output += str(get_lines(data=data))
            output += " "
        
        if args.words:
            output += str(get_words(data=data))
            output += " "
        
        if args.chars:
            output += str(get_characters(data=data))
            output += " "

        output += "\n"

        sys.stdout.write(output)
        sys.exit(0)