import divspl


def entry_point(argv):
    divspl.begin(argv)
    return 0


def target(*args):
    return entry_point, None
