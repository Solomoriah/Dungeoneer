#!/usr/bin/python3

# Basic Fantasy RPG Dungeoneer Suite
# Copyright 2007-2024 Chris Gonnerman
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


import cgi, string, time, traceback, sys

try:

    sys.path.append(".")

    from Dungeoneer import Treasure
    import makesite

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

    print("Content-type: text/html")
    print("Cache-control: no-cache")
    print("Expires:", time.asctime(time.gmtime(time.time())))
    print("")

    data["body"] = string.join(body, "\n")

    print(tmpl * data)

except:
    print("Content-type: text/plain\n")
    print("<pre>")
    traceback.print_exc(file = sys.stdout)
    print("</pre>")


# end of file.
