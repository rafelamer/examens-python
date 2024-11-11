#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Filename:   examens-grup.py
Author:     Rafel Amer (rafel.amer AT upc.edu)
Copyright:  Rafel Amer 2020--2024
Disclaimer: This code is presented "as is" and it has been written to
            generate random models of exams for the subject of Linear
            Algebra at ESEIAAT, Technic University of Catalonia
License:    This program is free software: you can redistribute it and/or modify
            it under the terms of the GNU General Public License as published by
            the Free Software Foundation, either version 3 of the License, or
            (at your option) any later version.

 	        See https://www.gnu.org/licenses/
"""
import filetype
import pandas
import os
import re
import sys
import unidecode
from optparse import OptionParser
from pandas_ods_reader import read_ods

def estudiants_from_ods(file,first,number,grups):
    result = []
    count = 0
    for e in file.values:
        count += 1
        if first is not None and count < first:
            continue
        if first is not None and number is not None and count >= first + number:
            continue
        if e[5] == 0:
            continue
        try:
            dades = {'nom'     : e[0],
                     'cognoms' : e[1],
                     'grup'    : e[4] 
                    }
            if grups is not None:
                trobat = False
                for gr in grups:
                    trobat = trobat or e[4].find(gr) == 0
                if trobat:
                    result.append(dades)
            else:
                result.append(dades)
        except:
            pass
    return result
#
#
#
def estudiants_from_excel(file,first,number,grups):
    result = []
    count = 0
    for index, e in file.iterrows():
        count += 1
        if first is not None and count < first:
            continue
        if first is not None and number is not None and count >= first + number:
            continue
        if e[5] == 0:
            continue
        try:
            dades = {'nom'     : e[0],
                     'cognoms' : e[1],
                     'email'   : e[3],
                     'grup'    : e[4] 
                    }
            if grups is not None:
                trobat = False
                for gr in grups:
                    trobat = trobat or e[4].find(gr) == 0
                if trobat:
                    result.append(dades)
            else:
                result.append(dades)
        except:
            pass
    return result
#
#
#
def estudiants_from_csv(file,first,number,grups):
    regex = re.compile(r'^\s*#.*$',re.IGNORECASE)
    result = []
    count = 0
    for e in file:
        if len(e) > 0:
            count += 1
        if first is not None and count < first:
            continue
        if first is not None and number is not None and count > first + number:
            continue
        e = e.strip()
        if regex.match(e):
            continue
        try:
            e = e.split(':')
            dades = {'nom'     : e[0],
                     'cognoms' : e[1],
                     'grup'    : e[4] 
                    }
            if grups is not None:
                trobat = False
                for gr in grups:
                    trobat = trobat or e[4].find(gr) == 0
                if trobat:
                    result.append(dades)
            else:
                result.append(dades)
        except:
            pass
    return result

parser = OptionParser()
parser.add_option("--estudiants",dest="estudiants",default=None)
parser.add_option("--grup",dest="grup",default=None)
parser.add_option("--full",dest="full")
parser.add_option("--primer",dest="primer")
parser.add_option("--nombre",dest="nombre")
parser.add_option("--carpeta",dest="carpeta",default=None)
parser.add_option("--nomfitxer",dest="nomfitxer",default=None)
parser.add_option("--solucions",action="store_true",dest="solucions",default=False)
(options,args) = parser.parse_args()

est = options.estudiants
try:
    grups = options.grup.split(',')
except:
    grups = None
carpeta = options.carpeta
if carpeta is None:
    print("S'ha d'especificar una carpeta")
    sys.exit(0)
try:
    primer = int(options.primer)
except:
    primer = None
try:
    nombre = int(options.nombre)
except:
    nombre = None 
nomfitxer = options.nomfitxer
if nomfitxer is None:
    print("S'ha d'especificar un nom de fitxer resultant")
    sys.exit(0)

full = options.full
try:
    full = int(full)
except:
    pass
if full is None:
    full = 0
if options.estudiants is not None:
    kind = filetype.guess(options.estudiants)
    if kind is not None and kind.mime == 'application/vnd.oasis.opendocument.spreadsheet':
        try:
            f = read_ods(options.estudiants,full,headers=False)
            estudiants = estudiants_from_ods(f,primer,nombre,grups)
        except:
            print("Can't open file or sheet")
            sys.exit(0)
    elif kind is not None and kind.mime in ['application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                                            'application/vnd.ms-excel']:
        f = pandas.read_excel(options.estudiants,full,header=None)
        estudiants = estudiants_from_excel(f,primer,nombre,grups)
    else:
        f = open(options.estudiants,"r")
        estudiants = estudiants_from_csv(f,primer,nombre,grups)
        f.close()
else:
  f = open("%s.csv" % espai,"r")
  estudiants = estudiants_from_csv(f,primer,nombre,grups)
  f.close()

l = []
for e in estudiants:
    filename = f"{e['cognoms']}-{e['nom']}".lower().replace(' ','-')
    filename = unidecode.unidecode(filename)
    filename = filename.replace("'","")
    if options.solucions:
        filename += "-solucio.pdf"
    else:
        filename += ".pdf"
    filename = f"{carpeta}/{filename}"
    l.append(filename)
if len(l) == 0:
    print("No hi ha cap estudiants a la llista")
    sys.exit(0)
l.sort()
filenames = " ".join(l)
comanda = f"pdfunite {filenames} {nomfitxer}"
os.system(comanda)
