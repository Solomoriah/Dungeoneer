#!/usr/bin/env python
###############################################################################
#  _Treasure.py -- base functions for treasure generator
###############################################################################


import Dice

categories = {
    "Coin":     0,
    "Gem":      1,
    "Art":      2,
    "Magic":    3,
}

class Generic:
    pass

class Item:

    def __init__(self):

        self.value = 0.0
        self.name = ''
        self.desc = []
        self.fullcat = self.cat = 'Item'
        self.qty = 1

    def __cmp__(self, other):
        if str(self) < str(other):
            return -1
        if str(self) > str(other):
            return 1
        return 0

    def __str__(self):

        s = "%02d %-20s: %-30s " % (categories[self.cat], self.cat, self.name)

        if self.qty != 1:
            s = s + ("%10.2f" % float(self.qty))

        s = s + (" (%10.2f GP total)" % (float(self.value) * self.qty))

        return s

# end of script.
