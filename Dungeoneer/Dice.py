#!/usr/bin/env python
###############################################################################
#  Dice.py -- die rolling utilities
###############################################################################

import random

Select = random.choice

def D(n, s, b = 0, m = 1):
    res = b
    for i in range(n):
        res = res + random.randint(1, s)
    return res * m

def NRoll(table):
    "NRoll() handles single-level tables, returning the index"
    total = 0
    for i in table:
        total = total + i[0]
    sel = D(1, total, 0)
    for i in range(len(table)):
        sel = sel - table[i][0]
        if sel < 1:
            return i
    return None # shouldn't get here.

def Roll(table):
    "Roll() handles single-level tables, returning the row"
    return table[NRoll(table)]

def MRoll(table):
    """MRoll() handles nested tables

    The last element of the table row may be a list,
    in which case it is assumed to be a subtable,
    and is rolled on.

    The last element may also be a callable object;
    it receives the current row as a tuple argument, 
    and must return a "row" (tuple).

    Otherwise, the entire row is returned.
    """
    while table:
        row = Roll(table)
        # print "---", row[1]
        if type(row[-1]) is type([]):
            table = row[-1]
        else:
            try:
                rc = row[-1](row)
            except TypeError:
                rc = row
            row = rc
            table = None
    return row

def tablecalc(tableobj):
    """tablecalc() prepares a table for tableroller()

    The table consists of a list; the first element will be filled with
    an integer value, being the total of the row weights.  Each subsequent 
    list element is a row, consisting of a tuple where the first element
    is an integer weight value and the subsequent elements are implementation
    defined.  This function adds up the weights and assigns the total to the
    first element of the table.
    """
    s = 0
    for row in tableobj[1:]:
        s += row[0]
    tableobj[0] = s

def tableroller(tableobj):
    """tableroller() selects a row from a weighted table which has been
    prepared as described in the tablecalc() function.  tableroller()
    will prepare the table automatically if the first element is 0.
    """
    if tableobj[0] == 0:
        tablecalc(tableobj)

    r = D(1, tableobj[0])
    orig_r = r

    for row in tableobj[1:]:
        r = r - row[0]
        if r <= 0:
            return row

    return [ 0, "FELL OUT " + tableobj[0] + " " + orig_r, 0 ]

# end of script.
