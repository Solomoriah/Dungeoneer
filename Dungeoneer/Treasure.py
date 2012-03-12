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
#  Treasure.py -- generate treasures for Basic Fantasy RPG
###############################################################################

import Gems, Art, Coins, Magic, Unknown
import Dice
import string

def combine(lst):
    lst.sort()
    hits = 1
    while hits:
        hits = 0
        for i in range(len(lst) - 1):
            if lst[i] is not None and lst[i+1] is not None:
                if lst[i].cat == lst[i+1].cat \
                and lst[i].name == lst[i+1].name \
                and lst[i].value == lst[i+1].value:
                    lst[i].qty += lst[i+1].qty
                    lst[i+1] = None
                    hits += 1
        if hits:
            lst = filter(lambda x: x is not None, lst)
    return lst

def _gen_coins(argtup):
    kind, n, s, b, mul = argtup
    return [ Coins.Coin(kind, (Dice.D(n, s, b) * mul)) ]

def _gen_gems(argtup):
    n, s, b, mul = argtup
    lst = []
    qty = Dice.D(n, s, b) * mul
    for i in range(qty):
        lst = lst + [ Gems.Gem() ]
    return lst

def _gen_art(argtup):
    n, s, b, mul = argtup
    lst = []
    qty = Dice.D(n, s, b) * mul
    for i in range(qty):
        lst = lst + [ Art.Art() ]
    return lst

def __gen_magic(argtup):
    kind, n, s, b, mul = argtup
    lst = []
    qty = Dice.D(n, s, b) * mul
    for i in range(qty):
        lst = lst + [ Magic.Magic(kind) ]
    return lst

def _gen_magic(argtup):
    if type(argtup) is type([]):
        lst = []
        for i in argtup:
            lst = lst + __gen_magic(i)
        return lst
    else:
        return __gen_magic(argtup)

