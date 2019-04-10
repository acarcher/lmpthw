# find
# (req) arg 1: directory
# (opt) arg 2: filter arguments -name -type
# (opt) arg 3: -print -exec

import argparse
import os
import glob
import subprocess

if __name__ == "__main__":
    ap = argparse.ArgumentParser()

    ap.add_argument("directory", nargs=1, help="directory to search")

    ap.add_argument("--name", nargs=1, help="file name")
    ap.add_argument("--type", nargs=1, help="file type")

    ap.add_argument("--print", action="store_true", help="print full file name")
    ap.add_argument("--exec", nargs="*", help="print full file name")

    args = vars(ap.parse_args())

    for dirpath, dirnames, filenames in os.walk(args["directory"][0]):

        print(dirpath)

        for file in filenames:
            print(os.path.join(dirpath, file))

    # for entry in glob.glob(".*", recursive=True):
    #     print(entry)

    # dir_and_file = str(args["directory"] + args["name"])

    # print(glob.glob(dir_and_file))
