# Skriv ett program som tar emot inmatning från användaren. Programmet ska ta emot antal svenska kronor.
sek = float(input("Enter amount to convert in sek: "))
# Programmet ska sedan göra om dessa till Japanska Yen med dagens kurs: 1 SKR = 10.81 YEN.
RATE = 10.81
yen = sek * RATE
# Programmet ska nu formaterat skriva ut hur många YEN det blir,
print(str(sek) + " is " + str(yen) + "yen")
#  samt vad 10 och
print(str(sek * 10)
    + " is "
    + str(yen * 10)
    + "yen")
#  100 gånger så mycket blir.
sek_converter_to_yen = (str(sek * 100)
    + " is "
    + str(yen * 100)
    + "yen")
print(sek_converter_to_yen)
