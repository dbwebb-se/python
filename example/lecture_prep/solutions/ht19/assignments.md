Authors:
    - aar, Andreas Arnesson
    - efo, Emil Folino
Revisions:
    - "2018-06-28": (A, aar) prep assignments from lecture. 



Uppgifter
---------------------------------

1. **Analysera text**. Den här uppgiften går ut på att du ska analysera textfilen "myths.txt" på 2 olika sätt. `analyze_text` funktionen ska innehålla en while-loop som tar emot input från användaren. Loopen ska avslutas om användaren skriver "q" eller "quit", när programmet avslutas ska funktionen returnera sant, `True`.
De två olika sätten texten ska analyseras på är:
    - Om användaren skriver "s" som input ska antalet meningar som finns i varje paragraph beräknas. Skriv ut antalet meningar som finns i de tre paragrafer som har flest meningar. Skriv ut med `print()`. Skriv enbart ut siffran sorterad från högst till lägst, ingen extra text.
    - Om användaren skriver "g" som input ska du räkna hur många gånger gudarnas namn nämns i varje paragraf. För topp tre paragrafer skriv ut antalet gånger gudarna nämns, skrivas ut med `print()`. Skriv enbart ut siffran, sorterad från högst tilllägst, ingen extra text. följande gudar finns i texten, "Odin,Thor,Hödur,Baldur,Tyr,Heimdall,Vidar,Vali,Loki,Frigga,Freya,Nanna,Iduna,Sif,Modi,Magni".

 Funktionen analyze_text ska enbart innehålla while-loopen som tar inputs och if-satsen för valen. Övriga funktioner ska ligga i en ny modul som du även ska skapa. Modulen ska heta `analyze_functions.py`, det ska finns minst en funktion för varje menyval, utom valet "q". Om användaren skriver ett ej giltigt argument ska "Not an option!" skrivas ut. Gör inga extra `print()` i din lösning förutom de som efterfrågas i kravspecifikationen. En paragraf separeras med två "\n".

2. **Kontrollera HEX-koder**. Fyll i funktionen `verify_hex`, den ska ta emot ett argument, en sträng. Funktionen ska sedan kontrollera om strängen är en giltig hex-kod för en färg. Funktionen ska returnera sant, True, om hex-koden är giltig, annars falskt, False.

 För att en sträng kan godkännas gäller följande krav:
    - Strängen börjar med en brädgård '#'.
    - Strängen består sedan av 3 eller 6 hexadecimala siffror 0-f.
    - Alla bokstäver ska vara små bokstäver.<br><br>
