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
#  Magic.py -- generate magic items
###############################################################################

import string
import Dice, Spells
import _Treasure

###############################################################################
#  Here is the entire magic-item generation table from the 
#  Basic Fantasy RPG Core Rules Release 70
###############################################################################

def _typify(row):
    addl = Dice.MRoll(row[2])
    return (0, row[1] % addl[1])

def _quantify(row):
    num = Dice.D(*row[2])
    return (0, row[1] % num)

def _genscroll(row):
    spells = Spells.genscroll(*row[2])
    return (0, "%s: %s" % (row[1], string.join(spells, ", ")))

_potion_table = [
    (3, "Potion of Clairaudience"),
    (4, "Potion of Clairvoyance"),
    (3, "Potion of Animal Control"),
    (3, "Potion of Dragon Control"),
    (3, "Potion of Giant Control"),
    (3, "Potion of Human Control"),
    (3, "Potion of Plant Control"),
    (3, "Potion of Undead Control"),
    (3, "Potion of Diminution"),
    (7, "Potion of Delusion"),
    (4, "Potion of ESP"),
    (4, "Potion of Fire Resistance"),
    (4, "Potion of Flying"),
    (4, "Potion of Gaseous Form"),
    (4, "Potion of Giant Strength"),
    (4, "Potion of Growth"),
    (4, "Potion of Healing"),
    (5, "Potion of Heroism"),
    (4, "Potion of Invisibility"),
    (4, "Potion of Invulnerability"),
    (4, "Potion of Levitation"),
    (4, "Potion of Longevity"),
    (2, "Potion of Poison"),
    (3, "Potion of Polymorph Self"),
    (8, "Potion of Speed"),
    (3, "Potion of Treasure Finding"),
]

_scroll_table = [
    ( 3, "Scroll of One Clerical Spell",        (0, 1), _genscroll),
    ( 3, "Scroll of Two Clerical Spells",       (0, 2), _genscroll),
    ( 2, "Scroll of Three Clerical Spells",     (0, 3), _genscroll),
    ( 1, "Scroll of Four Clerical Spells",      (0, 4), _genscroll),
    ( 6, "Scroll of One Magic-User Spell",      (2, 1), _genscroll),
    ( 5, "Scroll of Two Magic-User Spells",     (2, 2), _genscroll),
    ( 5, "Scroll of Three Magic-User Spells",   (2, 3), _genscroll),
    ( 4, "Scroll of Four Magic-User Spells",    (2, 4), _genscroll),
    ( 3, "Scroll of Five Magic-User Spells",    (2, 5), _genscroll),
    ( 2, "Scroll of Six Magic-User Spells",     (2, 6), _genscroll),
    ( 1, "Scroll of Seven Magic-User Spells",   (2, 7), _genscroll),
    ( 5, "Cursed Scroll"),
    (10, "Scroll of Protection from Lycanthropes"),
    (14, "Scroll of Protection from Undead"),
    ( 6, "Scroll of Protection from Elementals"),
    ( 5, "Scroll of Protection from Magic"),
    (10, "Map to Type A Treasure"),
    ( 4, "Map to Type E Treasure"),
    ( 3, "Map to Type G Treasure"),
    ( 8, "Map to %d Magic Items", (1, 4), _quantify),
]

_ring_spell_storing_table = [
    (24, "1"),
    (24, "2"),
    (19, "3"),
    (14, "4"),
    (10, "5"),
    ( 5, "6"),
    ( 4, "7"),
]

_rings_table = [
    ( 6, "Ring of Animal Control"),
    ( 6, "Ring of Human Control"),
    ( 7, "Ring of Plant Control"),
    (11, "Ring of Delusion"),
    ( 3, "Ring of Djinni Summoning"),
    (11, "Ring of Fire Resistance"),
    (13, "Ring of Invisibility"),
    ( 9, "Ring of Protection +1"),
    ( 4, "Ring of Protection +2"),
    ( 1, "Ring of Protection +3"),
    ( 2, "Ring of Regeneration"),
    ( 2, "Ring of %s Spell Storing", _ring_spell_storing_table, _typify),
    ( 6, "Ring of Spell Turning"),
    ( 2, "Ring of Telekinesis"),
    ( 7, "Ring of Water Walking"),
    ( 7, "Ring of Weakness"),
    ( 1, "Ring of %d Wishes", (1, 4), _quantify),
    ( 2, "Ring of X-Ray Vision"),
]

