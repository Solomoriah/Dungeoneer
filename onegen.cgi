#!/usr/bin/python

import cgi, string, time, traceback, sys

try:

    sys.path.append("/home/newcent/lib/python2.3")
    sys.path.append(".")

    from Dungeoneer import Adventurer

    form = cgi.FieldStorage()

    try:
        level = int(form.getfirst("level", "1"))
    except:
        level = 1

    try:
        klass = int(form.getfirst("class", "0"))
    except:
        klass = 0

    txt = Adventurer.single(klass, level)

    print "Content-type: text/html\n"

    print txt

except:
    print "Content-type: text/plain\n"
    print "<pre>"
    traceback.print_exc(file = sys.stdout)
    print "</pre>"

# end of file.
