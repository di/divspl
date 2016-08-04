from rply.token import BaseBox


class MainBox(BaseBox):
    def __init__(self, range_box, assignments):
        self.range_box = range_box
        self.assignments = assignments

    def eval(self):
        lines = []
        for i in self.range_box.range():
            line = ""
            for assignment in self.assignments.list():
                line += assignment.eval_with(i)
            lines.append(line or str(i))
        return "\n".join(lines) + "\n"


class AssignmentBox(BaseBox):
    def __init__(self, word, number):
        self.word = word
        self.number = number

    def eval_with(self, i):
        if not i % self.number.int():
            return self.word.str()
        return ''


class AssignmentsBox(BaseBox):
    def __init__(self, assignments=None, assignment=None):
        self.assignments = assignments
        self.assignment = assignment

    def list(self):
        if self.assignments:
            return self.assignments.list() + [self.assignment]
        return []


class RangeBox(BaseBox):
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def range(self):
        return range(self.low.int(), self.high.int() + 1)


class IntBox(BaseBox):
    def __init__(self, value):
        self.value = int(value.getstr())

    def int(self):
        return self.value


class WordBox(BaseBox):
    def __init__(self, value):
        self.value = value.getstr()

    def str(self):
        return self.value
