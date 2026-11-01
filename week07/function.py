#Reflection
#Question 1: I instantly spotted the red squiggly line error as thats a dead giveaway that somethings wrong. It tells me that 
#my first instinct is to just read the code from top to bottom and look for obvious errors
#2. Function takes the origional price and a customers discount tier level and calculates it, applys to origonal amount.
#3. I used Ai to scan the code for example 5 to find errors after I couldnt find any more, it helped me find the last error, this assignment was done all in the class on monday so no Ai was used for this portion of the assignment.







# --- Excercise 1 ---
def calculate_tax(price, rate):
    return price * rate

#calling function 

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"tax fo $350 at 5%: ${calculate_tax(350, 0.05):.2f}")

#--- excercise 2 ---
#EXAM

def apply_discount(price, tier):
    if tier =="gold":
        return price *0.85
    elif tier =="silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

#excercise 3---

original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

#excercise 3---

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount (price, discount_tier)
    tax = calculate_tax (discounted_price, tax_rate)
    return discounted_price + tax

#calling the final_price function
print(f"final_price(200, 0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")

#excersice 4---

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]
rate = 0.07
for price, tier in orders:
    total = final_price(price, rate, tier)

    print(f"Order for ${price} with {tier} discount: ${total:.2f}")

    #excercise 6--

    x = 100 #global  
    def double_it():
        x= 999 # local x 
        return x * 2 
    print(x)
    print(double_it())
    print(x)
