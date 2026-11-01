#Reflection Qs: 
#1: the most intersting thing about lists is that they start counting at 0 instead of 1.
#2: My accounting projects are often tedious and one way to make them more manageable is by using lists and loops to automate repetitive tasks.



# EXERCISE 1
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

print("-" * 40)

# EXERCISE 2
first_item = inventory[0]
last_item = inventory[-1]
middle_index = len(inventory) // 2
middle_item = inventory[middle_index]

print(first_item)
print(last_item)
print(middle_item)

print("-" * 40)

# EXERCISE 3
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

print("-" * 40)

# EXERCISE 4
inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

print("-" * 40)

# EXERCISE 5
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("TypeError caught: Tuples are immutable, which prevents accidental modification of coordinate values.")

print(coords)

print("-" * 40)

# EXERCISE 6
sales = [100, 250, 75, 480, 200]

total_sales = sum(sales)
count_sales = len(sales)
avg_sales = total_sales / count_sales
best_day = max(sales)
worst_day = min(sales)

print(f"Total: {total_sales} | Average: {avg_sales} | Best: {best_day} | Worst: {worst_day}")

print("-" * 40)

# EXERCISE 7
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    discounted.append(round(price * 0.90, 2))

print(prices)
print(discounted)

print("-" * 40)

# EXERCISE 8
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

high_count = len(high_sales)
high_avg = round(sum(high_sales) / high_count, 2)

print(f"{high_sales} | Count: {high_count} | Avg: {high_avg}")