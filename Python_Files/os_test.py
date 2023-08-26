import platform as pt


def check():
    if (pt.system() == 'Linux'):
        return 1
    if (pt.system() == 'Windows'):
        return 0
    else:
        return 99