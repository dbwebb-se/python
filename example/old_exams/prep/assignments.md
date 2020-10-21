Authors:
    - aar, Andreas Arnesson
    - efo, Emil Folino
Revisions:
    - "2020-10-06": (B, aar) Uppdaterad med nya räddningsprogrammet för HT20.
    - "2018-06-28": (A, efo) individuella examinationen 2018-lp1.


Individuell examination (prep)
==================================

Denna individuella examination består av fem uppgifter. De olika uppgifterna förklaras nedanför och varje uppgift ska lösas i filen "exam.py" i en specifik fördefinierad funktion.


Du kan när du vill under hela examinationen köra kommandot `dbwebb exam correct prep` för att rätta dina lösningar och se hur många poäng du har uppnått.

Utöver att lösa uppgifterna behöver du se till att alla filer validera med `dbwebb validate prep`.

Du har 5 timmar på dig att lösa uppgifterna och publicera dina lösningar med kommandot `dbwebb exam seal prep` inom tidsramen. Den sista `seal` som görs inom tidsramen är den som kommer användas som betygsunderlag.

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

1. **Analysera text**. Den här uppgiften går ut på att du ska analysera textfilen "manifesto.txt" på 3 olika sätt. `analyze_text` ska innehålla en while-loop som tar emot input från användaren. Loopen ska avslutas om användaren skriver **"q"** eller **"quit"**.
De tre olika sätten texten ska analyseras på är:
    - Om användaren skriver **"v"** som input ska antalet vokaler skrivas ut med `print()`.
    - Om användaren skriver **"p"** som input ska antalet punkter (".") skrivas ut med `print()`. Skriv enbart ut siffran, ingen extra text.
    - Om användaren skriver **"u"** som input ska antalet stora bokstäver skrivas ut med `print()`. Skriv enbart ut siffran, ingen extra text.

 Funktionen `analyze_text` ska enbart innehålla while-loopen som tar inputs och if-satsen för valen. Övriga funktioner ska ligga i en ny modul som du även ska skapa. Modulen ska heta `analyze_functions.py`, det ska finns minst en funktion för varje menyval, utom valet "q". Om användaren skriver ett ej giltigt argument ska **"Not an option!"** skrivas ut. Din kod **måste** ha två input() anrop, en för menyvalet och en efter resultatet har skrivits ut, som i Marvin och analyzer.
 
    **Exempel**

    input:
        "v"
    output:
        270



2. **Hitta medianen**. Fyll i funktionen `list_median`, den ska hitta medianen av värdena som finns i listan som ska skickas som argument till funktionen. Medianen är det värde, för en ordnad lista, som delar listan i två lika stora delar. Om listan innehåller ett jämnt antal element är medianen medelvärdet av de två tal som ligger i mitten av listan, **sorterad**. Du kan anta att värdena som skickas som argument endast innehåller heltal. Din funktion ska returnera medianen av listan och värdet ska max ha en decimal. Ni får **inte** importera moduler från Pythons standard bibliotek för att lösa uppgiften.

    **Exempel**

    input:
        [0, 1, 2, 4, 5]
    output:
        2
    input:
        [2, 1, 4, 5, 3, 2]
    output:
        2.5



3. **Hitta dubbletter**. Fyll i funktionen `find_duplicates`, den ska ta en lista som argument och listan innehåller strängar. Hitta alla dubbletter och returnera en lista med värden som är dubbletter. I den returnerade listan ska varje dubblett endast vara med **en gång**. Din lösning ska vara case-insensitive, dvs. `a == A`. Listan som returneras ska vara **sorterad** i bokstavsordning.

    **Exempel**
    input:
        ["hej", "hopp"]
    output:
        []
    input:
        ["hej", "hopp", "hej"]
    output:
        ["hej"]



4. **Kolla datatyper**. Fyll i funktionen `types`, den ska ta emot en lista som argument. Den listan kan innehålla ett godtyckligt antal element av tre olika datatyper. De möjliga datatyperna är heltal, strängar och listor. Funktionen ska returnera en sträng som byggs upp av beroende på de olika elementen som finns i argumentet. Beroende på datatypen gör följande:
    - **Heltal**, lägg till strängen **"The square of i is x."**, där "i" är heltalet och "x" är `i^2`.
    - **Sträng**, lägg till strängen **"The secret word is s."**, där "s" är strängen.
    - **Lista**, lägg till strängen **"The list contains x, y, z."**, där "xyz" är värden från listan. Listan kan innehålla en odefinierad mängd värden. Du kan anta att elementen är av datatypen sträng.

 Den returnerade strängen ska innehålla mellanrum mellan de olika strängar som har byggts ihop. Om argumentet är en tom lista ska funktionen returnera en tom sträng. 

    **Exempel**
        input:
            [2, "hej", ["tre", "fyra", "fem"]]
        output:
            "The square of 2 is 4. The secret word is hej. The list contains tre, fyra, fem.".
 
 

5. **Validera email adresser**. Fyll i funktionen `validate_email`, den ska validera en email adress. Funktionen ska returnera sant, **True**, om adressen är giltig, annars falskt, **False**.

 Följande regler gäller:
    - innehåller endast ett "@".
    - det ska finnas minst en karaktär framför "@".
    - efter @, ska det finnas minst en punkt, ".", och andra karaktärer framför respektive punkt.
    - efter den sista punkten ska det finnas 2 eller 3 karaktärer.
    - innehåller endast karaktärerna a-z och 0-9 samt ".", "_", "-", "@".
    - endast små bokstäver.

    **Exempel**
    input:
        "ab_c@dbwebb.com"
    output:
        True
    input:
        "abc@.com"
    output:
        False
