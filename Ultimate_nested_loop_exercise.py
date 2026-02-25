import random
numbers = []
# while len(numbers) < 100:
#     number = random.randint(1,1000)
#     if number not in numbers:
#         numbers.append(number)
# #OR
for count in range(1,100):
    is_unique = False
    while not is_unique:
        number = random.randint(1,1000)
        if number not in numbers:
            numbers.append(number)
            is_unique = True

print(f"Origional: {numbers}")
numbers = [3,1,55,31,2]
list_length = len(numbers)
count = 0
#outer loop controls the number of passess
for start in range(0,list_length -1):
    swapped = False
    #go from the end to the start
    for index in range (list_length-1, 0,-1):
        if numbers[index-1] > numbers[index]:
            temp =numbers[index -1]
            numbers[index-1] = numbers[index]
            numbers[index] = temp
            swapped = True
            count += 1
        if not swapped:
            break
print (f"{count} swaps were performed")
print(f"Sorted: {numbers}")