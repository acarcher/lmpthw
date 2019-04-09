# cat

# TODO:
# get files through command line
# read file
# write to stdout (print)
# implement options

# options:
# -n: number all output lines
# -b: number non-blank output lines

# -s: squeeze multiple adjacent blank lines

# -v: displays nonprinting characters, except for tabs and the end of line character
# -t: implies -v, but also display tabs as ^I
# -e: implies -v but also display end-of-line characters as $

import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="*", help="file to cat")

    parser.add_argument("-n", action="store_true", help="number all output lines")
    parser.add_argument("-b", action="store_true", help="number non-blank output lines")

    parser.add_argument("-s", help="squeeze multiple adjacent blank lines")

    parser.add_argument("-v", action="store_true", help="displays nonprinting characters, except for tabs and the end of line character")
    parser.add_argument("-t", action="store_true", help="implies -v, but also display tabs as ^I")
    parser.add_argument("-e", action="store_true", help="implies -v but also display end-of-line characters as $")

    args = vars(parser.parse_args())

    output = ""

    for file in args["files"]:
        with open(file) as f:
            data = f.read()
            # print(data)
            output += data

    if args["n"] is True:
        for idx, line in enumerate(output.splitlines()):
            print("{} {}".format(idx + 1, line))

    elif args["b"] is True:
        # for idx, line in enumerate([output = output.splitlines() if output != "\n"]):
        #     print("{} {}".format(idx + 1, line))
        pass




    # print(output)
