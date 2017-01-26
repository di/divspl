#!/usr/bin/env python

import os

from divspl.parser import parser
from divspl.lexer import lexer


def main():
    import sys
    begin(sys.argv)


def begin(argv):

    def _bytes(x):
        if bytes == str:
            return bytes(x)
        else:
            return bytes(x, 'utf-8')

    if len(argv) > 1:
        with open(argv[1], 'r') as f:
            result = parser.parse(lexer.lex(f.read()))
            os.write(1, _bytes(result.eval()))
    else:
        os.write(1, _bytes("Please provide a filename."))


if __name__ == '__main__':
    main()
