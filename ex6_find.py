# find
# (req) arg 1: directory
# (opt) arg 2: filter arguments -name -type
# (opt) arg 3: -print -exec

import argparse
import os
import glob
import subprocess


def parse_args():
    ap = argparse.ArgumentParser()

    ap.add_argument("directory", nargs=1, help="directory to search")

    ap.add_argument("--name", nargs=1, help="file name")
    ap.add_argument("--type", nargs=1, help="file type")

    ap.add_argument("--print", action="store_true", help="print full file name")
    ap.add_argument("--exec", nargs="*", help="print full file name")

    return vars(ap.parse_args())


def walk_dir(directory):
    results = []

    for dirpath, _, filenames in os.walk(directory):
        results.append(dirpath)

        for file in filenames:
            results.append(os.path.join(dirpath, file))

    return results


if __name__ == "__main__":

    args = parse_args()

    contents = walk_dir(args["directory"][0])

    for result in contents:
        print(result)

    # for entry in glob.glob(".*", recursive=True):
    #     print(entry)

    # dir_and_file = str(args["directory"] + args["name"])

    # print(glob.glob(dir_and_file))