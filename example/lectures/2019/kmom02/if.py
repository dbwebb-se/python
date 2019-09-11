number_one = int(input("Siffra 1: "))
number_two = int(input("Siffra 2: "))

message = "Rejected"

if number_one > 10 and number_one < 100:
    if number_two > 10 and number_two < 100:
        if number_one < 50 or number_two < 50:
            if number_two > 40 or number_two > 40:
                message = "Approved"

print(message)
