
import argparse
import commands


def main():
    """Main entrypoint of the cli."""
    # print("Main from cli is running")

    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='command')

    # build add command
    add = subparser.add_parser(commands.ADD)
    add.add_argument("numbers", nargs="+", type=int)

    # build subtract command
    sub = subparser.add_parser(commands.SUB)
    sub.add_argument("numbers", nargs="+", type=int)

    # build multiply command
    multi = subparser.add_parser(commands.MULTI)
    multi.add_argument("numbers", nargs="+", type=int)

    # build divide command
    div = subparser.add_parser(commands.DIV)
    div.add_argument("numbers", nargs="+", type=int)

    # test argument
    # argument is required.
    # parser.add_argument('test')
    # -- makes it optional.
    # parser.add_argument('--test')

    args = parser.parse_args()
    # print(args)
    if args.command == commands.ADD:
        result = sum(args.numbers)
        print(f"The sum of {args.numbers} is {result}.")
    elif args.command == commands.SUB:
        # split off the first item from the list and
        # then the balance into a seperate list
        first, *rest = args.numbers
        result = first - sum(rest)
        print(f"The difference of {args.numbers} is {result}.")
    elif args.command == commands.MULTI:
        # multiply the values in the list.
        result = 1
        # use a for statement to cycle through all elements in args.numbers
        for x in args.numbers:
            result = result * x
        print(f"The product of {args.numbers} is {result}.")
    elif args.command == commands.DIV:
        # divide all numbers in the list
        first, *rest = args.numbers
        result = 1
        # set a controlling flag for the first pass through
        run_once = 0
        for x in rest:
            if run_once == 0:
                result = first / x
                run_once = 1
            else:
                result = result / x
        print(f"The quotient of {args.numbers} is {result}.")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
