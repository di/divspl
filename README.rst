divspl (Dustin Ingram's Very Special Programming Language)
==========================================================

An implementation of a FizzBuzz DSL using `rply <https://github.com/alex/rply>`_.

Installation
============

::

    pip install divspl

Usage
=====

::

    divspl [filename]

Where::

    filename            A *.divspl filename to execute

Example
=======

Use the interpreter to execute valid DIVSPL code:

::

    divspl fizzbuzz.divspl

Or use it as a shebang:

::

    #!env/bin/divspl
    1...15
    fizz=3
    buzz=5

Then:

::

    ./fizzbuzz.divspl

Description
===========

`divspl` is an interpreter for the DIVSPL DSL (Dustin Ingram's Very Special
Programming Language Domain Specific Language), which is used for implementing
FizzBuzz-like programs.

Contact
=======

:On PyPI:
    http://pypi.python.org/pypi/divspl/

:Souce:
    https://github.com/di/divspl

:Issues:
    https://github.com/di/divspl/issues
