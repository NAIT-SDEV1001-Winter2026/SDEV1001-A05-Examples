# 2.	Write a program that asks the user to enter three test scores. The program should display each test score, as well as the average test of the users' scores.

# Output:
# Enter the first test score: 10
# Enter the second test score: 20
# Enter the third test score: 30
# Test Score 1: 10.0
# Test Score 2: 20.0
# Test Score 3: 30.0
# Average Score: 20.0

#get three numbers
score1 = float(input("Enter the first test score: "))
score2 = float(input("Enter the second test score: "))
score3 = float(input("Enter the third test score: "))

#show three numbers
print (f"Test Score 1: {score1}")
print (f"Test Score 2: {score2}")
print (f"Test Score 3: {score3}")

#calculate average
average = (score1 + score2 + score3) / 3

#display average
print(f"Average Score: {average}")




