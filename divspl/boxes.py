from rply.token import BaseBox


class MainBox(BaseBox):
    def __init__(self, range_box, assignments):
        self.range_box = range_box
        self.assignments = assignments

    def eval(self):
        lines = []
        for i in self.range_box.getrange():
            line = ""
            for assignment in self.assignments.getlist():
                line += assignment.eval_with(i)
            lines.append(line or str(i))
        return "\n".join(lines) + "\n"


class AssignmentBox(BaseBox):
    def __init__(self, word, number):
        self.word = word
        self.number = number

    def eval_with(self, i):
        if not i % self.number.getint():
            return self.word.getstr()
        return ''


class AssignmentsBox(BaseBox):
    def __init__(self, assignments=None, assignment=None):
        self.assignments = assignments
        self.assignment = assignment

    def getlist(self):
        if self.assignments:
            return self.assignments.getlist() + [self.assignment]
        return []


class RangeBox(BaseBox):
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def getrange(self):
        return range(self.low.getint(), self.high.getint() + 1)


class IntBox(BaseBox):
    def __init__(self, value):
        self.value = value

    def getint(self):
        return int(self.value.getstr())


class WordBox(BaseBox):
    def __init__(self, value):
        self.value = value

    def getstr(self):
        return self.value.getstr()
