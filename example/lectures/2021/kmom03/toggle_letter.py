"""
Skapa två funktioner, en funktion ska ta emot ett argument (en karaktär)
 och kolla om det är en versal. Om det inte är det ska den göra om den
 till en versal och returnera den. Om det redan är en versal ska den
 göras om till en gemen och returneras. 
 Lägg denna funktionen i en egen fil. 
 Tips, använd isupper(), upper() och lower().

Den andra funktionen ska ta en input där användare kan skriva in 
ett meddelande. Meddelandet ska göras om så att versaler blir 
gemeners och gemenr blir versaler, använd den andra funktionen 
för att göra om varje bokstav, och sist skriva ut det omgjorda 
meddelandet till skärmen. Lägg denna funktionen i en annan fil. 
I denna filen importera den första. 
Använd if __name__ == "__main__" för att anropa funktionen som
startar programmet.

Ex: input: "TjeNa MittBEna" output: "tJEnA mITTbeNA" 
"""

def switch_case(letter):
    """
    Change upper to lower and lower to upper
    """
    # return letter.lower() if letter.isupper() else letter.upper()
    if letter.isupper():
        return letter.lower()
    return letter.upper()
