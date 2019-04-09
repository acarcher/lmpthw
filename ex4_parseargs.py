import sys
import argparse

settings = {"option1": "", "option2": "", "option3": ""}


def parse_args(arguments):

    # prev_arg_opt = False
    # pos_args = []

    # for arg in arguments[1:]:  # ignore script name
    #     if arg[:2] == "--":
    #         option = arg[2:]
    #         prev_arg_opt = True

    #     elif arg[0] == "-":
    #         prev_arg_opt = False
    #         flags = list(arg[1:])

    #         for flag in flags:
    #             handle_flag(flag)

    #     elif prev_arg_opt:
    #         pos_args.append(arg)
    #         print("positional: {}".format(arg))

    while(arguments):
        arg = arguments.pop(0)

        if arg[:2] == "--":
            opt_arg = arg[:2]
            is_opt = True
        elif arg[0] == "-":
            flags = list(arg[1:])
            handle_flags(flags)
        else:
            pass


def handle_flags(flags):

    for flag in flags:

        if flag == "h":
            print("""This is the help statement""")
        else:

            print("handle_flag: {}".format(flag))


def handle_option(option, value):
    print("option: {}".format(option))
    settings[option] = value


# determine the type of argument
#   flags:
#       * start with -
#       * no space between them
#       * don't take a value
#   options:
#       * start with --
#       * do take a value and set variable
#       * space between option and value
#   positional
#       * extension of options that takes multiple values
#
# support "help"
# given a list ... turn list into flag, opt, pos
# for loop over elements isn't great because of the positional arguments
# while(not empty)
#   if flag:
#       pop
#       handle
#   if opt:
#       pop
#       save state
#   if pos:
#       check state
#       pop/error

def use_arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", action="store_true", help="compress")
    parser.add_argument("-z", action="store_true", help="gzip")
    parser.add_argument("-v", action="store_true", help="verbosity")
    parser.add_argument("-f", help="folder")
    parser.add_argument("-x", action="store_true", help="extract")

    parser.add_argument("--opt1", nargs=1, help="option 1")
    parser.add_argument("--opt2", nargs=1, help="option 2")
    parser.add_argument("--opt3", nargs="*", help="option 3")

    args = vars(parser.parse_args())

    opt1 = args["opt1"]
    opt2 = args["opt2"]
    opt3 = args["opt3"]

    print("opt1: {}\nopt2: {}\nopt3: {}".format(opt1, opt2, opt3))


if __name__ == "__main__":
    for idx, arg in enumerate(sys.argv):
        print("arg {}: {}".format(idx, arg))

    # parse_args(sys.argv)
    use_arg_parse()
