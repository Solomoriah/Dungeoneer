# Basic Fantasy RPG Dungeoneer Suite
# Copyright 2007-2024 Chris Gonnerman
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
#  Art.py -- generate object of art
###############################################################################

from . import Dice, _Treasure


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
    print(Art())


# end of file.
