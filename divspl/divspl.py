#!/usr/bin/env python

import os

from parser import parser
from lexer import lexer


def main():
    import sys
    begin(sys.argv)


def begin(argv):
    if len(argv) > 1:
        with open(argv[1], 'r') as f:
            result = parser.parse(lexer.lex(f.read()))
            os.write(1, result.eval())
    else:
        os.write(1, "Please provide a filename.")

if __name__ == '__main__':
    main()
