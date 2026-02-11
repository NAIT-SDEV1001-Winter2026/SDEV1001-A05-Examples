sum = 0
my_square = int(input("Enter a number to sum the squares: "))

for number in range (1,my_square + 1):
    sum += number ** 2

print(f"The sum of squares is {sum}")