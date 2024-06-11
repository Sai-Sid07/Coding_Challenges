import sys
import argparse
import csv  

def get_digits(arg: list) -> list:
    if arg == []:
        return []
    arg_f = list(filter(lambda arg: arg.isnumeric(), arg)) 
    return arg_f

def extract_data(filename: str, delimiter: str="\t") -> list:
    all_rows = []
    with open(file=filename, mode="r") as tsv:
        rd = csv.reader(tsv, delimiter=delimiter, quotechar='"')
        all_rows.extend(list(rd))
    return all_rows

parser = argparse.ArgumentParser(
                    prog='Create your own Cut Tool - python',
                    description='Python implementation of the Linux Command Cut. This is a part of Coding Challenge #4 by John Cricket',
                    epilog='''
                        Example : cat test.txt | python ccwc.py -l
                        python ccwc.py text.txt -l -w

                        Tip - You can create an alias cccut or ccut (custom cut).
                        ccut=python3 cut.py
                    '''
                    )

parser.add_argument("-f", type=str, help="fields to be cut. List either separated by comma or enclosed in " " with space.")
parser.add_argument("-d", type=str, help="custom delimited. Default is tab")
parser.add_argument("filename" , nargs="?")

args = parser.parse_args()

if __name__ == "__main__":
    file = args.filename

    delimiter = "\t"

    if args.d:
        delimiter = args.d

    data = []
    if file is not None:
        data = extract_data(filename=file, delimiter=delimiter)
    else:
        for line in sys.stdin:
            parts = line.strip().split(',')
            data.append(parts)

    field_number = str(len(data))

    if args.f:
        field_number = args.f

    f_argument = field_number.split(" ") if " " in field_number else field_number.split(",")
    split_0 = list(f_argument[0])
    split_1 = [] if len(f_argument) == 1 else list(f_argument[1:])
    row_0 = ''.join(get_digits(split_0))
    row_0 = (int)(row_0)
    row_xs = list(map(int, split_1))
    rows = [row_0] + row_xs
    cut_row = []

    for row in rows:
        elements = []
        for line in data:
            elements.append(line[row - 1])
        cut_row.append(elements)
    
    length = len(cut_row)
    for (index, _) in enumerate(cut_row[0]):
        for i in range(len(cut_row)):
            print(cut_row[i][index], end="\t")
        print()