_treasure_table = {

    # lair treasure

    'A': [
            (50, _gen_coins, ("CP", 5,  6, 0, 100)),
            (60, _gen_coins, ("SP",  5, 6, 0, 100)),
            (40, _gen_coins, ("EP", 5,  4, 0, 100)),
            (70, _gen_coins, ("GP", 10,  6, 0, 100)),
            (50, _gen_coins, ("PP",  1,  10, 0, 100)),
            (50, _gen_gems,  (6, 6, 0, 1)),
            (50, _gen_art,   (6, 6, 0, 1)),
            (30, _gen_magic, ("Any", 0, 0, 3, 1)),
         ],
    'B': [
            (75, _gen_coins, ("CP", 5,  10, 0,  100)),
            (50, _gen_coins, ("SP", 5,  6, 0,  100)),
            (50, _gen_coins, ("EP",  5, 4, 0,  100)),
            (50, _gen_coins, ("GP",  3, 6, 0,  100)),
            (25, _gen_gems,  (1, 6, 0, 1)),
            (25, _gen_art,   (1, 6, 0, 1)),
            (10, _gen_magic, ("AW", 0, 0, 1, 1)),
         ],
    'C': [
            (60, _gen_coins, ("CP", 6, 6, 0,  100)),
            (60, _gen_coins, ("SP", 5,  4, 0,  100)),
            (30, _gen_coins, ("EP",  2,  6, 0,  100)),
            (25, _gen_gems,  (1, 4, 0, 1)),
            (25, _gen_art,   (1, 4, 0, 1)),
            (15, _gen_magic, ("Any", 1, 2, 0, 1)),
         ],
    'D': [
            (30, _gen_coins, ("CP", 4, 6, 0,  100)),
            (45, _gen_coins, ("SP", 6, 6, 0,  100)),
            (90, _gen_coins, ("GP", 5, 8, 0,  100)),
            (30, _gen_gems,  (1, 8, 0, 1)),
            (30, _gen_art,   (1, 8, 0, 1)),
            (20, _gen_magic, [
                    ("Any",    1, 2, 0, 1),
                    ("Potion", 0, 0, 1, 1),
                ]
            ),
         ],
    'E': [
            (30, _gen_coins, ("CP",  2,  8, 0,  100)),
            (60, _gen_coins, ("SP",  6, 10, 0,  100)),
            (50, _gen_coins, ("EP",  3,  8, 0,  100)),
            (50, _gen_coins, ("GP",  4, 10, 0,  100)),
            (10, _gen_gems,  (1, 10, 0, 1)),
            (10, _gen_art,   (1, 10, 0, 1)),
            (30, _gen_magic, [
                    ("Any",    1, 4, 0, 1),
                    ("Scroll", 0, 0, 1, 1),
                ]
            ),
         ],
    'F': [
            (40, _gen_coins, ("SP",  3,  8, 0, 100)),
            (50, _gen_coins, ("EP",  4,  8, 0, 100)),
            (85, _gen_coins, ("GP",  6, 10, 0, 100)),
            (70, _gen_coins, ("PP",  2,  8, 0, 100)),
            (20, _gen_gems,  (2, 12, 0, 1)),
            (20, _gen_art,   (1, 12, 0, 1)),
            (35, _gen_magic, [
                    ("Non-Weapon", 1, 4, 0, 1),
                    ("Scroll", 0, 0, 1, 1),
                    ("Potion", 0, 0, 1, 1),
                ]
            ),
         ],
    'G': [
            (90, _gen_coins, ("GP",  4, 6, 0, 1000)),
            (75, _gen_coins, ("PP",  5, 8, 0,  100)),
            (25, _gen_gems,  (3,  6, 0, 1)),
            (25, _gen_art,   (1, 10, 0, 1)),
            (50, _gen_magic, [
                    ("Any",    1, 4, 0, 1),
                    ("Scroll", 0, 0, 1, 1),
                ]
            ),
         ],
    'H': [
            (75, _gen_coins, ("CP",  8, 10, 0,  100)),
            (75, _gen_coins, ("SP",  6, 10, 0, 1000)),
            (75, _gen_coins, ("EP",  3, 10, 0, 1000)),
            (75, _gen_coins, ("GP",  5,  8, 0, 1000)),
            (75, _gen_coins, ("PP",  9,  8, 0,  100)),
            (50, _gen_gems,  ( 1, 100, 0, 1)),
            (50, _gen_art,   (10,   4, 0, 1)),
            (20, _gen_magic, [
                    ("Any",    1, 4, 0, 1),
                    ("Scroll", 0, 0, 1, 1),
                    ("Potion", 0, 0, 1, 1),
                ]
            ),
         ],
    'I': [
            (80, _gen_coins, ("PP", 3, 10, 0, 100)),
            (50, _gen_gems,  (2, 6, 0, 1)),
            (50, _gen_art,   (2, 6, 0, 1)),
            (15, _gen_magic, ("Any", 0, 0, 1, 1)),
         ],
    'J': [
            (45, _gen_coins, ("CP", 3,  8, 0, 100)),
            (45, _gen_coins, ("SP", 1,  8, 0, 100)),
         ],
    'K': [
            (90, _gen_coins, ("CP", 2, 10, 0, 100)),
            (35, _gen_coins, ("SP", 1,  8, 0, 100)),
         ],
    'L': [
            (50, _gen_gems,  (1, 4, 0, 1)),
         ],
    'M': [
            (90, _gen_coins, ("GP", 4, 10, 0,  100)),
            (90, _gen_coins, ("PP", 2,  8, 0, 1000)),
         ],
    'N': [
            (40, _gen_magic, ("Potion", 2, 4, 0, 1)),
         ],
    'O': [
            (50, _gen_magic, ("Scroll", 1, 4, 0, 1)),
         ],

    # personal treasure

    'P': [
            (100, _gen_coins, ("CP", 3, 8, 0, 1)),
         ],
    'Q': [
            (100, _gen_coins, ("SP", 3, 6, 0, 1)),
         ],
    'R': [
            (100, _gen_coins, ("EP",  2, 6, 0, 1)),
         ],
    'S': [
            (100, _gen_coins, ("GP",  2, 4, 0, 1)),
         ],
    'T': [
            (100, _gen_coins, ("PP",  1, 6, 0, 1)),
         ],
    'U': [
            ( 50, _gen_coins, ("CP", 1, 20, 0, 1)),
            ( 50, _gen_coins, ("SP", 1, 20, 0, 1)),
            ( 25, _gen_coins, ("GP", 1, 20, 0, 1)),
            (  5, _gen_gems,  (1, 4, 0, 1)),
            (  5, _gen_art,   (1, 4, 0, 1)),
            (  2, _gen_magic, ("Any", 0, 0, 1, 1)),
         ],
    'V': [
            ( 25, _gen_coins, ("SP", 1, 20, 0, 1)),
            ( 25, _gen_coins, ("EP", 1, 20, 0, 1)),
            ( 50, _gen_coins, ("GP", 1, 20, 0, 1)),
            ( 25, _gen_coins, ("PP", 1, 20, 0, 1)),
            ( 10, _gen_gems,  (1, 4, 0, 1)),
            ( 10, _gen_art,   (1, 4, 0, 1)),
            (  5, _gen_magic, ("Any", 0, 0, 1, 1)),
         ],

    'U1': [
            ( 75, _gen_coins, ("CP", 1, 8, 0, 100)),
            ( 50, _gen_coins, ("SP", 1, 6, 0, 100)),
            ( 25, _gen_coins, ("EP", 1, 4, 0, 100)),
            (  7, _gen_coins, ("GP", 1, 4, 0, 100)),
            (  1, _gen_coins, ("PP", 1, 4, 0, 100)),
            (  7, _gen_gems,  (1, 4, 0, 1)),
            (  3, _gen_art,   (1, 4, 0, 1)),
            (  2, _gen_magic, ("Any", 0, 0, 1, 1)),
    ],

    'U2': [
            ( 50, _gen_coins, ("CP", 1, 10, 0, 100)),
            ( 50, _gen_coins, ("SP", 1, 8, 0, 100)),
            ( 25, _gen_coins, ("EP", 1, 6, 0, 100)),
            ( 20, _gen_coins, ("GP", 1, 6, 0, 100)),
            (  2, _gen_coins, ("PP", 1, 4, 0, 100)),
            ( 10, _gen_gems,  (1, 6, 0, 1)),
            (  7, _gen_art,   (1, 4, 0, 1)),
            (  5, _gen_magic, ("Any", 0, 0, 1, 1)),
    ],

    'U3': [
            ( 30, _gen_coins, ("CP", 2, 6, 0, 100)),
            ( 50, _gen_coins, ("SP", 1, 10, 0, 100)),
            ( 25, _gen_coins, ("EP", 1, 8, 0, 100)),
            ( 50, _gen_coins, ("GP", 1, 6, 0, 100)),
            (  4, _gen_coins, ("PP", 1, 4, 0, 100)),
            ( 15, _gen_gems,  (1, 6, 0, 1)),
            (  7, _gen_art,   (1, 6, 0, 1)),
            (  8, _gen_magic, ("Any", 0, 0, 1, 1)),
    ],

    'U45': [
            ( 20, _gen_coins, ("CP", 3, 6, 0, 100)),
            ( 50, _gen_coins, ("SP", 2, 6, 0, 100)),
            ( 25, _gen_coins, ("EP", 1, 10, 0, 100)),
            ( 50, _gen_coins, ("GP", 2, 6, 0, 100)),
            (  8, _gen_coins, ("PP", 1, 4, 0, 100)),
            ( 20, _gen_gems,  (1, 8, 0, 1)),
            ( 10, _gen_art,   (1, 6, 0, 1)),
            ( 12, _gen_magic, ("Any", 0, 0, 1, 1)),
    ],

    'U67': [
            ( 15, _gen_coins, ("CP", 4, 6, 0, 100)),
            ( 50, _gen_coins, ("SP", 3, 6, 0, 100)),
            ( 25, _gen_coins, ("EP", 1, 12, 0, 100)),
            ( 70, _gen_coins, ("GP", 2, 8, 0, 100)),
            ( 15, _gen_coins, ("PP", 1, 4, 0, 100)),
            ( 30, _gen_gems,  (1, 8, 0, 1)),
            ( 15, _gen_art,   (1, 6, 0, 1)),
            ( 16, _gen_magic, ("Any", 0, 0, 1, 1)),
    ],

    'U8': [
            ( 10, _gen_coins, ("CP", 5, 6, 0, 100)),
            ( 50, _gen_coins, ("SP", 5, 6, 0, 100)),
            ( 25, _gen_coins, ("EP", 2, 8, 0, 100)),
            ( 75, _gen_coins, ("GP", 4, 6, 0, 100)),
            ( 30, _gen_coins, ("PP", 1, 4, 0, 100)),
            ( 40, _gen_gems,  (1, 8, 0, 1)),
            ( 30, _gen_art,   (1, 8, 0, 1)),
            ( 20, _gen_magic, ("Any", 0, 0, 1, 1)),
    ],

    # coinage

    'CP': [
            (100, _gen_coins, ("CP", 0, 0, 1, 1)),
         ],
    'SP': [
            (100, _gen_coins, ("SP", 0, 0, 1, 1)),
         ],
    'EP': [
            (100, _gen_coins, ("EP",  0, 0, 1, 1)),
         ],
    'GP': [
            (100, _gen_coins, ("GP",  0, 0, 1, 1)),
         ],
    'PP': [
            (100, _gen_coins, ("PP",  0, 0, 1, 1)),
         ],

    # magic classes

    'MAGIC':  [ (100, _gen_magic, ("Any", 0, 0, 1, 1)), ],
    'POTION': [ (100, _gen_magic, ("Potion", 0, 0, 1, 1)), ],
    'SCROLL': [ (100, _gen_magic, ("Scroll", 0, 0, 1, 1)), ],
    'RING':   [ (100, _gen_magic, ("Ring", 0, 0, 1, 1)), ],
    'WSR':    [ (100, _gen_magic, ("WSR", 0, 0, 1, 1)), ],
    'MISC':   [ (100, _gen_magic, ("Misc", 0, 0, 1, 1)), ],
    'ARMOR':  [ (100, _gen_magic, ("Armor", 0, 0, 1, 1)), ],
    'WEAPON': [ (100, _gen_magic, ("Weapon", 0, 0, 1, 1)), ],
}

