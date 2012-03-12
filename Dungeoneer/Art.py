#!/usr/bin/env python
###############################################################################
#  Art.py -- generate object of art
###############################################################################

import Dice
import _Treasure

_art_types_table = [
    (6, "Anklet"),
    (6, "Belt"),
    (2, "Bowl"),
    (7, "Bracelet"),
    (6, "Brooch"),
    (5, "Buckle"),
    (5, "Chain"),
    (3, "Choker"),
    (5, "Clasp"),
    (2, "Circlet"),
    (4, "Comb"),
    (1, "Crown"),
    (3, "Cup"),
    (7, "Earring"),
    (3, "Flagon"),
    (3, "Goblet"),
    (5, "Knife"),
    (4, "Letter Opener"),
    (3, "Medal"),
    (7, "Necklace"),
    (1, "Plate"),
    (5, "Pin"),
    (1, "Sceptre"),
    (3, "Statuette"),
    (1, "Tiara"),
]

class Art(_Treasure.Item):
    def __init__(self):
        _Treasure.Item.__init__(self)
        self.cat = "Art"
        self.fullcat = self.fullcat + "." + self.cat
        row = Dice.Roll(_art_types_table)
        self.name = self.shortname = row[1]
        self.value = float(Dice.D(2, 8, 0) * 100)

if __name__ == '__main__':
    print Art()

# end of file.
