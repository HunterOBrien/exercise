# find amount of items the person has
item_count = int(input("How many items do you have:"))
GST = 0.15

while item_count > -1:
   item_count = item_count - 1
item = float(input("Enter item price here: "))
item_GST = item * GST
item_cost = item + item_GST
print("Total cost:", item_cost)

