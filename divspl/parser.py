from rply import ParserGenerator
from boxes import AssignmentBox, ProgramBox, RangeBox

pg = ParserGenerator(["ELLIPSIS", "EQUALS", "NUMBER", "WORD"])


@pg.production("main : range assignments")
def main(p):
    return ProgramBox(p[0], p[1])


@pg.production("assignments : assignments assignment")
@pg.production("assignments : ")
def expr_assignments(p):
    if p:
        return p[0] + [p[1]]
    return []


@pg.production("assignment : WORD EQUALS NUMBER")
def assignment_op(p):
    return AssignmentBox(p[0].value, int(p[2].value))


@pg.production("range : NUMBER ELLIPSIS NUMBER")
def range_op(p):
    return RangeBox(int(p[0].value), int(p[2].value))


parser = pg.build()
