#!/usr/bin/env python3

# -*- coding: utf-8 -*- #
def cname(s,ty):

    tail = "obis_%s.tsv" % ty.replace("/", "_")
    fo   = "%s_%s" % (s, tail) if s != "input_based" else tail
    return fo

def writeOut(out, s, ty):

    f = open(  cname(s, ty), 'w' )
    for i in out:
        f.write(i + "\n")
    f.close()
