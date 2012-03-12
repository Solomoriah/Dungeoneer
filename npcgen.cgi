#!/usr/bin/python

import cgi, string, time, traceback, sys, os

try:

    sys.path.append("/home/newcent/lib/python2.3")
    sys.path.append(".")

    from Dungeoneer import NPCs

    form = cgi.FieldStorage()

    txt = NPCs.generate(form.getfirst("type", "b"))

    print "Content-type: text/html\n"

    print txt

except:
    print "Content-type: text/plain\n"
    print "<pre>"
    traceback.print_exc(file = sys.stdout)
    print "</pre>"

# end of file.
