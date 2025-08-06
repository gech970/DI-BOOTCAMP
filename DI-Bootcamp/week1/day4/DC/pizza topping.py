toppings = []
base_price = 10.00
topping_price = 2.50

print("Enter pizza toppings  (type 'quit' to finish):")

while True:
    topping = input("> ").strip().lower()  
    
    if topping == 'quit':
        break
    if topping: 
        print(f"Adding {topping} to your pizza.")
        toppings.append(topping)

# Calculate total
total = base_price + len(toppings) * topping_price
print("\nYour pizza toppings:")
for topping in toppings:
    print(f"- {topping}")

print(f"\nTotal cost: ${total:.2f}")