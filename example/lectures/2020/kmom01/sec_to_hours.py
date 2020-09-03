"""
Gör ett program där användaren kan skriva in ett antal sekunder. Konvertera sekunderna till timmar och överblivna sekunder och skriv ut resultatet.
"""

tot_sec = int(input("Hur mångar sekunder har du?"))

hours = str(tot_sec // (60*60))
sec = str(tot_sec % (60*60))

print(str(tot_sec) + " seconds is " + hours + " hours and " + sec + " seconds")