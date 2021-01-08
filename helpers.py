
def get_classes(file):
    """ return a list from .txt file """
    f = open(file, "r")
    classes = []
    for x in f.readlines():
        classes.append(x[:-1])
    return classes