"""
Sort on price and merge data
"""
from operator import itemgetter

def id_to_key(id_, warehouse):
    """
    match key from prices to id in warehous and return key and data.
    """
    for key, data in warehouse.items():
        if id_ == data["ids"][0]:
            return key, data
    return None

def sort_by_price(prices, warehouse):
    """
    sort prices and print data based on sort
    """
    sorted_prices = sorted(prices.items(), key=itemgetter(1), reverse=True)
    for id_, price in sorted_prices:
        name, data = id_to_key(id_, warehouse)
        print(
            f"{name} kostart {price}, det finns {data['stock']} kvar på hyllplats {data['ids'][1]}"
        )

if __name__ == "__main__":
    prices_dict = {
       1234: 50,
       4224: 10,
       3141: 20,
       2742: 5,
    }
    warehouse_deluxe = {
       "köttfärs" : { "stock" : 20, "ids" : (1234, "K14") },
       "grädde" : { "stock" : 80, "ids" : (3141, "L12") },
       "krossade tomater": { "stock" : 33, "ids" : (4224, "E13") },
       "gul lök" : { "stock" : 42, "ids" : (2742, "D02") }
    }
    sort_by_price(prices_dict, warehouse_deluxe)
