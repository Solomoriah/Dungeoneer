#!/usr/bin/python3

# Basic Fantasy RPG Dungeoneer Suite
# Copyright 2007-2019, 2024-2025 Chris Gonnerman
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


import cgi, time, traceback, sys, html


def run():

    myid = "div%f" % time.time()

    sys.path.append(".")

    from Dungeoneer import Treasure

    form = cgi.FieldStorage()
    treasuretype = form.getfirst("treasuretype", None)
    if not treasuretype:
        print("Content-type: text/html\n")
        sys.exit(0)

    types = treasuretype.split()
    typestr = ", ".join(types).upper()
    typ = "Type"
    if len(types) > 1:
        typ = "Types"

    totval = 0
    typenames, tr = Treasure.Factory(tuple(types))

    body = [
        "<table>",
        "<thead>",
        "<tr><td colspan=4><b>Treasure %s %s</b></td>" % (typ, typenames),
        "<td>",
        """<button class=redbutton onclick='$("%s").remove();'>X</button>""" % myid,
        "</td></tr>",
        "</thead>",
        "<tbody>",
        "<tr><td>Qty.</td><td colspan=2>Name/Description</td>",
        "<td>Value Each</td><td>Value Total</td>",
        "</tr>",
    ]

    for t in tr:
        body.append("<tr><td>%g</td>" % t.qty)
        body.append("<td colspan=2>" + str(t.name) + "</td>")
        if t.value > 0.000001:
            body.append("<td>%s</td>" % f'{t.value:,}'.rstrip('0').rstrip('.'))
            body.append("<td>%s</td>" % f'{(t.value * t.qty):,}'.rstrip('0').rstrip('.'))
        else:
            body.append("<td></td><td></td>")
        body.append("</tr>")
        totval = totval + (t.qty * t.value)
        for d in t.desc:
            body.append("<tr>")
            body.append("<td>&nbsp;</td>")
            body.append("<td width=25>--</td>")
            body.append("<td width=350>" + d + "</td>")
            body.append("<td></td><td></td></tr>")

    body.append("</tbody><tfoot><tr><td colspan=4>Total Value</td>")
    body.append("<td>%s</td>" % f'{totval:,}'.rstrip('0').rstrip('.'))
    body.append("</tr></tfoot>")
    body.append("</table>")

    body.append("<p>")

    rc = []
    for t in tr:
        article = "a"
        if t.shortname[0].lower() in "aeiou":
            article = "an"
        t.textvalue = "{:,.0f}".format(t.value)
        t.textqty = "{:,.0f}".format(t.qty)
        if t.cat == "Magic":
            if t.qty > 1:
                rc.append("%s <b>%s</b>" % (t.textqty, t.shortname.lower()))
            else:
                rc.append("%s <b>%s</b>" % (article, t.shortname.lower()))
        elif t.cat == "Coin":
            rc.append("%s %s" % (t.textqty, t.shortname.lower()))
        elif t.value > 0:
            if t.qty == 1:
                rc.append("%s %s (worth %s gp)" % (article, t.shortname.lower(), t.textvalue))
            else:
                rc.append("%s %s (worth %s gp)" % (t.textqty, t.shortname.lower(), t.textvalue))
        else:
            rc.append("%s %s" % (t.textqty, t.shortname.lower()))

    if len(rc) > 2:
        rce = rc[-1]
        rc = rc[:-1]
        body.append("%s, and %s" % (", ".join(rc), rce))
    elif len(rc) == 2:
        body.append("%s and %s" % tuple(rc))
    elif len(rc) == 1:
        body.append(rc[0])
    else:
        body.append("(nothing)")

    block = "\n".join([
        "<div class=treasureblock id='%s'>" % myid,
        "\n".join(body),
        "</div>",
    ])

    print("Content-type: text/html\n")
    print(block)



if __name__ == "__main__":
    run()


# end of file.
