#!/usr/bin/env python

import sys

from parser import parser
from lexer import lexer


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            result = parser.parse(lexer.lex(f.read()))
            sys.stdout.write(result.eval())
    else:
        sys.stdout.write("Please provide a filename.")
