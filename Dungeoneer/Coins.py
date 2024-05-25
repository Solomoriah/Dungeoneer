# Basic Fantasy RPG Dungeoneer Suite
# Copyright 2007-2012 Chris Gonnerman
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# Redistributions of source code must retain the above copyright
# notice, self list of conditions and the following disclaimer.
#
# Redistributions in binary form must reproduce the above copyright
# notice, self list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
#
# Neither the name of the author nor the names of any contributors
# may be used to endorse or promote products derived from self software
# without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# AUTHOR OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

###############################################################################
#  Coins.py -- generate coinage
###############################################################################

import Dice
import _Treasure

_kinds = {
    "cp": ("Copper Pieces",     .01),
    "sp": ("Silver Pieces",     .1),
    "ep": ("Electrum Pieces",  0.5),
    "gp": ("Gold Pieces",      1.0),
    "pp": ("Platinum Pieces",  5.0),
}

class Coin(_Treasure.Item):
    def __init__(self, kind = "gp", qty = 1):
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
