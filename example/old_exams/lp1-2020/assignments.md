Authors:
    - aar, Andreas Arnesson
    - moc, Martin Borg
Revisions:
    - "2020-10-23": (A, aar, moc) Skapad inför HT20.


Individuell examination (try1)
==================================

Denna individuella examination består av fem uppgifter. De olika uppgifterna förklaras nedanför och varje uppgift ska lösas i filen "exam.py" i en specifik fördefinierad funktion.

Om det inte står i en uppgift att en modul ska importeras får man **inte** använda sig av importerade moduler/biblioteket.

När du rättar din kod, ha enbart `print()` och `input()` anrop i din kod där det efterfrågas av uppgiften. Annars kan det förstöra testerna.

Du kan när du vill under hela examinationen köra kommandot `dbwebb exam correct try1` för att rätta dina lösningar och se hur många poäng du har uppnått.

Utöver att lösa uppgifterna behöver du se till att alla filer validera med `dbwebb validate try1`.

Du har 5 timmar på dig att lösa uppgifterna och publicera dina lösningar med kommandot `dbwebb exam seal try1` inom tidsramen. Den sista `seal` som görs inom tidsramen är den som kommer användas som betygsunderlag.

**För att få godkänt på examinationen måste du få minst 20 poäng**

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

1. **Analysera text**. Den här uppgiften går ut på att du ska analysera textfilerna "title.basics.csv" och "title.ratings.csv" på 2 olika sätt. I filerna representerar varje rad en film, förutom första raden som innehåller kolumn namn för datan i kolumnerna. "title.basics.csv" innehåller ett id, huvudtitel, original titel och året den släpptes för varje film. "title.ratings.csv" innehåller id, genomsnitts betyg och antalet röster för varje film.

Funktionen `analyze_text` ska ta input från användaren för att välja vilken typ av analys som ska genomföras.
De två olika sätten texten ska analyseras på är:
    - Om användaren skriver **"title"** som input ska programmet skriva ut primaryTitle och averageRating för filmerna vars primaryTile och originalTitle är olika. Utskriften ska vara formaterad enligt **"title:rating"**.
    - Om användaren skriver **"year"** som input ska programmet be om en till input där användaren skriver in ett årtal. Skriv sen ut originalTitle och numVotes för filmerna vars year är lika med året användaren skrev in. Utskriften ska vara formaterad enlig **"title:votes"**.

 Funktionen `analyze_text` ska enbart innehålla inputs och if-satsen för valen. Övriga funktioner ska ligga i en ny modul som du även ska skapa. Modulen ska heta `analyze_functions.py`, det ska finns minst en funktion för varje menyval. Om användaren skriver ett ej giltigt argument ska **"Not an option!"** skrivas ut.

    **Exempel**

    input:
        "year"
        "1897"
    output:
        Bataille de neige:1468
        Boulevard des Italiens:18



2. **Omvänd summering**. Fyll i funktionen `reversed_sum`, den ska ta emot två argument. Det första argument är en lista som innehåller heltal och det andra argumentet är en sträng som innehåller operatorn "+" eller "-". Du ska byta håll på vartannat element i listan, t.ex. [15, 12, 13, 14] blir [51, 12, 31, 14]. Om operatorn är ett "+" ska du summera alla talen i listan. Om operatorn är "-" ska du subtrahera det första elementet med resterande element. Returnera resultatet.

    **Exempel**

    input:
        [15, 12, 13, 14], "+"
    output:
        108
    input:
        [15, 12, 13, 14], "-"
    output:
        -6



3. **Upprepande bokstavs distans**. Fyll i funktionen `repeating_letter_distance`, den ska ta emot ett argument som är en sträng som innehåller bokstäver. Funktionen ska räkna ut hur långt det är mellan repeterande bokstäver. Den ska returnera en dictionary där bokstäverna är nycklar och distansen är värdet. Om en bokstav saknar upprepning ska den inte finnas med i dictionarien.

    **Exempel**

    input:
        "abcab"
    output:
        {'a': 3, 'b': 3}



4. **Hitta ord**. Fyll i funktionen `find_word`, den ska ta emot två till tre argument. Det första argumentet är en sträng och innehåller en text, det andra argumentet är ett heltat som representerar en läng och det sista optionella argumentet kan vara en sträng eller ett heltal. Standard värdet för det optionella argumentet är `None`. Du ska hitta alla orden med en viss längd i texten. Ett ord är bokstäverna a-Z (stora och små bokstäver).
Om det inte skickas in något optionellt argument ska du returnera det första hittade ordet.
Om det optionella argumentet är en siffra, ska du returnera det X:e hittade ordet. T.ex. om du har hittat orden "paj" och "apa" och option är 2 ska du returnera "apa".
Om det optionella argumentet är en sträng, ska du returnera det första ordet som börjar med samma sträng. T.ex. om du har hittat "paj" och "apa" och option är "a", ska du returnera "apa".

    **Exempel**

    input:
        "A third class of historians-the so-called Historians of culture-", 10
    output:
        historians

    input:
        "A third class of historians-the so-called Historians of culture-", 10, 2
    output:
        Historians

    input:
        "A third class of historians-the so-called Historians of culture-", 10, Hist
    output:
        Historians



5. **Sortera på frekvens**. Fyll i funktionen `frequency_sort`, den ska ta emot en lista som argument och listan innehåller heltal. Sortera listan på frekvensen för antalet gånger varje element är med i listan, i fallande ordning. Returnera den sorterade listan. Till denna uppgiften får du importera och använda dig av modulen/biblioteket `operator`.

    **Exempel**

    input:
        [4, 6, 2, 2, 6, 4, 4, 4, 6]
    output:
        [4, 4, 4, 4, 6, 6, 6, 2, 2]
