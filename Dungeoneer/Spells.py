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

import random
import Dice

spellchart = [
    (0),
    (0, 1),
    (0, 2),
    (0, 2, 1),
    (0, 2, 2),
    (0, 2, 2, 1),
    (0, 3, 2, 2),
    (0, 3, 2, 2, 1),
    (0, 3, 3, 2, 2),
    (0, 3, 3, 2, 2, 1),
    (0, 4, 3, 3, 2, 2),
    (0, 4, 4, 3, 2, 2, 1),
    (0, 4, 4, 3, 3, 2, 2),
    (0, 4, 4, 4, 3, 2, 2),
    (0, 4, 4, 4, 3, 3, 2),
    (0, 5, 4, 4, 3, 3, 2),
    (0, 5, 5, 4, 3, 3, 2),
    (0, 5, 5, 4, 4, 3, 3),
    (0, 6, 5, 4, 4, 3, 3),
    (0, 6, 5, 5, 4, 3, 3),
    (0, 6, 5, 5, 4, 4, 3),
]

clericspells = [

    None, # no level 0 spells

    (
        "Cure Light Wounds*",
        "Detect Evil*",
        "Detect Magic",
        "Light*",
        "Protection from Evil*",
        "Purify Food and Water",
        "Remove Fear*",
        "Resist Cold",
    ),

    (
        "Bless*",
        "Charm Animal",
        "Find Traps",
        "Hold Person",
        "Resist Fire",
        "Silence 15' radius",
        "Speak with Animals",
        "Spiritual Hammer",
    ),

    (
        "Continual Light*",
        "Cure Blindness",
        "Cure Disease*",
        "Growth of Animals",
        "Locate Object",
        "Remove Curse*",
        "Speak with Dead",
        "Striking",
    ),

    (
        "Animate Dead",
        "Create Water",
        "Cure Serious Wounds*",
        "Dispel Magic",
        "Neutralize Poison*",
        "Protection from Evil 10' radius*",
        "Speak with Plants",
        "Sticks to Snakes",
    ),

    (
        "Commune",
        "Create Food",
        "Dispel Evil",
        "Insect Plague",
        "Quest",
        "Remove Quest",
        "Raise Dead*",
        "True Seeing",
        "Wall of Fire",
    ),

    (
        "Animate Objects",
        "Blade Barrier",
        "Find the Path",
        "Heal*",
        "Regenerate",
        "Restoration",
        "Speak with Monsters",
        "Word of Recall",
    ),
]

magicuserspells = [
    None, # no level 0 spells

    (
        "Charm Person",
        "Detect Magic",
        "Floating Disc",
        "Hold Portal",
        "Light",
        "Darkness",
        "Magic Missile",
        "Magic Mouth",
        "Protection from Evil*",
        "Read Languages",
        "Shield",
        "Sleep",
        "Ventriloquism",
    ),

    (
        "Continual Light",
        "Continual Darkness",
        "Detect Evil*",
        "Detect Invisible",
        "ESP",
        "Invisibility",
        "Knock",
        "Levitate",
        "Locate Object",
        "Mirror Image",
        "Phantasmal Force",
        "Web",
        "Wizard Lock",
    ),

    (
        "Clairvoyance",
        "Darkvision",
        "Dispel Magic",
        "Fireball",
        "Fly",
        "Haste",
        "Slow",
        "Hold Person",
        "Invisibility 10' radius",
        "Lightning Bolt",
        "Protection from Evil 10' radius*",
        "Protection from Normal Missiles",
        "Water Breathing",
    ),

    (
        "Charm Monster",
        "Confusion",
        "Dimension Door",
        "Growth of Plants",
        "Reduction of Plants",
        "Hallucinatory Terrain",
        "Ice Storm",
        "Massmorph",
        "Polymorph Other",
        "Polymorph Self",
        "Remove Curse",
        "Bestow Curse",
        "Wall of Fire",
        "Wizard Eye",
    ),

    (
        "Animate Dead",
        "Cloudkill",
        "Conjure Elemental",
        "Feeblemind",
        "Hold Monster",
        "Magic Jar",
        "Passwall",
        "Telekinesis",
        "Teleport",
        "Wall of Stone",
    ),

    (
        "Anti-Magic Shell",
        "Death Spell",
        "Disintegrate",
        "Flesh to Stone*",
        "Geas",
        "Remove Geas",
        "Invisible Stalker",
        "Lower Water",
        "Projected Image",
        "Reincarnate",
        "Wall of Iron",
    ),
]

scrolltable = [
    0,
    (30, 1),
    (25, 2),
    (20, 3),
    (13, 4),
    (9, 5),
    (3, 6),
]

# returns a list of spells

def genspells(clas, level):

    if clas == 0:
        tbl = clericspells
        if level == 1:
            return None
        else:
            row = spellchart[level-1]
    else:
        tbl = magicuserspells
        row = spellchart[level]

    spells = []

    for i in range(len(row)):
        n = row[i]
        sp = {}
        while n:
            spell = random.choice(tbl[i])
            if not sp.has_key(spell):
                sp[spell] = 1
            else:
                sp[spell] += 1
            n -= 1
        keys = sp.keys()
        keys.sort()
        for key in keys:
            if sp[key] > 1:
                spells.append("%dx %s" % (sp[key], key))
            else:
                spells.append(key)
            
    return spells

# creates a scroll of spells

def genscroll(clas, number):
    if clas == 0:
        tbl = clericspells
    else:
        tbl = magicuserspells
    scrollspells = []
    for i in range(number):
        lvl = Dice.tableroller(scrolltable)[1]
        scrollspells.append(random.choice(tbl[lvl]))
    scrollspells.sort()
    return scrollspells

# end of file.
