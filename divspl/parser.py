from rply import ParserGenerator
from boxes import (
    AssignmentBox, AssignmentsBox, MainBox, RangeBox, IntBox, WordBox
)

pg = ParserGenerator(["ELLIPSIS", "EQUALS", "NUMBER", "WORD"])


@pg.production("main : range assignments")
def main(p):
    return MainBox(p[0], p[1])


@pg.production("assignments : assignments assignment")
def expr_assignments(p):
    return AssignmentsBox(p[0], p[1])


@pg.production("assignments : ")
def expr_empty_assignments(p):
    return AssignmentsBox()


@pg.production("assignment : word EQUALS number")
def assignment_op(p):
    return AssignmentBox(p[0], p[2])


@pg.production("range : number ELLIPSIS number")
def range_op(p):
    return RangeBox(p[0], p[2])


@pg.production("number : NUMBER")
def number(p):
    return IntBox(p[0])


@pg.production("word : WORD")
def word(p):
    return WordBox(p[0])


parser = pg.build()
