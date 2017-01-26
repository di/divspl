from divspl import main


def entry_point(argv):
    main.begin(argv)
    return 0


def target(*args):
    return entry_point, None
