from rply.token import BaseBox


class ProgramBox(BaseBox):
    def __init__(self, range_box, assignment_boxes):
        self.range_box = range_box
        self.assignment_boxes = assignment_boxes

    def eval(self):
        return "\n".join(
            "".join(assignment.eval(i) for assignment in self.assignment_boxes) or str(i)
            for i in self.range_box.eval()
        ) + "\n"


class AssignmentBox(BaseBox):
    def __init__(self, word, number):
        self.word = word
        self.number = number

    def eval(self, i):
        if not i % int(self.number):
            return self.word
        return ''


class RangeBox(BaseBox):
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def eval(self):
        return range(self.low, self.high + 1)
