print("Golf Scrore Calculator")
sum = 0

scores = []
top_5_sum = 0
while True:
    #get scores from user
    score= input("Enter another score: (q to quit and calculate): ")
    #if q then quit
    if score == "q":
        break      
    #add the score to sum
    score = int(score)
    sum += score
    scores.append(score)

#calculate average
average  = sum/len(scores)
#display average
print(f"Your average golf score is {average}")

#HANDICAP CALCULATION
scores.sort()

#if less than 5 scores message
if len(scores)< 5:
    print("Your handicap is: Need at least 5 scores to calculate a handicap")
else:
#Sum of the top 5 scores
    for score in scores[0:5]:
        top_5_sum += score

    #calculate handicap
    handicap = top_5_sum/5 -72

    #display the handicap
    print(f"Your handicap is: {handicap:.2f}")


