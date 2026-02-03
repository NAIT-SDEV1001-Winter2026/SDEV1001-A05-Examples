# 5.	Create file named package_selector.py in this folder. Write a program for a gym so that it can determine which membership package a person should purchase. There are three packages:
# Package A: $40/month, 4 months
# Package B: $55/month, 8 months
# Package C: $75/month, 12 months
# Package D: $100/month, 12 month Note: ensure you have the words "You have selected Package A" or which ever package you select

package = input("Enter the package letter (A/B/C/D): ")

is_valid = True

match package.upper():
    case "A":
        monthly_fee = "$40"
        total_fee = "$160"
    case "B":
        monthly_fee = "$55"
        total_fee = "$440"  
    case "C":
        monthly_fee = "$75"
        total_fee = "$900"   
    case "D":
        monthly_fee = "$100"
        total_fee = "$1200"
    case _:
        is_valid = False
        print("Invalid package")

if is_valid:
    print(f"You have selected Package {package}")
    print(f"Your monthly fee is {monthly_fee}")
    print(f"Your total fee is {total_fee}")

#if an invalid package was entered, display an error message and DO NOT display the package, monthly fee and total fee