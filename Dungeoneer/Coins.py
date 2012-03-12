#!/usr/bin/env python
###############################################################################
#  Coins.py -- generate coinage
###############################################################################

import Dice
import _Treasure

_kinds = {
    "CP": ("Copper Pieces",     .01),
    "SP": ("Silver Pieces",     .1),
    "EP": ("Electrum Pieces",  0.5),
    "GP": ("Gold Pieces",      1.0),
    "PP": ("Platinum Pieces",  5.0),
}

class Coin(_Treasure.Item):
    def __init__(self, kind = "GP", qty = 1):
        _Treasure.Item.__init__(self)
        self.cat = "Coin"
        self.fullcat = self.fullcat + "." + self.cat
        self.qty = int(qty)
        self.shortname = kind 
        self.name = _kinds[kind][0]
        self.value = _kinds[kind][1]

    def __str__(self):

        name = "%6.2f %s" % (self.value, self.name)

        s = "%02d %-20s: %-30s " % (_Treasure.categories[self.cat], self.cat, name)

        if self.qty != 1:
            s = s + ("%10.2f" % float(self.qty))

        s = s + (" (%10.2f GP total)" % (float(self.value) * self.qty))

        return s

if __name__ == '__main__':
    print Coin()

# end of file.
