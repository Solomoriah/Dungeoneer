#!/usr/bin/python

import string

import Treasure, Dice, Adventurer, NPCs, Items, Traps

adventurer = Adventurer.generate
bandit = NPCs.generate

version = "Version 1.0 (Core Rules Release 74)"

##############################################################################
#  Tables and Supporting Functions
##############################################################################

statblock = {
    "name": 1,
    "ac": 2,
    "hd": 3,
    "noatt": 4,
    "dam": 5,
    "mv": 6,
    "noapp": 7,
    "sv": 8,
    "ml": 9,
    "tt": 10,
}

randenc_level1 = [
    0,
    (1, "Giant Bee", 13, (1, 4, 0), "1 sting", "1d4 + poison", "10' Fly 50'", (1, 6, 0), "F1", 9, "Special"),
    (1, "Goblin", 14, (1, 8, -1), "1 weapon", "1d6 or by weapon", "20'", (2, 4, 0), "F1", 7, "C"),
    (1, "Green Slime*", "can always be hit", (2, 8, 0), "1", "special", "1'", (0, 0, 1), "F2", 12, "None"),
    (1, "Kobold", 13, (1, 4, 0), "1 weapon", "1d4 or by weapon", "20'", (4, 4, 0), "NM", 6, "C"),
    (1, adventurer, "NPC Adventurer Party", 1),
    (1, bandit, "Bandits", "b"),
    (1, "Orc", 14, (1, 8, 0), "1 weapon", "1d8 or by weapon", "40'", (2, 4, 0), "F1", 8, "D"),
    (1, "Skeleton", 13, (1, 8, 0), "1", "1d6 or by weapon", "40'", (3, 4, 0), "F1", 12, "None"),
    (1, "Spitting Cobra", 13, (1, 8, 0), "1 bite or 1 spit", "1d4 + poison or blindness", "30'", (1, 6, 0), "F1", 7, "None"),
    (1, "Giant Crab Spider", 13, (2, 8, 0), "1 bite", "1d8 + poison", "40'", (1, 4, 0), "F2", 7, "None"),
    (1, "Stirge", 13, (1, 8, 0), "1 bite", "1d4 + 1d4/round blood drain", "10' Fly 60'", (1, 10, 0), "F1", 9, "D"),
    (1, "Wolf", 13, (2, 8, 0), "1 bite", "1d6", "60'", (2, 6, 0), "F2", 8, "None"),
]

randenc_level2 = [
    0,
    (1, "Giant Bombardier Beetle", 16, (2, 8, 0), "1 bite/1 spray",
        "1d6/2d6 (cone 10' wide by 10' long from rear of monster, save vs. Death Ray for half damage)",
        "40'", (1, 8, 0), "F2", 8, "None"),
    (1, "Giant Fly", 14, (2, 8, 0), "1 bite", "1d8", "30' Fly 60'", (1, 6, 0), "F1", 8, "None"),
    (1, "Ghoul", 14, (2, 8, 0), "2 claws/1 bite", "1d4/1d4/1d4, all plus paralysis", "30'", (1, 6, 0), "F2", 9, "B"),
    (1, "Gnoll", 15, (2, 8, 0), "1 weapon", "2d4 or by weapon +1", "30'", (1, 6, 0), "F1", 8,
        ("D", "K")),
    (1, "Gray Ooze", 12, (3, 8, 0), "1", "2d8", "1'", (0, 0, 1), "F3", 12, "None"),
    (1, "Hobgoblin", 14, (1, 8, 0), "1 weapon", "1d8 or by weapon", "30'", (1, 6, 0), "F1", 8,
        ("D", "K")),
    (1, "Lizard Man", 15, (2, 8, 0), "1 weapon", "1d6+1 or by weapon +1", "20'", (2, 4, 0), "F2", 11, "D"),
    (1, "Pit Viper", 14, (2, 8, 0), "1 bite", "1d4 + poison", "30'", (1, 8, 0), "F2", 7, "None"),
    (1, adventurer, "NPC Adventurer Party", 2),
    (1, "Giant Black Widow Spider", 14, (3, 8, 0), "1 bite", "2d6 + poison", "20' Web 40'", (1, 3, 0), "F3", 8, "None"),
    (1, "Troglodyte", 15, (2, 8, 0), "2 claws/1 bite", "1d4/1d4/1d4", "40'", (1, 8, 0), "F2", 9, "A"),
    (1, "Zombie", 12, (2, 8, 0), "1", "1d8 or by weapon", "20'", (2, 4, 0), "F2", 12, "None"),
]

