attende = ""
attendees = []
while True:
    attende = input("Enter name: ")
    if attende == "done":
        break
    attendees.append(attende)

# print("alla:")
# for name in attendees:
#     print(name, end=", ")

# for name in attendees[::2]:
#     print(name, end=", ")

# print("vartannan")
# print(", ".join(attendees[::2]))
# print(*attendees[::2], sep=", ")
# 
# print("tre sista:")
# for name in attendees[-3:]:
#     print(name, end=", ")
# 
# print("plats 3 och 4:")
# for name in attendees[2:4]:
#     print(name, end=", ")
