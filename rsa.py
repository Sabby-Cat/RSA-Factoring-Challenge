#!/usr/bin/python3
from sys import argv
"""defines a function"""


# fn unpack number factorial
def fc():
    """func to search file to nr and format n=p*q"""
    try:
        with open(argv[1]) as file:
            for nr in file:
                nr = int(nr)
                if nr % 2 == 0:
                        print("{}={}*{}".format(nr, nr // 2, 2))
                        continue
                p = 3
                while p < nr // 2:
                    if nr % p == 0:
                        print("{}={}*{}".format(nr, nr // p, p))
                        break
                    p = p + 2
                if p == (nr // 2) + 1:
                    print("{}={}*{}".format(nr, nr, 1))
    except (IndexError):
        pass

# autostart
fc()