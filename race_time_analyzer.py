from validation_and_math_functions import *   #import ALL the functions from this file

print("\n🏁 Race Time Analyzer\n")

# Ask for number of races (integer > 0), with validation
num_races = get_valid_positive_int("Enter the number of races: ")
num_times = get_valid_positive_int("Enter the number of times: ")


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
        valid_time = get_valid_positive_float(f"Enter time #{time_count}: ")        

        race_total += valid_time
        overall_total += valid_time
        overall_count += 1
        time_count += 1
        #if the time is faster than fastest so far
        #if it is the first time entered
        #set the fastest_overall
        if fastest_overall == None or valid_time < fastest_overall:
        # if valid_time is None or valid_time > fastest_overall:
            fastest_overall = valid_time
        if slowest_overall == None or valid_time > slowest_overall:
        # if valid_time is None or valid_time < slowest_overall:
            slowest_overall = valid_time

    race_avg = get_and_calculate_average(race_total,time_count - 1)    
    print(f"Average time for race {race_count}: {race_avg:.2f}\n")
    race_count += 1
    if fastest_average == None or race_avg < fastest_average:
    # if race_avg is None or race_avg > fastest_average:    
        fastest_average = race_avg
# After all races
overall_avg = get_and_calculate_average(overall_total,overall_count)

print(f"Overall average time across all races: {overall_avg:.2f}")
print(f"Fastest time across all races: {fastest_overall:.2f}")
print(f"Slowest time across all races: {slowest_overall:.2f}")
print(f"Fastest race average: {fastest_average:.2f}")

#For Monday
#Functions to:
#return a valid integer > 0. def get_valid_positive_int(prompt):
#return a valid float > 0. def get_valid_positive_float(prompt):
#return an average. def get_and_calculate_average (sum,count):