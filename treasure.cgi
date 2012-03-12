#!/usr/bin/python

import cgi, string, time, traceback, sys

try:

    sys.path.append("/home/newcent/lib/python2.3")
    sys.path.append(".")

    from Dungeoneer import Treasure
    import makesite
    import cgilogger

    scriptpath = "treasure.cgi"

    tmpl = makesite.LoadTemplate("template.site")
    data = makesite.Template()

    body = [ ]

    header = [
        "<input type='submit' value='Generate'>",
        "</form>",
        "<table width=620 border=0 cellspacing=0 cellpadding=0 class=small>",
        "<tr><td>",
        "You may enter any treasure type from A to V, or you may generate",
        "single magic items by entering <b>Magic</b>, <b>Potion</b>,",
        "<b>Scroll</b>, <b>WSR</b> (Wand, Staff, or Rod), <b>Misc</b>,",
        "<b>Armor</b>, or <b>Weapon<b>.",
        "</td></tr>",
        "</table>",
        "<p>",
    ]

    form = cgi.FieldStorage()

    if form.has_key("type"):

        typefld = form["type"]
        types = []

        if type(typefld) is type([]):
            for i in typefld:
                types = types + string.split(i.value)
        else:
            types = string.split(typefld.value)

        ttl = "Basic Fantasy RPG Treasure Generator -- "

        if len(types) > 1:
            ttl = ttl + "Types " + string.upper(string.join(types, ", "))
        else:
            ttl = ttl + "Type " + string.upper(string.join(types, ", "))

        data["title"] = ttl

        body.append("<form action='%s'>" % scriptpath)
        body.append("<input type='text' name='type' value='%s'>" \
            % string.join(types, " "))
        body += header

        bgs = [ "white", "#E0E0E0", ]

        body.append("<table border=0 cellspacing=0 width=620>")

        totval = 0
        typenames, tr = Treasure.Factory(tuple(types))

        body.append("<tr bgcolor=white>")
        body.append("<td colspan=5><b>Treasure Type %s</b></td>" % typenames)
        body.append("</tr>")

        body.append("<tr bgcolor='#D0D0D0' valign=bottom>")
        body.append("<td>Qty.</td><td colspan=2>Name/Description</td>")
        body.append("<td>Value<br>Each</td><td>Value<br>Total</td>")
        body.append("</tr>")

        for t in tr:
            body.append("<tr valign=top bgcolor='%s'>" % bgs[0])
            bgs = bgs[1:] + bgs[:1]
            body.append("<td align=right width=60>%g &nbsp;</td>" % t.qty)
            body.append("<td width=440 colspan=2>" + str(t.name) + "</td>")
            if t.value > 0.000001:
                body.append("<td align=right width=60>%g</td>" % t.value)
                body.append("<td align=right width=60>%g</td>" % (t.value * t.qty))
            else:
                body.append("<td>&nbsp;</td>")
                body.append("<td>&nbsp;</td>")
            body.append("</tr>")
            totval = totval + (t.qty * t.value)
            for d in t.desc:
                body.append("<tr>")
                body.append("<td>&nbsp;</td>")
                body.append("<td width=25>--</td>")
                body.append("<td width=350>" + d + "</td>")
                body.append("<td>&nbsp;</td>")
                body.append("<td>&nbsp;</td>")
                body.append("</tr>")

        body.append("<tr bgcolor='#D0D0D0'>")
        body.append("<td colspan=4>Total Value</td>")
        body.append("<td align=right>%g</td>" % totval)
        body.append("</tr>")
        body.append("</table>")
        body.append("<p>")

    else:
        data["title"] = "Basic Fantasy RPG Treasure Generator",
        body.append("<form action='%s'>" % scriptpath)
        body.append("<input type='text' name='type' value=''>")
        body += header

    print "Content-type: text/html"
    print "Cache-control: no-cache"
    print "Expires:", time.asctime(time.gmtime(time.time()))
    print

    data["body"] = string.join(body, "\n")

    print tmpl * data

except:
    print "Content-type: text/plain\n"
    print "<pre>"
    traceback.print_exc(file = sys.stdout)
    print "</pre>"

# end of file.
