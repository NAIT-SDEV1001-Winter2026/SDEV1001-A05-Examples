#prompt for a movie name
movie_name = input("Enter a movie name: ").lower()
#if "star wars" print 2 prints
if movie_name == "star wars":
    print("Great movie!")
    print("Check it out!")
#if "star trek" print 1 print
elif movie_name == "star trek":
    print("Good movie")
#if "Maze Runner" print 1 print
elif movie_name == "maze runner":
    print("Cool show!")
#otherwise print ("Unknown Movie")
else:
    print("Unknown Movie")

#Match Case
match movie_name:
    case "Star Wars":
        print("Great movie!")
        print("Check it out!")
    case "Star Trek":
        print("Good Movie")
    case "Maze Runner":
        print("Cool Show!")
    case _:
        print("unknown Movie")
    


