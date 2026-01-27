# 4.	Ask the user for
# •	number of pizzas (int)
# •	price per pizza (float, dollars)
# •	tip percent (float; e.g., 15 for 15%)
# •	number of people sharing (int)

# Calculate and print: subtotal, tip amount, total, and amount per person.
# Formatting currency to 2 decimals. Display appropriate inputs and outputs.

#get number of pizzas, price of pizza, tip percent, and number of people
pizzas = int(input("How many pizzas? "))
price_each = float(input("Price per pizza ($): "))
tip_percent = float(input("Tip percent (e.g., 15 for 15%): "))
people = int(input("How many people sharing? "))

#calculate subtotal tip amount, total, and amount per person
subtotal = pizzas * price_each
tip = subtotal * (tip_percent / 100)
total = subtotal + tip
per_person = total / people

#display  subtotal tip amount, total, and amount per person
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tip: ${tip:.2f}")
print(f"Total: ${total:.2f}")
print(f"Each person pays: ${per_person:.2f}")