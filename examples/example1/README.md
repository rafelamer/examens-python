## Primer exemple

En aquesta carpeta podem veure l'estructura típica per a elaborar un examen amb 4 exercicis de manera que les dades de cada exercici es generen de manera aleatòria per a cada estudiant. Els fitxers necessaris són els següents:

1. *estudiants.csv*: fitxer de text amb un estudiant a cada línia amb les dades següents separades per dos punts:
```
NOM:GOGNOMS:DNI:CORREU ELECTRÒNIC:GRUP
```  
Si no es posen el DNI i el grup, sha de deixar el camp en blanc
```
NOM:GOGNOMS::CORREU ELECTRÒNIC:
```  
2. *examen.tex*: conté les dades bàsiques per a generar un examen (fitxer TeX) per a cada estudiant.
3. *p<nombre>.tex*: un fitxer TeX per a cada problema. Ha de contenir l'enunciat del problema i com s'han d'incloure les dades i solucions per a cada estudiant.
4. *Problemes.py*: fitxer en _Python_ que defineix la classe *Problemes* i una funció per a cada un dels problemes. Aquesta funció ha de retornar un diccionari que té com a claus les *paraules* del fitxer TeX que volem substituir i com a *valors*, les cadenes (strings) per les quals s'han de substituir.

Per generar els fitxers TeX i els PDF amb els exàmens, hem d'executar la comanda
```
~$ examen.py --examen=examen.tex --estudiants=estudiants.csv --problemes=4 --tex-engine=pdflatex
```
Aleshores, es crea la carpeta *tex* os s'hi guarden tots els fitxers _.tex_ i _.pdf_.

Altres exemples amb diferents opcions de *examen.py* són
```
~$ examen.py --examen=examen.tex --estudiants=estudiants.csv --problemes=2 --possibles-problemes=4 --aleatori --tex-engine=pdflatex
```
genera exàmens de 2 problemes escollits aleatòriament d'entre el 4 problemes disponibles i els ordena aleatòriament.
```
~$ examen.py --examen=examen.tex --grups=1,3:2,4 --estudiants=estudiants.csv --problemes=2 --possibles-problemes=4 --aleatori --tex-engine=pdflatex
```
genera exàmens de 2 problemes escollint-ne un d'entre el 1 i el 2 i l'altre d'entre el 3 i 4 i els ordena aleatòriament.
```
~$ examen.py --examen=examen.tex --incompatibles=1,2 --estudiants=estudiants.csv --problemes=2 --possibles-problemes=4 --aleatori --tex-engine=pdflatex
```
genera exàmens de 2 problemes escollits aleatòriament d'entre el 4 problemes disponibles i els ordena aleatòriament. En cap examen hi sortiran els problemes 1 i 3.
```
~$ examen.py --examen=examen.tex --estudiants=estudiants.csv --problemes=2 --possibles-problemes=4 --aleatori --tex-engine=pdflatex --json
```
genera exàmens de 2 problemes escollits aleatòriament d'entre el 4 problemes disponibles i els ordena aleatòriament. Guarda les generades aleatòriament en un fitxer _.json_.
```
~$ examen.py --examen=examen.tex --estudiants=estudiants.csv --problemes=2 --possibles-problemes=4 --aleatori --tex-engine=pdflatex --json
```
A més de generar els exàmens guarda les dades aleatòries en el fitxer _examen0%d.json.
```
~$ examen.py --examen=examen.tex --estudiants=estudiants.csv  --dades=examen001.json --tex-engine=pdflatex
```
Genera els exàmens a partir de les dades guardades al fitxer _examen001.json_.
