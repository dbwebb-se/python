"""
Skriv en funktion som tar emot en lista som innehåller heltal och en (1) nivå av nestlade listor,
även dessa med heltal.

Iterera igenom listan och summera alla siffror i förälder listan.
Varje gång du stöter på en barn lista summera siffrorna i denna och skriv ut barnlistans summa.
Addera barnlistornas summa till förälderlistans totala summa.


[1, 2, 3, 4]
[1, 2, [6, 7, 8], 5, 7, 9]
[[1, 2], [6, 7, 8], [5, 7, 9], [7, 9, 13], 2]
                    
"""

def sum_child_list(numbers):
    """
    sum a list of integers
    """
    result = 0
    for number in numbers:
        result += number
    print("inne", result)
    return result

def sum_list(numbers):
    """
    Sum a list of integers which can be nestled
    """
    result = 0
    for number in numbers:
        if isinstance(number, list):
            result += sum_child_list(number)
        else:
            result += number
    print(result)

# Rekursiv lösning - överkurs
#def sum_list(numbers):
#    result = 0
#    for number in numbers:
#        if isinstance(number, list):
#            result += sum_list(number)
#        else:
#            result += number
#    print(result)
#    return result

sum_list([1, 2, 3, 4])
sum_list([1, 2, [6, 7, 8], 5, 7, 9])
sum_list([[1, 2], [6, 7, 8], [5, 7, 9], [7, 9, 13], 2])
