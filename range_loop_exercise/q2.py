rows = int (input("Enter the number of rows: "))

for row in range(1,rows + 1):
    spaces = rows - row#Number of spaces
    stars = 2 * row - 1#Number of stars
    print (" " * spaces +  "*" * stars)