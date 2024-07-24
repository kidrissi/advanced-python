import random


def big_tab(rn, rint):
    tab = []
    for i in range(rn):
        tab.append(random.randint(1, rint))
    return tab