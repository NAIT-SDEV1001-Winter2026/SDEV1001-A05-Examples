#While loops repeat a block of code while a condition is True
#Useful whn you don't know how many times to loop before the loop

#Counter controlled loop
#print 1 to 5
counter = 1
while counter <=5:
    print(counter)
    counter += 1

#Use controlled loop
#Ask the user for numbers to add. Enter 'done' to print the sum

# sum  = 0
# while True:#An endless loop unless break
#     value = input("Enter a number. done to quit: ")
#     if value.lower() == "done":
#         break
#     sum += int(value)
# print(f"Sum: {sum}")

#without break
# sum  = 0
# value = ""
# while value != "done" :
#     value = input("Enter a number. done to quit: ")
#     if value.lower() != "done":        
#         sum += int(value)
# print(f"Sum: {sum}")

#With a boolean
# sum  = 0
# is_done = False
# while not is_done:
#     value = input("Enter a number. done to quit: ")
#     if value.lower() != "done":        
#         sum += int(value)
#     else:
#         is_done = True
# print(f"Sum: {sum}")

#Another boolean loop
keep_going = True
while keep_going:
    #Something really cool!! :)
    response = input("That was fun! Would you like quit now?(q) ")
    if response.lower() == "q":
        keep_going = False
print("Loop over! Have a groovy day!")

