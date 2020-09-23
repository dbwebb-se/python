inp = ""
attendees = []
while True:
    inp = input("Enter name: ")
    if "extended" in inp:
        names = inp.split(":").split(",")
        attendees.extend(names)
    elif "index" in inp:
        try:
            index = attendees.index(inp.split(" ")[1])
            print(inp, "has index", index)
        except ValueError:
            print(inp, "is not attending the movie")

    elif inp != "done":
        attendees.append(inp)
    else:
        break

print("alla:")
print(", ".join(attendees))

print("vartannan")
print(*attendees[::2], sep=", ")

print("tre sista:")
for name in attendees[-3:]:
    print(name, end=", ")

print("plats 3 och 4:")
for name in attendees[2:4]:
    print(name, end=", ")