randenc_level3 = [
    0,
    (1, "Giant Ant", 17, (4, 8, 0), "1", "2d6", "60'", (2, 6, 0), "F4", 7, "U"),
    (1, "Carnivorous Ape", 14, (4, 8, 0), "2 claws", "1d4/1d4", "40'", (1, 6, 0), "F4", 7, "None"),
    (1, "Giant Tiger Beetle", 17, (3, 8, 1), "1", "2d6", "50'", (1, 6, 0), "F3", 9, "U"),
    (1, "Bugbear", 15, (2, 8, 2), "1 weapon", "1d8 or by weapon", "30'", (2, 4, 0), "F2", 9,
        ("B", "L", "M")),
    (1, "Doppleganger", 15, (4, 8, 0), "1", "1d12 or by weapon", "30'", (1, 6, 0), "F4", 10, "E"),
    (1, "Gargoyle", 15, (4, 8, 0), "2 claws/1 bite/1 horn", "1d4/1d4/1d6/1d4", "30' Fly 50' (15')", (1, 6, 0), "F6", 11, "C"),
    (1, "Gelatinous Cube", 12, (4, 8, 0), "1", "2d4 + paralysis", "20'", (0, 0, 1), "F2", 12, "V"),
    (1, "Lycanthrope, Wererat*", 13, (3, 8, 0), "1 bite or 1 weapon", "1d4 or 1d6 or by weapon", "40'", (1, 8, 0), "F3", 8, "C"),
    (1, "Ogre", 15, (4, 8, 1), "1 weapon", "2d6", "30'", (1, 6, 0), "F4", 10, ("C", (1, 20, 0, 100), "GP")),
    (1, "Shadow", 13, (2, 8, 0), "1 touch", "1d4 + 1 point Strength loss", "30'", (1, 10, 0), "F2", 12, "F"),
    (1, "Tentacle Worm", 13, (3, 8, 0), "6 tentacles", "paralysis", "40'", (1, 3, 0), "F3", 9, "B"),
    (1, "Wight*", 15, (3, 8, 0), "1 touch", "Energy drain (1 level)", "30'", (1, 6, 0), "F3", 12, "B"),
]