_wandstaffrod_table = [
    ( 8, "Rod of Cancellation"),
    ( 4, "Staff of Commanding"),
    (11, "Staff of Healing"),
    ( 2, "Staff of Power"),
    ( 5, "Snake Staff"),
    ( 4, "Staff of Striking"),
    ( 1, "Staff of Wizardry"),
    ( 5, "Wand of Enemy Detection"),
    ( 8, "Wand of Magic Detection"),
    ( 8, "Wand of Secret Door Detection"),
    ( 8, "Wand of Trap Detection"),
    ( 5, "Wand of Fear"),
    ( 5, "Wand of Cold"),
    ( 5, "Wand of Fireballs"),
    ( 5, "Wand of Illusion"),
    ( 5, "Wand of Lightning Bolts"),
    ( 6, "Wand of Paralyzation"),
    ( 5, "Wand of Polymorphing"),
]

_misc_magic_table = [
    (4, "Amulet of Proof Against Detection and Location"),
    (2, "Bag of Devouring"),
    (6, "Bag of Holding"),
    (5, "Boots of Levitation"),
    (5, "Boots of Speed"),
    (5, "Boots of Traveling and Leaping"),
    (6, "Broom of Flying"),
    (3, "Cloak of Displacement"),
    (4, "Crystal Ball"),
    (2, "Crystal Ball with Clairaudience"),
    (1, "Drums of Panic"),
    (1, "Efreeti Bottle"),
    (1, "Bowl Commanding Water Elementals"),
    (1, "Brazier Commanding Fire Elementals"),
    (1, "Censer Commanding Air Elementals"),
    (1, "Stone Commanding Earth Elementals"),
    (7, "Elven Cloak"),
    (7, "Elven Boots"),
    (2, "Flying Carpet"),
    (7, "Gauntlets of Ogre Power"),
    (2, "Girdle of Giant Strength"),
    (6, "Helm of Reading Languages and Magic"),
    (1, "Helm of Telepathy"),
    (1, "Helm of Teleportation"),
    (1, "Horn of Blasting"),
    (9, "Medallion of ESP"),
    (1, "Mirror of Life Trapping"),
    (5, "Rope of Climbing"),
    (3, "Scarab of Protection"),
]

_special_enemy_table = [
    (1, "Lycanthropes"),
    (1, "Spell Users"),
    (1, "Undead"),
    (1, "Dragons"),
    (1, "Regenerators"),
    (1, "Enchanted Monsters"),
]

_special_ability_table = [
    (9, "Casts Light 30' on Command"),
    (3, "Locate Objects"),
    (4, "Flames on Command"),
    (1, "Drains Energy"),
    (1, "%d Wishes", (1, 4), _quantify),
    (2, "Charm Person"),
]

_roll_again_weapon_table = [
    (40, "+1, %s", _special_ability_table, _typify),
    (10, "+2, %s", _special_ability_table, _typify),
    ( 5, "+3, %s", _special_ability_table, _typify),
    ( 2, "+4, %s", _special_ability_table, _typify),
    ( 1, "+5, %s", _special_ability_table, _typify),
    # NOTE:  This table should include +1/+2 and +1/+3 options
    #        but presently does not.
]

_weapon_adjustment_table = [
    (40, "+1"),
    (10, "+2"),
    ( 5, "+3"),
    ( 2, "+4"),
    ( 1, "+5"),
    (17, "+1/+2 vs. %s", _special_enemy_table, _typify),
    (10, "+1/+3 vs. %s", _special_enemy_table, _typify),
    (10, "Roll Again plus Special Ability", _roll_again_weapon_table),
    ( 3, "Cursed, -1",    0),
    ( 2, "Cursed, -2",    0),
]

_missile_weapon_adjustment_table = [
    (46, "+1"),
    (12, "+2"),
    ( 6, "+3"),
    (18, "+1/+2 vs. %s", _special_enemy_table, _typify),
    (12, "+1/+3 vs. %s", _special_enemy_table, _typify),
    ( 4, "Cursed, -1",    0),
    ( 2, "Cursed, -2",    0),
]

_sword_type_table = [
    ( 5, "Shortsword %s", _weapon_adjustment_table, _typify),
    (11, "Longsword %s", _weapon_adjustment_table, _typify),
    ( 2, "Scimitar %s", _weapon_adjustment_table, _typify),
    ( 2, "Greatsword %s", _weapon_adjustment_table, _typify),
]

_axe_type_table = [
    ( 5, "Hand Axe %s", _weapon_adjustment_table, _typify),
    (13, "Battle Axe %s", _weapon_adjustment_table, _typify),
    ( 2, "Great Axe %s", _weapon_adjustment_table, _typify),
]

_mace_type_table = [
    ( 5, "Hammer %s", _weapon_adjustment_table, _typify),
    (13, "Mace %s", _weapon_adjustment_table, _typify),
    ( 2, "Maul (Great Hammer) %s", _weapon_adjustment_table, _typify),
]

_arrow_type_table = [
    (14, "Shortbow Arrows %s", _missile_weapon_adjustment_table, _typify),
    ( 6, "Longbow Arrows %s", _missile_weapon_adjustment_table, _typify),
]

