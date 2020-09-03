"""
Skriv ett program som tar emot inmatning från användaren. 
Programmet ska sedan göra om dessa till Japanska Yen med dagens kurs: 
1 SKR = 10.81 YEN.

Programmet ska nu formaterat skriva ut hur många YEN det blir, 
samt vad 10 och
100 gånger så mycket blir.
"""
RATE = 10.81

sek = int(input("Skriv in sek: "))

yen = sek * RATE
print(str(sek) + "kr är " + str(yen) + "yen")

ten_times = sek * 10 
yen = ten_times * RATE

print(str(ten_times) + "kr är " + str(yen) + "yen")

ten_times = sek * 100
yen = ten_times * RATE

print(str(ten_times) + "kr är " + str(yen) + "yen")