randenc_level45 = [
    0,
    (1, "Bear, Cave", 15, (7, 8, 0), "2 claws/1 bite + hug", "1d8/1d8/2d6 + 2d8 hug", "40'", (1, 2, 0), "F7", 9, "None"),
    (1, "Caecilia, Giant", 14, (6, 8, 0), "1 bite + swallow on 19/20", "1d8 + 1d8/round if swallowed", "20' (10')", (1, 3, 0), "F3", 9, "B"),
    (1, "Cockatrice", 14, (5, 8, 0), "1 beak + special", "1d6 + petrification", "30' Fly 60' (10')", (1, 4, 0), "F5", 7, "D"),
    (1, "Doppleganger", 15, (4, 8, 0), "1", "1d12 or by weapon", "30'", (1, 6, 0), "F4", 10, "E"),
    (1, "Gray Ooze", 12, (3, 8, 0), "1", "2d8", "1'", (0, 0, 1), "F3", 12, "None"),
    (1, "Hellhound", 15, (4, 8, 0), "1 bite or 1 breath", "1d6 or 1d6 per Hit Die", "40'", (2, 4, 0), "F4", 9, "C"),
    (1, "Lycanthrope, Werewolf*", 15, (4, 8, 0), "1 bite", "2d4", "60' Human Form 40'", (1, 6, 0), "F4", 8, "C"),
    (1, "Minotaur", 14, (6, 8, 0), "1 gore/1 bite or 1 weapon", "1d6/1d6 or by weapon + 2", "40'", (1, 6, 0), "F6", 11, "C"),
    (1, "Ochre Jelly*", 12, (5, 8, 0), "1", "2d6", "10'", (0, 0, 1), "F5", 12, "None"),
    (1, "Owlbear", 15, (5, 8, 0), "2 claws/1 bite + 1 hug", "1d8/1d8/1d8 + 2d8", "40'", (1, 4, 0), "F5", 9, "C"),
    (1, "Rust Monster*", 18, (5, 8, 0), "1", "special", "40'", (1, 4, 0), "F5", 7, "None"),
    (1, "Wraith*", 15, (4, 8, 0), "1 touch", "1d6 + energy drain (1 level)", "Fly 80'", (1, 4, 0), "F4", 12, "E"),
]

randenc_level67 = [
    0,
    (1, "Basilisk", 16, (6, 8, 0), "1 bite/1 gaze", "1d10/petrification", "20' (10')", (1, 6, 0), "F6", 9, "F"),
    (1, "Black Pudding*", 14, (10, 8, 0), "1", "3d8", "20'", (0, 0, 1), "F10", 12, "None"),
    (1, "Caecilia, Giant", 14, (6, 8, 0), "1 bite + swallow on 19/20", "1d8 + 1d8/round if swallowed", "20' (10')", (1, 3, 0), "F3", 9, "B"),
    (1, "Displacer", 16, (6, 8, 0), "2 blades", "1d8/1d8", "50'", (1, 4, 0), "F6", 8, "D"),
    (1, "Hydra, 6 Headed", 17, (6, 8, 0), "6 bites", "1d10 per bite", "40' (10')", (0, 0, 1), "F6", 9, "B"),
    (1, "Lycanthrope, Weretiger*", 17, (5, 8, 0), "2 claws/1 bite", "1d6/1d6/2d6", "50' Human Form 40'", (1, 4, 0), "F5", 9, "C"),
    (1, "Mummy*", 17, (5, 8, 0), "1 touch + disease", "1d12 + disease", "20'", (1, 4, 0), "F5", 12, "D"),
    (1, "Owlbear", 15, (5, 8, 0), "2 claws/1 bite + 1 hug", "1d8/1d8/1d8 + 2d8", "40'", (1, 4, 0), "F5", 9, "C"),
    (1, "Rust Monster*", 18, (5, 8, 0), "1", "special", "40'", (1, 4, 0), "F5", 7, "None"),
    (1, "Scorpion, Giant", 15, (4, 8, 0), "2 claws/1 stinger", "1d10/1d10/1d6 + poison", "50' (10')", (1, 6, 0), "F2", 11, "None"),
    (1, "Spectre*", 17, (6, 8, 0), "1 touch", "Energy drain 2 levels/touch", "Fly 100'", (1, 4, 0), "F6", 11, "E"),
    (1, "Troll", 16, (6, 8, 0), "3", "1d6/1d6/1d10", "40'", (1, 8, 0), "F6", 10, "D"),
]

