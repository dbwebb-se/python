Authors:
    - aar, Andreas Arnesson
    - efo, Emil Folino
Revisions:
    - "2018-10-03": (B, efo) Genomläsning och precisering.
    - "2018-09-05": (A, efo, aar) individuella examinationen 2018-lp1.


Individuell examination (try1)
==================================

Denna individuella examination består av fem uppgifter. De olika uppgifterna förklaras nedanför och varje uppgift ska lösas i filen "exam.py" i en specifik fördefinierad funktion.

För alla uppgifter du löser, uppdatera funktionens docstring (kommentaren längst upp i funktionen) till en relevant kommentar om vad funktionen gör.

Du kan när du vill under hela examinationen köra kommandot `dbwebb exam correct try1` för att rätta dina lösningar och se hur många poäng du har uppnått.

Utöver att lösa uppgifterna behöver du se till att alla filer valideras med `dbwebb validate try1`.

Du har 5 timmar på dig att lösa uppgifterna och publicera dina lösningar med kommandot `dbwebb exam seal try1` inom tidsramen. Den sista `seal` som görs inom tidsramen är den som kommer användas som betygsunderlag.

**För att få godkänt på examinationen måste du klara uppgift 1.**

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

1. **Analysera text**. Denna uppgiften går ut på att du ska analysera textfilen "value-of-time.txt" på 3 olika sätt. Funktionen `analyze_text` ska innehålla en while-loop som tar emot input från användaren. Loopen ska avslutas om användaren skriver "q" eller "quit", när programmet avslutas ska funktionen returnera sant, `True`.

 De tre olika sätten texten ska analyseras på är:
    - Om användaren skriver "s" eller "spaces" som input ska antalet mellanrum skrivas ut med `print()`. Skriv enbart ut siffran, ingen extra text.
    - Om användaren skriver "l" eller "letters" som input ska antalet bokstäver (a-z, A-Z) skrivas ut med `print()`. Skriv enbart ut siffran, ingen extra text.
    - Om användaren skriver "c" eller "specials" som input ska antalet speciella tecken som finns i paragrafen med flest special tecken skrivas ut med `print()`. Skriv enbart ut siffran, ingen extra text. En paragraf är ett stycke av text som avgränsas med minst ett radbrytningstecken. Speciella karaktärer i detta sammanhanget är: `(),".:-'?`.<br><br>

 Funktionen analyze_text ska enbart innehålla while-loopen som tar inputs och if-satsen för valen. Övriga funktioner ska ligga i en ny modul som du även ska skapa. Modulen ska heta `analyze_functions.py`, det ska finns minst en funktion för varje menyval, utom valet "q". Om användaren skriver ett ej giltigt argument ska "Not an option!" skrivas ut. Gör inga extra `print()` i din lösning förutom de som efterfrågas i kravspecifikationen.

2. **Validera mobilnummer**. Den här uppgiften går ut på att du ska validera om en sträng är ett giltigt mobilnummer. Ett giltigt mobilnummer följer formatet "xxx-xxx xx xx" där de tre första siffrorna (de tre första x) måste vara något av följande: 070, 072, 073, 076 eller 079. Sedan ska det följa ett bindestreck och sju siffror 0-9 enligt formateringen ovan med tre siffror, ett mellanslag, två siffror, ett mellanslag och två siffror. Din funktion ska returnera sant, True, eller falskt, False, beroende på om strängen är ett korrekt formaterat mobiltelefonnummer.

3. **Verifiera kreditkort**. Fyll i funktionen `verify_credit_card`. Funktionen ska ta emot ett argument som är en sträng på 16 heltal och returnera True eller False. Ett korrekt kreditkortsnummer uppfyller följande krav:
    - Sista siffran är vår kontrollsiffra.
    - Ta resten av sekvensen och dubbla varannan siffra.
    - Om ett tal blir störren än 9 räkna ut dess tvärsumma/siffersumma dvs. summera talets siffror. Exempel, 12 -> 1 + 2 = 3
    - Addera ihop alla siffror.
    - Multiplicera talet med 9.
    - Jämför sista siffran i talet med kontrollsiffran, om de är lika är det ett giltigt kreditkort.<br><br>

 Exempel kontroll:
    - Input är 38520000023237.
    - Kontroll siffra 7.
    - Resten av sekvensen är 3852000002323.
    - Dubblering av siffrorna, 6,8,10,2,0,0,0,0,0,2,6,2,6
    - Tvärsummering av 10 -> 1 + 0 = 1.
    - Addera alla siffror, 6+8+1+2+0+0+0+0+0+2+6+2+6 = 33.
    - Multiplicera med 9, 33 * 9 = 297.
    - 7 == 7, dvs. ett godkänt kreditkortsnummer.<br><br>

4. **Hitta differensen**. Fyll i funktionen `find_difference`, den ska ta två listor som argument och listorna innehåller strängar. Hitta alla element som endast finns i en av listorna och returnera en lista med de värden. I den returnerade listan ska varje element bara vara med en gång. Din lösning ska vara case-insensitive, dvs. a == A. Listan som returneras ska vara sorterad i bokstavsordning.

5. **Analysera datum och tider**. Den här uppgiften går ut på at du ska ska plocka ut giltiga datum och tider från texten i filen "value-of-time.txt". Funktionen `validate_date_time` ska innehålla en while-loop som tar emot input från användaren. Loopen ska avslutas om användaren skriver "q" eller "quit", när programmet avslutas ska funktionen returnera sant, True. Gör inga extra `print()` i din lösning förutom de som efterfrågas i kravspecifikationen.
    - Om användaren skriver "d" eller "date" som input ska alla korrekta datum i filen skrivas ut med `print()`. Separera alla datum med ", ". Där ska inte vara något ", " sist i utskriften.
    - Om användaren skriver "t" eller "time" som input ska alla korrekta tider skrivas ut med `print()`. Separera alla datum med ", ". Där ska inte vara något ", " sist i utskriften.<br><br>

 Funktionen `validate_date_time` ska enbart innehålla while-loopen som tar inputs och if-satsen för valen. Övriga funktioner ska ligga i en ny modul som du även ska skapa. Modulen ska heta `date_time_functions.py`, det ska finns minst en funktion för datum och en för tid. Om användaren skriver ett ej giltigt argument ska "Not an option!" skrivas ut.
    Ett giltigt datum följer [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, dvs. yyyy-mm-dd, ex. 2018-09-05. Ni kan räkna med att alla månader har 31 dagar.
    En giltig tid följer formatet hh:mm, ex. 08:09.
