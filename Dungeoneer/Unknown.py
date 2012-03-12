#!/usr/bin/env python
###############################################################################
#  Unknown.py -- handle unknown treasure types
###############################################################################

import Dice
import _Treasure

class Unknown(_Treasure.Item):
    def __init__(self, typ = None):
        _Treasure.Item.__init__(self)
        self.cat = "Unknown"
        self.fullcat = self.fullcat + "." + self.cat
        self.qty = 1
        self.shortname = typ
        self.name = typ
        self.value = 0

    def __str__(self):
        return self.name


if __name__ == '__main__':
    print Unknown()

# end of file.
