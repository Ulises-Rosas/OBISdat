#!/usr/bin/env python3

# -*- coding: utf-8 -*- #
import argparse
import urllib.request
import json
import re

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

class Obis:

    def __init__(self, opts = None, path = None):

        if opts is None:
            opts = {'scientificname': None,'size': 5000}

        opts2 = {}

        for k, v in opts.items():
            if isinstance(v, str):
                opts2[k] = v.replace(" ", "%20")
            else:
                opts2[k] = v

        self.host = 'https://api.obis.org/v3'
        self.opts = opts2
        self.path = path
        self.size = opts['size']
        ## cases where size does not work
        ## so far
        self.afterPaths = [
            'occurrence'
        ]

    @property
    def header(self):
        mh   = lambda d: "&".join(["%s=%s" % (i, j) for i, j in d.items() if j is not None])
        opts = self.opts
        taxa = opts['scientificname']
        out  = []
        if taxa is not None:
            for i in taxa:
                opts['scientificname'] = i.replace(" ", "%20")
                out.append( mh(opts) )
        else:
            out.append( mh(opts) )
        return out

    @property
    def isAfterNeeded(self):
        regAfterPath = "|".join(["^%s$" % i for i in self.afterPaths])

        return bool(re.findall(regAfterPath, self.path))

    def dataRetriever(self):


        headers = self.header
        afned   = self.isAfterNeeded
        out     = []
        for n, head in enumerate(headers):

            page  = 1
            skip  = 0
            after = -1
            done  = 0
            total = 0

            print("\n%s. Downloading from %s path" % (n + 1, self.path))
            while True:

                url = "%s/%s?%s&" % (self.host, self.path, head)
                if afned:
                    complete_url = url + "after=%s" % after
                else:
                    complete_url = url + "skip=%s"  % skip

                allJson = json.load(urllib.request.urlopen(complete_url))
                results = allJson['results']

                if len(results) == 0:
                    break

                if page == 1:
                    total += allJson['total']
                    out.append( "\t".join(["%s" % i for i in results[0].keys()]) )
                    page += 1

                for element in results:
                    out.append( "\t".join(["%s" % str(x) for _, x in element.items()]) )

                done += len(results)

                print("   %s/%s records handled" % (done, total))

                if done == total:
                    break

                if afned:
                    after = results[-1]['id']

                skip += self.size

        return out

    def geographics(self, of):

        dat = self.dataRetriever()
        if of is None:
            return dat
        else:
            out = []
            for i in of:
                for ii in dat[1:]:
                    if re.findall( i, ii):
                        out.append(ii)
            out.insert(0, dat[0])
            return out

def cname(s,ty):

    tail = "obis_%s.tsv" % ty.replace("/", "_")
    fo   = "%s_%s" % (s, tail) if s != "input_based" else tail
    return fo

def writeOut(out, s, ty):

    f = open(  cname(s, ty), 'w' )
    for i in out:
        f.write(i + "\n")
    f.close()

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
    # Obj = Obis({'scientificname': ['Reptilia', 'Mammalia'], 'areaid': '190', 'size': 5000}, 'checklist')

    Obj = Obis(query, args.path)

    if re.findall("(country|area|institute)", args.path):
        out = Obj.geographics(args.of)
    else:
        out = Obj.dataRetriever()

    writeOut(out, args.out, args.path)

if __name__ == '__main__':
    main()