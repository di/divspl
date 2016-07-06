from rply import ParserGenerator
from boxes import AssignmentBox, IntBox, ProgramBox, RangeBox, WordBox

pg = ParserGenerator(["ELLIPSIS", "ASSIGNMENT", "NUMBER", "WORD"])


@pg.production("main : range assignments")
def main(p):
    return ProgramBox(p[0], p[1])


@pg.production("range : num ELLIPSIS num")
def range_op(p):
    return RangeBox(p[0], p[2])


@pg.production("num : NUMBER")
def expr_number(p):
    return IntBox(int(p[0].value))


@pg.production("word : WORD")
def expr_word(p):
    return WordBox(p[0].value)


@pg.production("assignments : assignments assignment")
@pg.production("assignments : ")
def expr_assignments(p):
    if p:
        return p[0] + [p[1]]
    return []


@pg.production("assignment : word ASSIGNMENT num")
def assignment_op(p):
    return AssignmentBox(p[0], p[2])

parser = pg.build()
