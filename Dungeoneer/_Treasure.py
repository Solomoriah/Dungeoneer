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
#  _Treasure.py -- base functions for treasure generator
###############################################################################


import Dice

categories = {
    "Coin":     0,
    "Gem":      1,
    "Art":      2,
    "Magic":    3,
}

class Generic:
    pass

class Item:

    def __init__(self):

        self.value = 0.0
        self.name = ''
        self.desc = []
        self.fullcat = self.cat = 'Item'
        self.qty = 1

    def __cmp__(self, other):
        if str(self) < str(other):
            return -1
        if str(self) > str(other):
            return 1
        return 0

    def __str__(self):

        s = "%02d %-20s: %-30s " % (categories[self.cat], self.cat, self.name)

        if self.qty != 1:
            s = s + ("%10.2f" % float(self.qty))

        s = s + (" (%10.2f GP total)" % (float(self.value) * self.qty))

        return s

# end of script.
