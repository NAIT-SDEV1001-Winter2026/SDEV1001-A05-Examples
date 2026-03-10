
print("\n🏁 Race Time Analyzer\n")

# Ask for number of races (integer > 0), with validation
while True:
    #get user input
    races = input("How many races are there? ")
    try:
        #attempt to cast the number of races to an integer
        #if it fails jump to except
        num_races = int(races) #attempt to cast the number of races to an integer
        if num_races > 0:            
            break#if valid then break out of the input loop
        else:
            print("Please enter an integer greater than 0.\n")           
    except ValueError:
        print("That wasn't a valid integer. Please try again.\n")

while True:
    #get user input
    times = input("How many times for each race are there? ")
    try:
        #attempt to cast the number of races to an integer
        #if it fails jump to except
        num_times = int(times) #attempt to cast the number of races to an integer
        if num_times > 0:                        
            break#if valid then break out of the input loop
        else: 
            print("Please enter an integer greater than 0.\n")
    except ValueError:
        print("That wasn't a valid integer. Please try again.\n")



print()#print a blank space

#These variable are created here so they are seen and usable anywhere in our program
overall_total = 0.0
overall_count = 0

fastest_overall = None#could also use None with adjusted decision(meaning no value)
slowest_overall = None##could also use None with adjusted decision(meaning no value)
fastest_average = None#could also use None with adjusted decision(meaning no value)
# Outer loop over races
race_count = 1
while race_count <= num_races:
    print(f"Race #{race_count}")
    race_total = 0.0
    
    time_count = 1
    while time_count <= num_times:
        # Prompt for a float (positive), with validation
        while True:
            time = input(f"Enter time {time_count}: ")
            try:
                valid_time = float(time)
                if valid_time > 0:                                                        
                    break
                else: 
                    print("Please enter a non-negative time in seconds.\n")
            except ValueError:
                print("That wasn't a valid number. Please try again.\n")

        race_total += valid_time
        overall_total += valid_time
        overall_count += 1
        time_count += 1
        #if the time is faster than fastest so far
        #if it is the first time entered
        #set the fastest_overall
        if fastest_overall is None or valid_time < fastest_overall:
        # if valid_time is None or valid_time > fastest_overall:
            fastest_overall = valid_time
        if  fastest_overall is None or valid_time > slowest_overall:
        # if valid_time is None or valid_time < slowest_overall:
            slowest_overall = valid_time

    race_avg = race_total / (time_count - 1)#-1 due to using time_count in prompt
    print(f"Average time for race {race_count}: {race_avg:.2f}\n")
    race_count += 1
    if fastest_overall is None or race_avg < fastest_average:
    # if race_avg is None or race_avg > fastest_average:    
        fastest_average = race_avg
# After all races
overall_avg = overall_total / overall_count

print(f"Overall average time across all races: {overall_avg:.2f}")
print(f"Fastest time across all races: {fastest_overall:.2f}")
print(f"Slowest time across all races: {slowest_overall:.2f}")
print(f"Fastest race average: {fastest_average:.2f}")

#For Monday
#Functions to:
#return a valid integer > 0. def get_valid_positive_int(prompt):
#return a valid float > 0. def get_valid_positive_float(prompt):
#return an average. def get_and_calculate_average (sum,count):