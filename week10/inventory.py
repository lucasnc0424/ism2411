#Reflection Qs: 
#1: the most intersting thing about lists is that they start counting at 0 instead of 1.
#2: My accounting projects are often tedious and one way to make them more manageable is by using lists and loops to automate repetitive tasks.

# EXERCISE 1
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

print("----------------------------------------")

# EXERCISE 2
first_item = inventory[0]
last_item = inventory[-1]
middle_item = inventory[2]

print(first_item)
print(last_item)
print(middle_item)

print("----------------------------------------")

# EXERCISE 3
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

print("----------------------------------------")

# EXERCISE 4
inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

print("----------------------------------------")

# EXERCISE 5
coords = (40.7128, -74.0060)

# coords[0] = 99  # gives typeerror because tuples cant be changed
print("Tuples are immutable so you cant change values")

print(coords)

print("----------------------------------------")

# EXERCISE 6
sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
avg = total / count
best = max(sales)
worst = min(sales)

print("Total:", total)
print("Average:", avg)
print("Best:", best)
print("Worst:", worst)

print("----------------------------------------")

# EXERCISE 7
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    new_price = round(price * 0.90, 2)
    discounted.append(new_price)

print(prices)
print(discounted)

print("----------------------------------------")

# EXERCISE 8
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for s in sales:
    if s > 300:
        high_sales.append(s)

high_count = len(high_sales)
high_avg = round(sum(high_sales) / high_count, 2)

print("High sales:", high_sales)
print("Count:", high_count)
print("Average:", high_avg)

