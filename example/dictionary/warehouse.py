#!/usr/bin/env python3

"""
Code examples for dictioanries
"""

from operator import itemgetter

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

for key in sorted(warehouse.keys()):
    print(key, warehouse[key])

for key, value in sorted(warehouse.items(), key=itemgetter(1), reverse=True):
    print(key, value)

warehouse_deluxe = {
    "köttfärs" :{"stock" : 20, "price" : 50},
    "grädde" :{"stock" : 80, "price" : 20},
    "krossade tomater" :{"stock" : 33, "price" : 10},
    "gul lök" :{"stock" : 42, "price" : 5}
}

for key in sorted(warehouse_deluxe.keys()):
    print(key, warehouse_deluxe[key]["price"])

warehouse_deluxe = {
    "köttfärs" :{"stock" : 20, "price" : 50, "ids" : (1234, "K14")},
    "grädde" :{"stock" : 80, "price" : 20, "ids" : (3141, "L12")},
    "krossade tomater":{"stock" : 33, "price" : 10, "ids" : (4224, "E13")},
    "gul lök" :{"stock" : 42, "price" : 5, "ids" : (2742, "D02")}
}

warehouse_deluxe["röd lök"] = {}
warehouse_deluxe["röd lök"]["stock"] = 7
warehouse_deluxe["röd lök"]["price"] = 9
warehouse_deluxe["röd lök"]["ids"] = (6314, "D04")

for key in sorted(warehouse_deluxe.keys()):
    print("{product} costs {price} and we have {stock} in stock. It has barcode {barcode} and stock id {stock_id}."\
          .format(
              product=key,
              price=warehouse_deluxe[key]["price"],
              stock=warehouse_deluxe[key]["stock"],
              barcode=warehouse_deluxe[key]["ids"][0],
              stock_id=warehouse_deluxe[key]["ids"][1]
          ))
