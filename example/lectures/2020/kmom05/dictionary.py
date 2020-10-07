"""
Example of sorting and merging two dictionaries
"""
from operator import itemgetter

# def id_to_key(id, warehouse):
#     for item in warehouse.items():
#         if id == item[1]["ids"][0]:
#             return (item[0], item[1])

# def sort_by_price(prices, warehouse):
#     sorted_prices = sorted(prices.items(), key=itemgetter(1), reverse=True)
#     for id_, price in sorted_prices:
#         key, data = id_to_key(id_, warehouse)
#         print(f"{key} kostar {price}, det finns {data['stock']} kvar på hyllplats {data['ids'][1]}")


def merge(prices, warehouse):
    """
    Merge two dictionaries into list with tuples
    """
    everything = []
    for name, item in warehouse.items():
        everything.append((
            name,
            item,
            prices[item["ids"][0]]
        ))
    print(everything)
    return everything

def sort_by_price(everything):
    """
    Sort data on price
    """
    sorted_prices = sorted(everything, key=itemgetter(2), reverse=True)

    for name, data, price in sorted_prices:
        print(f"{name} kostar {price}, det finns {data['stock']} kvar på hyllplats {data['ids'][1]}")


def main():
    """
    Start of program
    """
    prices = {
        1234: 50,
        4224: 10,
        3141: 20,
        2742: 5,
    }

    warehouse = {
        "köttfärs" : 
            { 
                "stock" : 20,
                "ids" : (
                    1234, "K14"
                ) 
            },
        "grädde" : 
            {
                "stock" : 80,
                "ids" : (
                    3141, "L12"
                ) 
            },
        "krossade tomater": {"stock" : 33, "ids" : (4224, "E13")},
        "gul lök" :{"stock" : 42, "ids" : (2742, "D02")}
    }
    # sort_by_price(prices, warehouse)

    everything = merge(prices, warehouse)
    sort_by_price(everything)

if __name__ == "__main__":
    main()
