#!/usr/bin/env python3

warehouse = {
    "köttfärs" : 20,
    "grädde" : 80,
    "krossade tomater": 33,
    "gul lök" : 42
}

print(warehouse["krossade tomater"])

warehouse["krossade tomater"] = 58

warehouse["röd lök"] = 7

print(warehouse)

for key, value in warehouse.items():
    print(key, value)
