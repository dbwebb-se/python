Authors:
    - aar, Andreas Arnesson
    - grm, Marie Grahn
Revisions:
    - "2021-10-26": (A, aar, grm) Skapad inför HT21.


Individuell examination (try1)
==================================

Denna individuella examination består av fem uppgifter. De olika uppgifterna förklaras nedanför och varje uppgift ska lösas i filen "exam.py" i en specifik fördefinierad funktion.

Om det inte står i en uppgift att en modul ska importeras får man **inte** använda sig av importerade moduler/biblioteket.

När du rättar din kod, ha enbart `print()` och `input()` anrop i din kod där det efterfrågas av uppgiften. Annars kan det förstöra testerna.

Du kan när du vill under hela examinationen köra kommandot `dbwebb test try1` för att rätta dina lösningar och se hur många poäng du har uppnått.

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

1. **Räkna element**. Fyll i funktionen `count_elements`, den ska ta emot ett argument. Det argumentet är en sträng som innehåller en kemisk formel som beskriver vilka element och hur många av dem som utgör molekylen. Du ska räkna ut hur många av varje element som finns i formeln. T.ex. formeln för Difluordiklormetan är "CCl2F2", i  den finns 1 C, 2 Cl och 1 F. Ett element har följande uppbyggnad.

    Ett element börjar med stor bokstav och kan efterföljas av en liten bokstav. Det utgör benämningen. För att markera hur många som finns kan benämningen efterföljas av ingen siffra eller 1-99. Ingen siffra innebär 1.

    Funktionen ska returnera en dictionary där nycklarna är benämningen på elementen och värdena är hur många av dem som finns i formlen.

    Om argumentet är en tom sträng ska funktionen returnera en tom dictionary.

**Exempel**

    argument:
        "CCl2F2"
    return:
        {'C': 1, 'Cl': 2, 'F': 2}
    argument:
        "Ag"
    return:
        {'Ag': 1}



2. **Räkna ut fotbollsresultat**. Det har spelats några omgångar av damallsvenskan i fotboll. De aktuella lagen är Hammarby Dam, Eskilstuna, Kristianstad och AIK Dam. Tidningen ”Fotbollsnytt” vill ha in resultatet som ett dictionary i ett speciellt format så att det passar deras layout. 

    Fyll i funktionen `fotball_results`. Den tar emot två argument, första argumentet är en tuple som innehåller lagnamnen. Indexpositionerna för namnen funkar som id i det andra argumentet. Det andra argumentet är en lista med tupler. Varje tuple innehåller tre element; lag1 (index position för namnet i första argumentet), lag2 (index position för namnet i första argumentet) och matchresultatet. Matchresultatet `"0-1"` innebär en vinst för lag2 med 1 mål mot lag1 med 0 mål.

    Skapa en dictionary som har lagnamnen som nycklar och värdet är en ny dictionary. Den ska ha nycklarna `"scores"`, `"points"` och `"games"`. I `"scores"` ska du spara den totala målskillnaden för laget. Målskillnad är totala antalet mål laget har gjort minus antalet mål som har gjorts mot laget. I `"games"` ska du spara antalet matcher laget har spelat. I `"points"` ska du spara antalet poängen för alla matcher; en vinst är värd 3 poäng, förlust är värt 0 poäng och oavgjort är värt 1 poäng för båda lagen.

    Returnera dictionaryn med lagens resultat.

**Exempel**

    argument:
        ("Hammarby Dam", "AIK Dam"), [(1, 0, "1-2"), (1, 0, "2-0")]
    return:
        {'AIK Dam': {'scores': 1, 'points': 3, 'games': 2}, 'Hammarby Dam': {'scores': -1, 'points': 3, 'games': 2}}



3. **Delmängd är noll**. Fyll i funktionen `subset_zero`. I filen `numbers.txt` finns en nummerserie per rad. Om en nummerserie innehåller två tal som tar ut varandra, t.ex. 2 och -2, eller innehåller talet 0, så ska du skriva ut sifferserien som en lista efter följt av `"True"` annars sifferserien efterföljt av `"False"`.

    Läs igenom filen i ordningen serierna står och skriv ut True eller False för varje serie.

**Exempel**

    fil:
        0, 4, -6
        2, 6, -7, 15, 7
        11, 4, -8
    utskrift:
        [0, 4, -6] True
        [2, 6, -7, 15, 7] True
        [11, 4, -8] False



4. **Jolly Jumper**. Fyll i funktionen `jolly`. Funktionen tar ett argument, som är en lista med tal. En lista av n-tal kallas Jolly Jumper om de absoluta värdena för skillnaderna mellan varje tal alltid minskar med **1** eller är **samma** som förra. Med absolut tal tal menas att negativa tal räknas som positiva.

    T.ex. med listan [1 4 2 3] blir uträkningen:
    1 - 4 == -3 # -3 räknas som 3.
    4 - 2 == 2
    2 - 3 == -1 # -1 räknas som 1
    Listan är Jolly då skillnaden alltid minskar med 1.

    Funktionen ska returnera en sträng som innehåller skillnaderna, space separerade, efter följt av JOLLY om talen är Jolly, annars NOT JOLLY. 

**Exempel**

    argument:
        1 4 2 3
    return:
        3 2 1 JOLLY

    argument:
        5 1 4 2 -1 6
    return:
        4 3 2 3 7 NOT JOLLY



5. **Jämför banker**. Fyll i funktionen `compare_banks`. Du ska jämföra sparande mellan två banker. Bankerna representeras som varsin modul. Skapa modulerna `savingscentral.py` och `stockbank.py`. I båda moduler ska du skapa en funktion som heter `money_growth()` och tar emot två argument, som heltal; pengar och år. År parametern ska ha default värdet `10`.

    Med sparande hos **savingscentral** får man 0,78% ränta per år och det kostar inga avgifter. Med sparande hos **stockbank** får man 5,1% ränta per år och kostar en avgift på 10% av beloppet efter alla årens utveckling.

    Utvecklingen räknas ut med formlen, år * pengar * ränta.

    Fyll i respektive `money_growth()` funktion med den bankens sparande uträkning. Funktionerna ska returnera summan pengar man har tjänat eller förlorat på att spara i banken, avrundat till två decimaler.
    Om året som skickas in som argument är mindre än 0 ska funktionerna lyfta ett `ValueError`.

    I funktion `compare_banks` ska du ta emot **ett** `input()` anrop. Användaren kan antingen skriva in en sträng som innehåller en summa pengar och antalet år separerat med ett kommatecken eller bara en summa pengar. Om användaren bara skriva in en summa ska default värdet i år parametern användas. Anropa båda `money_growth()` funktionerna för att räkna ut hur mycket pengar man tjänar i de olika bankerna. Returnera en tuple där första elementet är pengarna från savingscentral och andra elementet är pengarna från stockbank.
    Om `money_growth()` funktionerna lyfter `ValueError` ska `compare_banks()` returnera en tom tuple.

**Exempel**

    input:
        "100,20"
    return:
        (15.6, 91.8)

    input:
        "50,-2"
    return:
        ()

    input:
        "-203,7"
    return:
        (-11.08, -65.22)

    input:
        "203"
    return:
        (15.83, 93.18)
