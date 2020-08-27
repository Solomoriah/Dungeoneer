# Basic Fantasy RPG Dungeoneer Suite
# Copyright 2007-2018 Chris Gonnerman
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

import string

import Treasure, Dice, Adventurer, NPCs, Items, Traps, Monsters, Rooms

adventurer = Adventurer.generate
bandit = NPCs.generate

version = "Version 1.1 (Core Rules Release 107)"

##############################################################################
#  Tables and Supporting Functions
##############################################################################

randenc = {

    1: [
        0,
        (1, adventurer, "NPC Adventurer Party", 1),
        (1, bandit, "Bandits", "b"),
    ],

    2: [
        0,
        (1, adventurer, "NPC Adventurer Party", 2),
    ],

    3: [
        0,
        (1, adventurer, "NPC Adventurer Party", 3),
    ],

    4: [
        0,
        (1, adventurer, "NPC Adventurer Party", 4),
    ],

    5: [
        0,
        (1, adventurer, "NPC Adventurer Party", 5),
    ],

    6: [
        0,
        (1, adventurer, "NPC Adventurer Party", 6),
    ],

    7: [
        0,
        (1, adventurer, "NPC Adventurer Party", 7),
    ],

    8: [
        0,
        (1, adventurer, "NPC Adventurer Party", 8),
    ],

    9: [
        0,
        (1, adventurer, "NPC Adventurer Party", 9),
    ],
}

for key in Monsters.monsters.keys():
    monster = Monsters.monsters[key]
    lvl = monster["dungeonlevel"]
    if type(lvl) is int:
        lvl = (lvl,)
    for l in lvl:
        if l > 0:
            if l not in randenc:
                randenc[l] = [ 0 ]
            randenc[l].append((2, key, monster))


def treasureformat(tr):
    trlst = []
    for t in tr:
        if t.qty != 1:
            nm = "%g %s" % (t.qty, t.shortname)
        else:
            nm = t.shortname
        if t.cat != "Coin" and t.value > 0.0000001:
            each = ""
            if t.qty > 1:
                each = " each"
            nm = "%s (%g GP value%s)" % (nm, t.value, each)
        trlst.append(nm)
    return trlst


def null_fn(row, level):
    if row[3]:
        trlst = treasureformat(Treasure.Treasure("U%d" % level))
        return "<p class='Text Body'>" + row[2] + " with Treasure: " + string.join(trlst, ", ")
    return "<p class='Text Body'>" + row[2]


def trap_fn(row, level):
    trap = "<p class='Text Body'>Trap: %s" % Dice.tableroller(Traps.traptable)[1]
    treasure = ""
    if row[3]:
        trlst = treasureformat(Treasure.Treasure("U%d" % level))
        treasure = " with Treasure: %s" % string.join(trlst, ", ")
    return trap + treasure


statblock_fmt = "%(num)s %(name)s: AC %(ac)s, HD %(hitdice)s, #At %(noatt)s, Dam %(dam)s, Mv %(mv)s, Sv %(sv)s, Ml %(ml)s"


def monster_fn(row, level):
    level = min(level, 8)
    if level in randenc:
        rand_tbl = randenc[level]
    else:
        rand_tbl = [ 0 ]
    contents = Dice.tableroller(rand_tbl)
    treasure = ""
    if type(contents[1]) is type(""): # it's a monster
        monster = contents[2]
        hd = monster["hd"]
        if hd[1] == 8:
            monster["hitdice"] = "%d" % hd[0]
        else:
            monster["hitdice"] = "%dd%d" % hd[:-1]
        if hd[2] != 0:
            if hd[2] > 0:
                monster["hitdice"] = "%s+%d" % (monster["hitdice"], hd[2])
            else:
                monster["hitdice"] = "%s%d" % (monster["hitdice"], hd[2])
        tt = None
        if type(monster["tt"]) == tuple:
            tt = monster["tt"]
            ls = []
            for i in tt:
                ls.append(str(i))
            monster["tt"] = string.join(ls, ", ")
        else:
            tt = ( monster["tt"], )
        num = monster["noapp"]
        num = Dice.D(*num)
        if row[3]:
            if monster["tt"] != "None":
                treasure = None
                try:
                    types, tr = Treasure.Factory(tt)
                except:
                    tr = []
                    treasure = " with Treasure Type %s" % monster[-1]
                trlst = treasureformat(tr)
                if not treasure:
                    treasure = " with Treasure: " + string.join(trlst, ", ")
        monster["num"] = num
        monster = (statblock_fmt % monster)

        hplist = []

        for i in range(num):
            hplist.append(Adventurer.hitpointblock(max(1, Dice.D(*hd))))

        monster = monster + string.join(hplist, "\n")

    elif type(contents[1]) != type(""):
        args = contents[3:]
        monster = contents[1](*args)
        treasure = ""
    else:
        monster = contents[1]
        if row[3]:
            treasure = "with Treasure"
    return "%s<p class='Text Body'>%s" % (monster, treasure)


dungeon_table = [
    0,
    (16, null_fn, "Empty", 0),
    ( 4, null_fn, "Empty", 1),
    (40, monster_fn, "Monster", 0),
    (24, monster_fn, "Monster", 1),
    ( 4, null_fn, "Special", 0),
    ( 8, trap_fn, "Trap", 0),
    ( 4, trap_fn, "Trap", 1),
]

def makedungeon(level, rooms, first = 1):

    body = [ ]

    body.append("<p class='Text Body'>\n<b>%d Rooms on Level %d</b>" % (rooms, level))

    for i in range(rooms):
        roomtype = Dice.tableroller(Rooms.roomtypes)
        row = Dice.tableroller(dungeon_table)
        contents = row[1](row, level)
        items = []
        if Dice.D(1, 2) == 1 or row[2] == "Empty":
            for j in range(Dice.D(1, 3)) or row[2] == "Empty":
                items.append(Dice.tableroller(Items.itemtable)[1])
        body.append("<p class='Text Body'>\n<b>%d. %s:</b> %s\n<p class='Text Body'>\n%s"
            % (i+first, roomtype[1], string.join(items, ", "), contents))

    return string.join(body, "\n")


# end of file.
