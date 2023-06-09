"""
get number of items, price of items
total price = total price + price of item
if total price > 100
    total price = total price * 0.1
display Total price for all items is total price
"""

number_of_items = int(input("How many items? "))
while number_of_items < 0:
    print("invalid number of items")
    number_of_items = int(input("How many items? "))
total_price = 0
for i in range(number_of_items):
    price_of_item = float(input("Price of Item: "))
    total_price = total_price + price_of_item
if total_price > 100:
    total_price = total_price - total_price * 0.1
print(f"Total price for {number_of_items} items is {total_price:.2f}")