_bolts_type_table = [
    (14, "Light Crossbow Bolts %s", _missile_weapon_adjustment_table, _typify),
    ( 6, "Heavy Crossbow Bolts %s", _missile_weapon_adjustment_table, _typify),
]

_bow_type_table = [
    (14, "Shortbow %s", _missile_weapon_adjustment_table, _typify),
    ( 6, "Longbow %s", _missile_weapon_adjustment_table, _typify),
]

_polearm_type_table = [
    ( 5, "Spear %s", _weapon_adjustment_table, _typify),
    (11, "Pike %s", _weapon_adjustment_table, _typify),
    ( 2, "Longspear %s", _weapon_adjustment_table, _typify),
    ( 2, "Halberd %s", _weapon_adjustment_table, _typify),
]

_weapon_type_table = [
    (18, "Sword", _sword_type_table),
    ( 9, "Dagger %s", _weapon_adjustment_table, _typify),
    ( 9, "Axe", _axe_type_table),
    ( 9, "Mace", _mace_type_table),
    (11, "Arrows", _arrow_type_table),
    (11, "Bolts", _bolts_type_table),
    ( 9, "Bow", _bow_type_table),
    ( 4, "Sling %s", _missile_weapon_adjustment_table, _typify),
    ( 9, "Polearm", _polearm_type_table),
]

_cursed_armor_table = [
    (50, "-1"),
    (30, "-2"),
    (10, "-3"),
]

_armor_adjustment_table = [
    (50, "+1"),
    (30, "+2"),
    (10, "+3"),
    ( 5, "Cursed", _cursed_armor_table),
    ( 5, "Cursed, Armor Class 11"),
]

_shield_adjustment_table = [
    (50, "+1"),
    (30, "+2"),
    (10, "+3"),
    ( 5, "Cursed", _cursed_armor_table),
]

_shield_table = [
    (20, "Buckler Shield %s", _shield_adjustment_table, _typify),
    (20, "Small Shield %s", _shield_adjustment_table, _typify),
    (50, "Medium Shield %s", _shield_adjustment_table, _typify),
    (10, "Large Shield %s", _shield_adjustment_table, _typify),
]

_armor_type_table = [
    ( 7, "Leather Armor %s", _armor_adjustment_table, _typify),
    ( 5, "Studded Leather Armor %s", _armor_adjustment_table, _typify),
    (18, "Chain Mail %s", _armor_adjustment_table, _typify),
    (13, "Plate Mail %s", _armor_adjustment_table, _typify),
    ( 2, "Full Plate Armor %s", _armor_adjustment_table, _typify),
    (54, "Shield", _shield_table),
]

_wpn_armor_table = [
    (70, "Weapons", _weapon_type_table),
    (30, "Armor",   _armor_type_table),
]

_magic_table = [
    (25, "Weapon",         _weapon_type_table),
    (10, "Armor",          _armor_type_table),
    (20, "Potion",         _potion_table),
    (30, "Scroll",         _scroll_table),
    ( 5, "Ring",           _rings_table),
    ( 5, "Wand/Staff/Rod", _wandstaffrod_table),
    ( 5, "Miscellaneous",  _misc_magic_table),
]

_non_weapon_item_table = [
    (10, "Armor",          _armor_type_table),
    (20, "Potion",         _potion_table),
    (30, "Scroll",         _scroll_table),
    ( 5, "Ring",           _rings_table),
    ( 5, "Wand/Staff/Rod", _wandstaffrod_table),
    ( 5, "Miscellaneous",  _misc_magic_table),
]

class Magic(_Treasure.Item):
    __magic_switch = {
        "AN": _magic_table,
        "PO": _potion_table,
        "SC": _scroll_table,
        "AW": _wpn_armor_table,
        "NO": _non_weapon_item_table,
        "RI": _rings_table,
        "WS": _wandstaffrod_table,
        "MI": _misc_magic_table,
        "AR": _armor_type_table,
        "WE": _weapon_type_table,
    }
    def __init__(self, kind = "Any"):
        _Treasure.Item.__init__(self)
        self.cat = "Magic"
        self.fullcat = self.fullcat + "." + self.cat
        row = Dice.MRoll(self.__magic_switch[string.upper(kind)[:2]])
        self.name = self.shortname = row[1]
        if len(row) > 3:
            self.desc = row[3]
    def __str__(self):
        s = self.cat + ": "
        if self.qty != 1:
            s = s + " " + str(self.qty)
        s = s + " " + self.name
        if self.desc:
            s = s + (" [%d sub-items]" % len(self.desc))
        return s

###############################################################################
#  Test Main
###############################################################################

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        # args should be [ [ n ] t ]
        if len(sys.argv) == 2:
            n = 1
            t = sys.argv[1]
        else:
            n = int(sys.argv[1])
            t = sys.argv[2]
        for i in range(n):
            print Magic(t)
    else:
        print Magic()

# end of file.
