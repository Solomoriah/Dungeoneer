#!/usr/bin/env python
###############################################################################
#  Gems.py -- generate gems
###############################################################################

import Dice
import _Treasure

_ornamental_stones = [
        'Azurite',          'Banded Agate',
        'Blue Quartz',      'Eye Agate',
        'Hematite',         'Lapis Lazuli',
        'Malachite',        'Moss Agate',
        'Obsidian',         'Rhodochrosite',
        'Tiger Eye',        'Turquoise',
        'Marble',
]

_semi_precious_stones = [
        'Bloodstone',       'Carnelian',
        'Chalcedony',       'Chrysoprase',
        'Citrine',          'Jasper',
        'Moonstone',        'Onyx',
        'Rock Crystal',     'Sardonyx',
        'Smoky Quartz',     'Star Rose Quartz',
        'Zircon',
]

_fancy_stones = [
        'Amber',            'Alexandrite',
        'Amethyst',         'Chrysoberyl',
        'Coral',            'Garnet',
        'Jade',             'Jet',
        'Peridot',          'Tourmaline',
        'Spinel',           'Pearl',
]

_precious_stones = [
        'Pearl',            'Aquamarine',
        'Spinel',           'Garnet',
        'Topaz',
]

_gems = [
        'Black Opal',       'Fire Opal',
        'Opal',             'Oriental Amethyst',
        'Oriental Topaz',   'Sapphire',
]

_jewels = [
        'Emerald',          'Black Sapphire',
        'Diamond',          'Jacinth',
        'Oriental Emerald', 'Ruby',
        'Star Ruby',        'Star Sapphire',
]

_gem_table = [
    ( 0, "",                     None,                     1.0,  0),
    (20, "Ornamental Stones",    _ornamental_stones,      10.0, 10),
    (25, "Semi-Precious Stones", _semi_precious_stones,   50.0,  8),
    (30, "Fancy Stones",         _fancy_stones,          100.0,  6),
    (20, "Precious Stones",      _precious_stones,       500.0,  4),
    ( 5, "Gems",                 _gems,                 1000.0,  2),
    ( 0, "Jewel",                _jewels,               5000.0,  2),
]

class Gem(_Treasure.Item):
    def __init__(self):
        _Treasure.Item.__init__(self)
        row = Dice.NRoll(_gem_table)
        self.name = self.shortname = Dice.Select(_gem_table[row][2])
        self.cat = "Gem"
        self.fullcat = self.fullcat + "." + self.cat
        va = Dice.D(2, 6)
        mult = 1.0
        if va == 2:
            row -= 1
        elif va == 3:
            mult = 0.5
        elif va == 4:
            mult = 0.75
        elif va == 10:
            mult = 1.5
        elif va == 11:
            mult = 2.0
        elif va == 12:
            row += 1
        self.value = _gem_table[row][3] * mult
        if self.value >= 1:
            self.value = int(self.value) * 1.0

if __name__ == '__main__':
    print Gem()

# end of file.
