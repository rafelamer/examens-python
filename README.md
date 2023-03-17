# Generador d'exàmens amb Python

*examens-python* és una utilitat per a generar exàmens aleatoris a partir de models de preguntes. Per a generar les dades aleatòries es fa servir el llenguatge de programació _Python_ i la seva llibreria _sympy_.

Es fa servir el _LaTeX_ per a generar els diferents models d'examen. Per tant, per fer servir aquesta utilitat necessitem tenir intal·lats els programes següents:

1. **LaTeX**, preferiblement el TeXLive, que està disponible per a Linux, Windows 10/11  i MacOS (https://www.tug.org/texlive/).
2. **Python**, la versió 3.7 o posterior (https://www.python.org/).
3. **SymPy**, que és una llibreria de _Python_ per a càlcul simbòlic (https://www.sympy.org).
4. **Python unidecode**, que serveix, entre altres coses, per treure els accents de qualsevol text. Es fa servir per treure els accents del nom i cognoms dels estudiants ja que poden donar problemes a l'hora d'ajuntar fitxers amb nom que conté aquests nom i cognoms.
5. **Asymptote**, utilitzat per generar gràfics. (https://asymptote.sourceforge.io/). No és necessari si no volem incluir als examens gràfics fets amb aquest programa. Està inclòs tant a TeXLive com a MiKTeX. Amb Fedora, Debian i Ubuntu s'ha d'instal·lar el paquet _asymtote_.
6. **Git** per descarregar i mantenir actualitzat el repositori. Les distribucions de Linux ja tenen paquets per instal·lar-lo. En Windows 10/11 el podem el podem descarregar de https://git-scm.com/download/win.
7. **Latexmk**, per defecte s'instal·la amb el TeXLive i amb el MiKTeX. Amb Fedora, Debian i Ubuntu s'ha d'instal·lar el paquet _latexmk_.

Amb Windows 10/11 i amb Linux si la nostra distribució no incorpora aquests paqquets, podem executar des de la línia de comandes i com a administrador
```
pip3 install sympy
pip3 install unidecode
```

## Descàrrega

Per a descarregar aquesta utilitat heu d'executar la comanda
```
~$ git clone https://github.com/rafelamer/examens-python.git
```
i per fer-la servir des de qualsevol carpeta on tinguem els models d'examen, les diferents preguntes i el fitxer amb les dades dels estudiants, hem de procedir a

* Copiar els fitxers examen.sty, upc-ma.pdf i eseiaat-ma.pdf a una carpeta on els TeX pugui trobar-los. Amb Linux poden ser _$HOME/texmf/tex/latex/_ o _/usr/local/share/texmf/tex/latex/_ i en Windows 10/11 depèn si teniu instal·lat el TexLive o el MikTeX, però en general ha de ser a la carpeta _localtexmf\\tex\\latex_
* Copiar el fitxer Algebra.py a una carpeta on el Python pugui trobar-lo. Amb Linux pot ser _/usr/local/lib/python3.11/dist-packages/_ i en Windows 10/11 _C:\\Archivos de programa\\Python311\\Lib\\site-packages\\_
* Copiar els fitxers _examen.py_ i _credentials.py_  a una carpeta des d'on es pugui executar des de la línia de comandes. Amb Linux pot ser _/usr/local/bin/_ i en Windpws 10/11 a una carpeta que estigui en el _%Path%_ o bé podem afegir la carpeta _examens-python_ que s'ha creat en executar la comanda _git clone_ al _%Path%_.
* En lloc de copiar també es poden crear enllaços simbòlics mab la comanda _ln_ del Linux o _mklink_ del Windows 10/11


En Linux, he executat les comandes següents:
```
~$ whoami
amer
~$ su -
Password:
~# whoami
root
~# cd /usr/local/bin
~/usr/local/bin# ln -sf /home/amer/Git/examens-python/examen.py .
~/usr/local/bin# ln -sf /home/amer/Git/examens-python/enviar-examens.py .
~/usr/local/bin# ln -sf /home/amer/Git/examens-python/examens-grup.py .
~/usr/local/bin# cd ../lib/python3.11/dist-packages/
~/usr/local/bin/lib/python3.11/dist-packages# ln -sf /home/amer/Git/examens-python/Algebra.py .
~/usr/local/bin/lib/python3.11/dist-packages# ^D
~$ mkdir -P .asy ; cd .asy
~/.asy$ ln -sf /home/amer/Git/examens-python/coordenades.asy .
~/.asy$ cd ..
~$ mkdir -p texmf/tex/latex ; cd texmf/tex/latex
~texmf/tex/latex$ ln -sf /home/amer/Git/examens-python/examen.sty .
~texmf/tex/latex$ ln -sf /home/amer/Git/examens-python/upc-ma.pdf .
~texmf/tex/latex$ ln -sf /home/amer/Git/examens-python/eseiaat-ma.pdf .
~texmf/tex/latex$ ln -sf /home/amer/Git/examens-python/upc-ma-otf.pdf .
~texmf/tex/latex$ ln -sf /home/amer/Git/examens-python/eseiaat-ma-otf.pdf .
~texmf/tex/latex$ cd
~$ ln -sf /home/amer/Git/examens-python/LaTeXMk .latexmkrc
```

En Windows 10/11, obrim el teminal (cmd) com a administrador i executarem
```
C:\Windows\system32> cd "C:\Program Files\Python311
C:\Program Files\Python311> mklink examen.py "C:\Users\Rafel Amer\examens-python\examen.py"
C:\Program Files\Python311> mklink enviar-examens.py "C:\Users\Rafel Amer\examens-python\enviar-examens.py"
C:\Program Files\Python311> mklink examens-grup.py "C:\Users\Rafel Amer\examens-python\examens-grup.py"
C:\Program Files\Python311> cd Lib\site-packages
C:\Program Files\Python311\Lib\site-packages> mklink Algebra.py "C:\Users\Rafel Amer\examens-python\Algebra.py
C:\Program Files\Python311\Lib\site-packages> cd C:\Users\Rafel Amer>
C:\Users\Rafel Amer> mkdir .asy
C:\Users\Rafel Amer> cd .asy
C:\Users\Rafel Amer\.asy> mklink coordenades.asy "C:\Users\Rafel Amer\examens-python\coordenades.asy"
C:\Users\Rafel Amer\.asy> cd ..
C:\Users\Rafel Amer> mkdir -p texmf\tex\latex
C:\Users\Rafel Amer> cd texmf\tex\latex
C:\Users\Rafel Amer\texmf\tex\latex> mklink examen.sty "C:\Users\Rafel Amer\examens-python\examen.sty"
C:\Users\Rafel Amer\texmf\tex\latex> mklink upc-ma.pdf "C:\Users\Rafel Amer\examens-python\upc-ma.pdf"
C:\Users\Rafel Amer\texmf\tex\latex> mklink eseiaat-ma.pdf "C:\Users\Rafel Amer\examens-python\eseiaat-ma.pdf"
C:\Users\Rafel Amer\texmf\tex\latex> mklink upc-ma-otf.pdf "C:\Users\Rafel Amer\examens-python\upc-ma-otf.pdf"
C:\Users\Rafel Amer\texmf\tex\latex> mklink eseiaat-ma-otf.pdf "C:\Users\Rafel Amer\examens-python\eseiaat-ma-otf.pdf"
C:\Users\Rafel Amer\texmf\tex\latex> cd C:\
C:\> mkdir LatexMk
C:\> cd LaTeXMk
C:\LaTeXMk> mklink LaTeXMk "C:\Users\Rafel Amer\examens-python\LaTeXMk"
```

## Utilització

Un cop tenim en una carpeta els fitxers _examen.tex_, _Problemes.py_, _estudiants.csv_ i _p1.tex_, _p2.tex_, _p3.tex_, etc., executem la comanda
```
~$ examen.py --examen=examen.tex --estudiants=estudiants.csv --problemes=4
```
Cada línia del fitxer _estudiants.csv_ ha de ser de la forma
```
NOM:COGNOMS:DNI:CORREU ELECTRÒNIC:GRUP
```
on els camps obligatoris són NOM, COGNOMS i CORREU ELECTRÒNIC. DNI i GRUP poden estar en blanc.

Les opcions que tenim són
```
Utilització: examen.py --examen=<fitxer> --estudiants=<fitxer> --problemes=<enter> [--no-solucions] [--tex-engine=pdflatex]
    --examen=<fitxer>                   : Fitxer LaTeX amb el model d'examen
    --estudiants=<fitxer>               : Fitxer amb nom:cognoms dels estudiants
    --problemes=<nombre|llista>         : Nombre de problemes o llista de problemes
    --possibles-problemes=<nombre>      : Nombre de possibles problemes
                                        : S'escullen aleatòriament d'entre aquest nombre de problemes
    --incompatibles=<incompatibilitats> : Llista d'incompatibiliats
    --grups=<llista>                    : Llista de grups de problemes     
                                        : Si és possible, sortirà un problema de cad grup                        
    --dades=<fitxer>                    : Fitxer amb les dades generades anteriorment
    --tex-engine=<programa>             : Nom del programa de LaTeX utilitzat
                                        : Si no s'especifica, no es generen els PDF
    --aleatori                          : L'ordre dels problemes serà aleatori
    --nombre-examens=<nombre>           : Identifica els fitxers numèricament i no per nom i cognoms
                                        : Quantitat d'exàmens a fer
    --no-solucions                      : No es generen els fitxers amb les solucions
    --json                              : Es guarden la dades dels enunciats en un fitxer json
    --logs                              : Es mostren els logs del latex quan hi ha un error
    --ajuda                             : Imprimeix aquesta ajuda"
```

Cada vegada que es fa una col·lecció d'exàmens aleatoris i s'especifica l'opció --json, es guarden les dades aleatòries en un fitxer JSON, que en el cas anterior seria _examen001.json_. Si volem tornar a generar els exàmens amb les mateixes dades, haurem d'executar
```
~$ examen.py --examen=examen.tex --estudiants=estudiants.csv --dades=examen001.json
```

Si en l'examen hi volem incloure gràfics generats amb l'asymptote (https://asymptote.sourceforge.io/), hem d'instal·lar-lo i també convé instal·lar el _latexmk_:
 ```
~# apt install asymptote
~# apt install latexmk
 ```
i copiar el fitxer _LatexMk_ a la carpeta _/etc_. Aleshores, per generar els PDF executarem la comanda  _examen.py_ amb l'opció _--tex-engine='latexmk -pdf'_.

## Enviament de correus amb Google API

### Credencials

Per poder enviar a cada estudiant un correu electrònic amb el seu examen adjunt, hem de tenir instal·lada l'API del Google. En Linux la podem instal·lar amb la comanda
```
~# apt install python3-testresources
~# pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
A continuació, hem d'activar al nostre compte de GMail la utilització d'aquesta API. Per això, accedim al WEB https://developers.google.com/gmail/api/quickstart/python i cliquem al botó _Enable the Gmail API_. Aleshores, ens demanarà el nostre correu electrònic i contrasenya de GMail. Si cal, tornem a clicar a _Enable the Gmail API_ i se'ns obrirà una finestra on ens demana "Enable GMail API: Enter new project name", hi posem, per exemple, "UPC" i cliquem a "NEXT". A continuació a "Configure your OAuth client" hi posem "Desktop App" i cliquem a "CREATE" i després a "DOWNLOAD CLIENT CONFIGURATION".

Com a resultat d'aquesta operació ens haurem descarregat el fitxer _credentials.json_ i el guardem a la carpeta $HOME/credentials/

El segon pas consisteix en executar el programa _credentials.py_ des d'un terminal
```
~$ credentials.py
```
Se'ns obre una finestra del navegador i ens torna a demanar el nostre correu electrònic i contrasenya de GMail. Una vegada completat tindrem el fitxer _token.pickle_ a la carpeta $HOME/credentials/

El fitxer _token.pickle_ conté una autorització per llegir i enviar correus que té una validesa limitada. Aproximadament al cap d'una hora d'haver-lo descarregat. Per aquest motiu, el programa _enviar-correus.py_, si és necessari actualitza aquest fitxer o torna a descarregar-lo si no el pot actualitzar i per això ha d'obrir un navegador.

Per tant és millor executar el programa _enviar-correus.py_ des d'una sessió en la que es pugui obrir un navegador.

**Advertència**: Si fem servir un ordinador compartit, hem se tenir present que qualsevol persona que tingui accés al fitxer _token.pickle_, pot accedir al nostre correu de GMail. És una bona idea que, una vegada utilitzats, els encriptem, per exemple amb les comandes
```
~$ openssl enc -pbkdf2 -aes-256-cbc -in credentials.json -out credentials.json.data
~$ shred -n 64 credentials.json
~$ openssl enc -pbkdf2 -aes-256-cbc -in token.pickle -out token.pickle.data
~$ shred -n 64 token.pickle
```
Quan els vulguem tornar a utilitzar, els hem de desencriptar:
```
~$ openssl enc -aes-256-cbc -d -in credentials.json.data -out credentials.json
~$ openssl enc -aes-256-cbc -d -in token.pickle.data -out token.pickle
```

### Enviament dels correus

Un cop generat els fitxers PDF amb els enunciats dels exàmens, es poden enviar per correu electrònic als estudiants amb la comanda
```
~$ enviar-examens.py --estudiants=estudiants.csv --subject="Examen Final" --sender=rafel.amer@upc.edu --message=correu.txt
```

En el fitxer _correu.txt_ hi tindrem el cos del missatge que volem enviar a cada estudiant. Per exemple, hi podem escriure les instruccions per a la realització de l'examen

Quan hagi finalitzat l'examen, podem enviar les solucions a cada estudiant afegint l'opció _--solucions_ a la comanda anterior.
```
~$ enviar-examens.py --estudiants=estudiants.csv --subject="Solucions de l'Examen Final" --sender=rafel.amer@upc.edu --message=correu2.txt --solucions
```
