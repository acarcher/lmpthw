# grep
# get cmd line args
# load the file
# read the file into a list
# iterate through the list searching for pattern
#


import argparse
import re


def parse_args():
    ap = argparse.ArgumentParser()

    ap.add_argument("pattern", type=str, help="pattern to search for")

    ap.add_argument("file", type=str, help="file to search in")

    ap.add_argument("-i", action="store_true", help="make case insensitive")
    ap.add_argument("-n", action="store_true", help="")

    # ap.add_argument("-r", action="store_true", help="")

    return ap.parse_args()


def grep(args):

    result = []

    pattern = args.pattern
    file = args.file

    with open(file) as f:
        listified = f.readlines()

    for line in listified:
        if args.i:
            if re.search(pattern, line, flags=re.I):
                result.append(line)
        else:
            if re.search(pattern, line):
                result.append(line)

    for line in result:
        print(line.rstrip())


args = parse_args()
grep(args)
