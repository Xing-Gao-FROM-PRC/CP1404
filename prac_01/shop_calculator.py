total_price = 0 
item_num = int(input("Number of items:"))
while item_num < 0:
    print("Invalid number of items!")
    item_num = int(input("Number of items:"))
for i in range (0,item_num):
    item_price = float(input("Price of item:"))
    total_price = total_price + item_price
if total_price > 100:
    total_price = total_price - total_price * 0.1
print(f"Total price for {item_num} items is $" + "{:.2f}".format(total_price))