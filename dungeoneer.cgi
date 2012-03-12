#!/usr/bin/python

import os, sys, string

sys.path.append("/home/newcent/lib/python2.3")
import makesite

sys.path.append(".")
from Dungeoneer import Treasure, Dice, Stocker

sys.stderr = sys.stdout

def safeint(s, b):
    try:
        return int(s)
    except:
        return b

try:
    # generate the dungeon

    fields = {}
    for i in string.split(os.environ["QUERY_STRING"], "&"):
        key, value = string.split(i, "=", maxsplit=1)
        fields[key] = value

    level = max(safeint(fields["level"], 1), 1)
    first = max(safeint(fields["first"], 1), 1)
    rooms = max(safeint(fields["rooms"], 1), 1)

    body = Stocker.makedungeon(level, rooms, first)

    print "Content-type: text/html\n"
    print body
    
except:

    import traceback

    print "Content-type: text/plain\n"

    print "<pre>"
    traceback.print_exc(file=sys.stdout)
    print "</pre>"
    

# end of file.
