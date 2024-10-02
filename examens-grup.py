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

import os
import re
import sys
import unidecode
from optparse import OptionParser

parser = OptionParser()
parser.add_option("--estudiants",dest="estudiants",default=None)
parser.add_option("--grup",dest="grup",default=None)
parser.add_option("--carpeta",dest="carpeta",default=None)
parser.add_option("--nomfitxer",dest="nomfitxer",default=None)
parser.add_option("--solucions",action="store_true",dest="solucions",default=False)
(options,args) = parser.parse_args()

regex = re.compile(r'^\s*#.*$',re.IGNORECASE)
estudiants = []
est = options.estudiants
try:
    grups = options.grup.split(',')
except:
    grups = None
carpeta = options.carpeta
if carpeta is None:
    print("S'ha d'especificar una carpeta")
    sys.exit(0)
nomfitxer = options.nomfitxer
if nomfitxer is None:
    print("S'ha d'especificar un nom de fitxer resultant")
    sys.exit(0)

try:
    f = open(est,encoding='utf8')
    for line in f:
        line = line.rstrip()
        if regex.match(line):
            continue
        try:
            data = line.split(':')
            estudiants.append({'nom' : data[0],'cognoms' : data[1],'grup' : data[4]})
        except:
            continue
    f.close()
except:
    print("Error de lectura del fitxer d'estudiants")
    sys.exit(0)

l = []
for e in estudiants:
    g = e['grup']
    if grups is not None:
        trobat = False
        for grup in grups:
            trobat = trobat or g.find(grup) == 0
        if not trobat:
            continue
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
