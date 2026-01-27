# 5.	Ask the user for a currency amount and display the number of dollars, quarters, dimes, nickels, and pennies in that amount. Display appropriate inputs and outputs.

#get amount 
amount = float(input("Enter a dollar amount (e.g. 3.87): ")) #3.87
#convert amount to all cents
cents = int(amount * 100)#387

#calculate dollars
dollars = cents // 100 #3
remainder = cents % 100 #87

#calculate quarters
quarters = remainder // 25 #3
remainder = remainder % 25 #12

#calculate dimes
dimes = remainder // 10 #1
remainder = remainder % 10 #2

#calculate nickels
nickels = remainder // 5 #0
remainder = remainder % 5 #2

#calculate pennies
pennies = remainder #2

#Display results
print("Coin Breakdown:")
print("Dollars:", dollars)
print("Quarters:", quarters)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", pennies)




 