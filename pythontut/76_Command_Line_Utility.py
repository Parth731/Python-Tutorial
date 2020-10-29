
'''

command line interface article:
https://en.wikipedia.org/wiki/Command-line_interface

falty calculator exercise using command line utility 
'''


import argparse
import sys

def calc(args):
    if args.o == "add":
        return args.x + args.y

    elif args.o == "mul":
        return args.x * args.y

    elif args.o == "sub":
        return args.x - args.y

    elif args.o == "div":
        return args.x / args.y

    else:
        return "some went wrong"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x',
                        type=float,
                        default=1.0,
                        help="Enter the First Number."
                             "This is a utility for "
                             "calculation. please contact harry"
                             "bhai")

    parser.add_argument('--y',
                        type=float,
                        default=3.0,
                        help="Enter the second Number. "
                             "This is a utility for "
                             "calculation. please contact harry"
                             "bhai")

    parser.add_argument('--o',
                        type=str,
                        default="add",
                        help= "This is a utility for "
                             "calculation. please contact harry"
                             "bhai for more")


    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))

    # calc() function converted to string then
    # stdout printed to console