randenc_level8 = [
    0,
    (1, "Black Pudding*", 14, (10, 8, 0), "1", "3d8", "20'", (0, 0, 1), "F10", 12, "None"),
    (1, "Chimera", 16, (9, 8, 0), "2 claws/3 heads + special", "1d4/1d4/2d4/2d4/3d4 + special", "40' (10') Fly 60' (15')", (1, 2, 0), "F9", 9, "F"),
    (1, "Giant, Hill", 15, (8, 8, 0), "1", "2d8", "40'", (1, 4, 0), "F8", 8, ("E", (1, 8, 0, 1000), "GP")),
    (1, "Giant, Stone", 17, (9, 8, 0), "1 stone club or 1 thrown rock", "3d6 or 3d6", "40'", (1, 2, 0), "F9", 9, ("E", (1, 8, 0, 1000), "GP")),
    (1, "Hydra, 7 Headed", 18, (7, 8, 0), "7 bites", "1d10 per bite", "40' (10')", (0, 0, 1), "F7", 9, "B"),
    (1, "Lycanthrope, Wereboar*", 16, (4, 8, 0), "1 bite", "2d6", "50' Human Form 40'", (1, 4, 0), "F4", 9, "C"),
    (1, "Purple Worm", 16, (11, 8, 0), "1 bite/1 sting", "2d8/1d8+poison", "20' (15')", (1, 2), "F6", 10, "None"),
    (1, "Salamander*, Flame", 19, (8, 8, 0), "2 claws/1 bite+heat", "1d4/1d4/1d8+1d8/round", "40'", (1, 4, 1), "F8", 8, "F"),
    (1, "Salamander*, Frost", 21, (12, 8, 0), "4 claws/1 bite+cold", "1d6/1d6/1d6/1d6/2d6+1d8/round", "40'", (1, 3, 0), "F12", 9, "E"),
    (1, "Vampire*", 18, (7, 8, 0), "1 weapon or special", "1d8 or by weapon or special", "40' Fly 60'", (1, 6, 0), "F7", 11, "F"),
]

randenc_select = [
    None,
    randenc_level1,
    randenc_level2,
    randenc_level3,
    randenc_level45,
    randenc_level45,
    randenc_level67,
    randenc_level67,
    randenc_level8,
]

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

statblock_fmt = "%s %s (AC %s, HD %s, #At %s, Dam %s, Mv %s, Sv %s, Ml %s)"

def monster_fn(row, level):
    level = min(level, 8)
    rand_tbl = randenc_select[level]
    contents = Dice.tableroller(rand_tbl)
    treasure = ""
    if len(contents) == 11:
        monster = list(contents[1:])
        monster[1] = str(monster[1])
        monster[8] = str(monster[8])
        hd = monster[2]
        if hd[1] == 8:
            monster[2] = "%d" % hd[0]
        else:
            monster[2] = "%dd%d" % hd[:-1]
        if hd[2] != 0:
            if hd[2] > 0:
                monster[2] = "%s+%d" % (monster[2], hd[2])
            else:
                monster[2] = "%s%d" % (monster[2], hd[2])
        tt = None
        if type(monster[9]) == tuple:
            tt = monster[9]
            ls = []
            for i in tt:
                ls.append(str(i))
            monster[9] = string.join(ls, ", ")
        else:
            tt = ( monster[9], )
        num = monster[6]
        del monster[6]
        num = Dice.D(*num)
        if row[3]:
            if monster[-1] != "None":
                treasure = None
                try:
                    types, tr = Treasure.Factory(tt)
                except:
                    tr = []
                    treasure = " with Treasure Type %s" % monster[-1]
                trlst = treasureformat(tr)
                if not treasure:
                    treasure = " with Treasure: " + string.join(trlst, ", ")
        monster = tuple([ str(num) ] + monster[:-1])
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
        row = Dice.tableroller(dungeon_table)
        contents = row[1](row, level)
        items = []
        if Dice.D(1, 2) == 1 or row[2] == "Empty":
            for j in range(Dice.D(1, 3)) or row[2] == "Empty":
                items.append(Dice.tableroller(Items.itemtable)[1])
        body.append("<p class='Text Body'>\n<b>Room %d:</b> %s\n<p class='Text Body'>\n%s" % (i+first, string.join(items, ", "), contents))

    return string.join(body, "\n")


# end of file.