_treasure_table['U4'] = _treasure_table['U45']
_treasure_table['U5'] = _treasure_table['U45']
_treasure_table['U6'] = _treasure_table['U67']
_treasure_table['U7'] = _treasure_table['U67']

def Types():
    types = _treasure_table.keys()
    ones = filter(lambda x: len(x) == 1, types)
    mults = filter(lambda x: len(x) > 1, types)
    ones.sort()
    mults.sort()
    return ones + mults

def Treasure(typ):
    tr = []
    try:
        tbl = _treasure_table[string.upper(typ)]
        for i in tbl:
            if Dice.D(1, 100, 0) <= i[0]:
                tr = tr + i[1](i[2])
    except:
        tr = [ Unknown.Unknown(typ) ]
    return tr

def Factory(args):

    types = []
    tr = []

    mult = 1

    for i in args:
        if type(i) is tuple:
            i = Dice.D(*i)
        try:
            nmult = int(i)
            mult = nmult
            types.append("%d" % mult)
            continue
        except:
            pass
        types.append(i + ",")
        for n in range(mult):
            tr += Treasure(i)

    types = string.join(types, " ")

    if types[-1] == ',':
        types = types[:-1]

    return (types.upper(), combine(tr))

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print "Usage:  Treasure.py treasuretype [ treasuretype ... ]"
        sys.exit(0)

    types, tr = Factory(sys.argv[1:])

    print "Treasure Type " + string.upper(types)

    vtot = 0.0
    ocat = ''
    qty_len = 1
    for t in tr:
        qty_len = max(len(str(t.qty)), qty_len)
    qty_fmt = "%" + str(qty_len) + "d"
    for t in tr:
        if t.cat != ocat:
            print t.cat
        ocat = t.cat
        if t.value != 0:
            print "   ", qty_fmt % t.qty, t.name, t.value, "GP ea.", \
                t.value * t.qty, "GP total"
        else:
            print "   ", qty_fmt % t.qty, t.name
        for i in t.desc:
            print "       ", i
        vtot = vtot + (t.qty * t.value)
    print "----- Total Value", vtot, "GP\n"

# end of script.
