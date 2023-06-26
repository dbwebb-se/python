"""
inmatning antal svenska kronor från användaren. 
omvandla  till Japanska Yen, kurs: 1 SKR = 10.81 YEN.

skriva ut hur många YEN, 
samt 10 och 100 gånger så mycket
"""
sek = float(input("Skriv in hur många svenska kronor: "))

sek_to_yen_course = 10.81
yen = sek * sek_to_yen_course

print(f"{sek} svenska kronor är {yen} yen")
print(f"{sek * 10} svenska kronor är {yen * 10} yen")
print(f"{sek*100} svenska kronor är {yen*100} yen")
