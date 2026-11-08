#customers.py
#Lucas Cunningham
#Module 11 lab: Lab customer Dictionary lineups

from os import name


print("---Exercise 1 ---")
customer = {
    "name": "Lucas Cunningham" , #Key : value,
    "email": "lucascn0424@gmail.com" , 
    "tier": "Gold" , 
    "ytd_spend" : 12400,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print("---Exercise 2 ---")
customer['phone'] = '555-5555'# Adding a new key-value pair to the dictionary
print(customer)
customer['tier']  =  'platinum'
print(customer)
del customer ['name']
print(customer)

print(customer.get('ytd_spend', 0))
print("---Exercise 3 ---")
print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError as error:
    print("Email not found", error)
print("---Exercise 4 ---")
for key, value in customer.items():
    print(f"{key}: {value}")
for key in customer:
    print(key)
for something in customer: 
    print(something, customer[something])
print("---Exercise 5 ---")
tier_discounts = {
    "bronze": 0,
    "silver": .05,
    "gold": .1,
    "platinum": .15,
}

purchase = 200
discount_rate = tier_discounts.get(customer['tier'], 0)
final_price = purchase * (1 - discount_rate)
print(f"Tier:{customer['tier']}")
print(f"Discount Rate: {discount_rate * 100}%")
print(f"Final Price: {final_price:.2f}")

print("---Exercise 6 ----")
customers = [
    {"name": "bob", "tier": "silver", "ytd_spend": 5000},
    {"name": "alice", "tier": "gold", "ytd_spend": 10000},
    {"name": "charlie", "tier": "bronze", "ytd_spend": 2000}

]


for record in customers:
    rate = tier_discounts.get(record['tier'], 0)
    discount = 300 * rate
    print(f"{record['name']} ({record['tier']}): ${discount:.2f} off a $300 purchase")

print("---Exercise 7 ---")
catalog = {
    "Widget A": {'price': 9.99, "Stock": 150},
    "Widget C": {'price': 49.99, 'stock': 8}

}

for name, details in catalog.items():
    if details ["stock"] < 20:
        print(f"LOW STOCK: {name}- only {details['stock']} left")

print("---Exercise 8 ---")

trasactions = [
    {"region": "South", "amount": 300}
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},

]

sales_by_region = {}
for sale in transactions:
    region = sale['region']
    amount = sale['amount']
    sales_by_region [region] = sales_by_region.get (region, 0) + amount

    print(sales_by_region)
    for region in sorted (sales_by_region):
        print(f"{region}: {sales_by_region[region]}")