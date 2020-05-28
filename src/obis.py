#!/usr/bin/env python3

# -*- coding: utf-8 -*- #
import re
import argparse
from OBISdat.utils import *
from OBISdat.core_obis import Obis

def getOpt():
    parser = argparse.ArgumentParser(description="Wrapper for OBI's API [ host: https://api.obis.org/v3 ]")

    parser.add_argument('path', metavar='<path>',
                        default="checklist",
                        help='path for host.................[default = checklist]')
    parser.add_argument('--taxa', nargs='+',
                        metavar="<taxa>",
                        default=None)
    parser.add_argument('--of', nargs='+',
                        metavar="",
                        help="Coupled with country and area path",
                        default=None)
    parser.add_argument('--areaid', metavar="<query parameter>",
                        default=None)
    parser.add_argument('--taxonid', metavar="<query parameter>",
                        default=None)
    parser.add_argument('--datasetid', metavar="<query parameter>",
                        default=None)
    parser.add_argument('--instituteid', metavar="<query parameter>",
                        default=None)
    parser.add_argument('--nodeid', metavar="<query parameter>",
                        default=None)
    parser.add_argument('--startdate', metavar="<query parameter>",
                        default=None)
    parser.add_argument('--enddate', metavar="<query parameter>",
                        default=None)
    parser.add_argument('--startdepth', metavar="<query parameter>",
                        default=None)
    parser.add_argument('--enddepth', metavar="<query parameter>",
                        default=None)
    parser.add_argument('--geometry', metavar="<query parameter>",
                        default=None)
    parser.add_argument('--size', metavar="<query parameter>",
                        default=5000,
                        help='items retrieved by iteration..[default = 5000]')
    parser.add_argument('--out', metavar="str",
                        action='store',
                        default='input_based',
                        help='Output name [Default = <input_based>.tsv]')
    args = parser.parse_args()
    return args

def main():
    args = getOpt()

    query = {
        'scientificname': args.taxa,
        'areaid': args.areaid,
        'taxonid': args.taxonid,
        'datasetid': args.datasetid,
        'instituteid': args.instituteid,
        'nodeid': args.nodeid,
        'startdate': args.startdate,
        'enddate': args.enddate,
        'startdepth': args.startdepth,
        'enddepth': args.enddepth,
        'geometry': args.geometry,
        'size': args.size
    }
    # Obj = Obis({'scientificname': ['Reptilia', 'Mammalia'],
    #             'areaid': '190',
    #             'size': 5000}, 'checklist')

    Obj = Obis(query, args.path)

    if re.findall("(country|area|institute)", args.path):
        out = Obj.geographics(args.of)
    else:
        out = Obj.dataRetriever()

    writeOut(out, args.out, args.path)

if __name__ == '__main__':
    main()