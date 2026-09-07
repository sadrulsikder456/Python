prices = {"mouse": 500, "keyboard": 1200, "monitor": 8500}

max_price = 0
most_expensive_item = ""

for item, price in prices.items():
    if price > max_price:
        max_price = price
        most_expensive_item = item

print(f"the most expensive item is {most_expensive_item} and the price is {max_price}")


# prices = {'Mouse': 500, 'Keyboard': 1200, 'Monitor': 8500, 'Headphone': 1500}

# max_price = 0
# most_expensive_item = ""


# for item, price in prices.items(): # .items() diye key ar value eksathe pawa jay
#     if price > max_price:
#         max_price = price
#         most_expensive_item = item

# print(f"The most expensive item is {most_expensive_item} costing {max_price}")
