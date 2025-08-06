sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]
finished_sandwiches = []
print("The deli has run out of Pastrami!")
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")
print("\nPreparing sandwiches:")
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")


        
           