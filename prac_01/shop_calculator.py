discount_threshold= 100
discount_rate=0.10

total_price=0

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    price=float(input("Price: "))
    total_price+=price

if total_price>discount_threshold:
    total_price=total_price*(1- discount_rate)

print(f"Total price for {number_of_items} items: ${total_price:.2f}")