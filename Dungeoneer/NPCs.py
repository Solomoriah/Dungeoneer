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

from Adventurer import *
import Dice

banditarmor = [
    0,
    ( 4, "Leather Armor", 13 ),
    ( 1, "Chain Mail", 15 ),
]

piratearmor = [
    0,
    ( 1, "Leather Armor", 13 ),
    ( 2, "", 11 ),
]

banditweapons = [
    0,
    ( 7, "Battle Axe", 1, "1d8" ),
    ( 6, "Shortsword", 1, "1d6" ),
    ( 7, "Longsword", 1, "1d8" ),
    ( 2, "Scimitar", 1, "1d8" ),
    ( 2, "Spear", 2, "1d6" ),
]

class Bandit(Character):

    def outfit(c, ldr):

        if ldr:
            a = Dice.tableroller(banditarmor)
            c.armor = a[1]
            c.armorvalue = a[2]
        else:
            c.armor = "Leather Armor"
            c.armorvalue = 13

        if ldr:
            magicarmor(c, 5)

        c.calc()

        b = Dice.tableroller(banditweapons)
        c.meleeweapon = b[1]
        c.damage = b[3]

        if ldr:
            magicweapon(c, 5)
            c.potion = genpotion(c.clas, c.level)
            c.scroll = genscroll(c.clas, c.level)


class Pirate(Character):

    def outfit(c, ldr):

        a = Dice.tableroller(piratearmor)
        c.armor = a[1]
        c.armorvalue = a[2]

        if ldr:
            magicarmor(c, 5)

        c.calc()

        w = Dice.tableroller(banditweapons)
        c.meleeweapon = w[1]
        c.damage = w[3]

        if ldr:
            magicweapon(c, 5)
            c.potion = genpotion(c.clas, c.level)
            c.scroll = genscroll(c.clas, c.level)

def magicarmor(c, chance):
    if Dice.D(1, 100) > min(95, c.level * chance):
        return
    if c.armor == "":
        return
    bonus = Dice.tableroller(armorbonus)[1]
    c.armor = "%s +%d" % (c.armor, bonus)
    c.armorvalue = c.armorvalue + bonus

def magicweapon(c, chance):
    if Dice.D(1, 100) > min(95, c.level * chance):
        return
    bonus = Dice.tableroller(meleeweaponbonus)[1]
    c.meleeweapon = "%s %s" % (c.meleeweapon, bonus)
    c.damage = "%s %s" % (c.damage, bonus)

def bandits():

    # how many flunkies?

    ftrs = Dice.D(2, 12)
    thfs = Dice.D(1, 6)

    # if there are 11 or more mooks, a fighter
    # and a thief will lead them; otherwise,
    # 50% chance of either.

    lftr = 0
    lthf = 0

    if (ftrs + thfs) >= 11:
        lftr = Dice.D(1, 4) + 1
        lthf = Dice.D(1, 4) + 1
    else:
        if Dice.D(1, 100) <= 50:
            lftr = Dice.D(1, 4) + 1
        else:
            lthf = Dice.D(1, 4) + 1

    party = []

    if lftr > 0:
        character = Bandit(lftr, 1)
        character.outfit(1)
        party.append(character)

    if lthf > 0:
        character = Bandit(lthf, 3)
        character.outfit(1)
        party.append(character)

    nftrs = ftrs

    while nftrs:
        character = Bandit(1, 1)
        character.outfit(0)
        character.name = ""
        character.noapp = min(nftrs, Dice.D(1, ftrs))
        nftrs -= character.noapp
        party.append(character)

    nthfs = thfs

    while nthfs:
        character = Bandit(1, 3)
        character.outfit(0)
        character.name = ""
        character.noapp = min(nthfs, Dice.D(1, thfs))
        nthfs -= character.noapp
        party.append(character)

    for character in party:
        if character.noapp > 1:
            character.hp = []
            for i in range(character.noapp):
                character.hp.append(character.rollhp())

    return party

def pirates():

    party = []

    # how many flunkies?

    mooks = Dice.D(3, 8)
    mates = Dice.D(1, 3)

    # captain
    character = Pirate(Dice.D(1, 4) + 2, 1)
    character.outfit(1)
    character.name = "Captain " + character.name
    party.append(character)

    # mates
    for i in range(mates):
        character = Pirate(Dice.D(1, 4) + 1, 1)
        character.outfit(1)
        party.append(character)

    # mooks

    nmooks = mooks

    while nmooks:
        character = Pirate(1, 1)
        character.outfit(0)
        character.name = ""
        character.noapp = min(nmooks, Dice.D(1, mooks))
        nmooks -= character.noapp
        character.hp = []
        for i in range(character.noapp):
            character.hp.append(character.rollhp())
        party.append(character)

    return party

def generate(typ):
    if typ == "b":
        party = bandits()
    else:
        party = pirates()
    return showparty(party)

if __name__ == "__main__":

    party = bandits()
    print showparty(party)

# end of file.
