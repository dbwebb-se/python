Authors:
    - aar, Andreas Arnesson
    - efo, Emil Folino
Revisions:
    - "2020-10-07": (B, aar) Omgjord för nya rättningsprogrammet HT20.
    - "2019-10-22": (A, efo, aar) individuella examinationen 2019-lp1.


Individuell examination (try1)
==================================

Denna individuella examination består av fem uppgifter. De olika uppgifterna förklaras nedanför och varje uppgift ska lösas i filen "exam.py" i en specifik fördefinierad funktion.

Du kan när du vill under hela examinationen köra kommandot `dbwebb exam correct try1` för att rätta dina lösningar och se hur många poäng du har uppnått.

Utöver att lösa uppgifterna behöver du se till att alla filer valideras med `dbwebb validate try1`.

Du har 5 timmar på dig att lösa uppgifterna och publicera dina lösningar med kommandot `dbwebb exam seal try1` inom tidsramen. Den sista `seal` som görs inom tidsramen är den som kommer användas som betygsunderlag.

**För att få godkänt på examinationen måste du få minst 20 poäng.**

Följande tabell används vid bedömning av den individuella examinationen.

| Bedömningspunkt | Poäng | Din poäng |
|-----------------|-------|-----------|
| Uppgift 1 är implementerad och fungerar enligt specifikationen. | 20 | |
| Uppgift 2 är implementerad och fungerar enligt specifikationen. | 10 | |
| Uppgift 3 är implementerad och fungerar enligt specifikationen. | 10 | |
| Uppgift 4 är implementerad och fungerar enligt specifikationen. | 10 | |
| Uppgift 5 är implementerad och fungerar enligt specifikationen. | 10 | |
| TOTALT | 60 | |

Tillsammans med kursmoment 01-06 ger dessa poäng ditt slutbetyg, [Bedömning och betygsättning](http://dbwebb.se/kurser/faq/bedomning-och-betygsattning-individuell).


Uppgifter
---------------------------------

1. **Sök och ersätt**. Fyll i funktionen `find_replace`. Funktionen ska läsa in filen `manifesto.txt` för att söka och ersätta ord. Funktionen ska ta emot två stycken inputs, en för ordet du ska söka efter och en för ordet som det ska ersättas med. Innehållet ska se exakt likadant ut som tidigare fast med ordet ersatt. Om ett ord finns med flera gånger ska alla ersättas. Skriv ner resultatet till en ny fil som ska heta `output.txt`, alltså skriv inte över `manifesto.txt` läs bara från den.

    **Exempel**

    input:
        Enter word to find: ugly
        Enter word to replace with: ko

    content of `output.txt`:
        Beautiful is better than ko.
        Explicit is better than implicit.
        ...

I exemplet ovan är inte "Enter word to find: " och "Enter word to replace with: " en del av vad vi ger som input. Det är exempel på vad ni kan skriva i input funktionen.

Tips, om du råkar skriva över eller ändrar i `manifesto.txt` kan du först ta en kopia på `exam.py` och sedan göra `dbwebb exam checkout try1` igen.



2. **Inventering på gården**. Fyll i funktionen `count_animals`. Funktionen ska räkna antalet djur av varje art som finns i en dictionary och **returnera** en formaterad sträng med antalet, artens namn och alla djurens namn. Varje art ska vara på en egen rad, arternas ordning ska vara i bokstavsordning och djurens namn ska vara sorterade i bokstavsordning. Resultat strängen får inte ha en radbrytning (`\n`) i slutet.  

    **Exempel**

    input:
    ```
    {
        "ko": ["Mamma Mu", "Kalvin"],
        "gris": "Babe",
    }
    ```
    output:
        "1 gris: Babe
         2 ko: Kalvin, Mamma Mu"



3. **Verifiera ISBN 13 nummer**. Fyll i funktionen `validate_isbn`, den ska ta emot en sträng som argument. Ett giltig nummer är 13 karaktärer långt och innehåller bara siffror. För att kolla om det är giltigt kollar vi om sista siffran i numret är lika med en check siffra. check siffran beräknas med följande metod på de **12** första siffrorna från numret:
    1. Starta från vänster och multiplicera vartannat siffra med 1 och vartannat med 3.
    2. Summera uträkningen från steg 1.
    3. Gör modulus 10 på summan från steg 2.
    4. Om resultatet från steg 3 är noll är check siffran 0. Annars är check siffran 10 minus resultatet från steg 3.
    5. Om check siffran är lika med sista siffran från isbn numret returnera True, annars False.

    **Exempel**
    input:
        "9781617294136"
    output:
        True
    Uträkning:
    ```
    sum = 9*1 + 7*3 + 8*1 + 1*3 + 6*1 + 1*3 + 7*1 + 2*3 + 9*1 + 4*3 + 1*1 + 3*3
    check = 10 - (sum % 10)
    check == 6
    ```



4. **Avgör vinnare**. Fyll i funktionen `decide_winners`, den ska ta emot en lista som argument. Listan innehåller i sin tur andra listor som i sin tur innehåller resultat från set i pingismatcher. Resultatet från ett set är formaterat som en sträng med första spelarens poäng följt av ett bindestreck och andra spelarens poäng. T.ex. "5-11", här vann player2 med 11 mot 5. I funktionen ska du räkna ut om player1 eller player2 vann för varje match. Vinnaren är den som vann flest set och vinnare av ett set är spelaren med flest poäng i setet. Funktionen ska returnera en lista som innehåller vinnaren av de olika matcherna. Om du får en tom lista som argument ska du returnera en tom lista.

    **Exempel**

    input:
        [["11-2", "5-11", "6-11"], ["11-3", "11-5"]]
    output:
        ["player2", "player1"]



5. **Analysera datum och tider**. Fyll i funktionen `validate_bookings`. Den ska ta emot en lista som innehåller dictionaries med information för att boka ett schema. Varje dictionary innehåller datum, tid och kurskod. I funktionen ska du kolla att inga datum och tider överlappar för schemabokningen. Om inga kurser överlappar returnera True annars False.

    **Exempel**
    input:
        [
            {
                "date": "2019-10-28", "time": "10-12", "course": "DV1531"
            },
            {
                "date": "2019-10-28", "time": "9-10", "course": "PA1439"
            }
        ]
    output:
        True
