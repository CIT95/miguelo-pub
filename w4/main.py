import random
# LISTS FILLED IN
weekList = ["Monday", "Tuesday", "Wednesday", "Thurday",
            "Friday", "Saturday", "Sunday"]
motivatingWord = ["great", "wonderfull", "stupendous", "fantastic",
                  "fabulous", "splendid", "marvelous", "superb",
                  "favorable", "satisfying", "delightful", "rewarding",
                  "fulfilling", "gainful", "fruitful", "productive"]
musclesToWork = ["legs", "abs", "shoulders", "back", "chest", "biceps"]
userName = input("What is your name?: ")
# PROMPT THE USER
print(f"{userName}'s Weekly Gym Planner")
print("\
       0: Monday\n\
       1: Tuesday\n\
       2: Wednesday\n\
       3: Thurday\n\
       4: Friday\n\
       5. Saturday\n\
       6. Sunday\n")
# input what day of the week it is
dayOfWeek = int(input("What day of the week is it today?: "))
while dayOfWeek < 0 or dayOfWeek > 6:
    print("Invalid input!")
    dayOfWeek = int(input("What day of the week is it today?: "))

# Input for if the user went to work today
print("0: No\n1: Yes")
workToday = int(input("Did you go to work today?: "))
while workToday < 0 or workToday > 1:
    print("Invalid input!")
    workToday = int(input("Did you go to work today?: "))

# Randomly chooses a motivating word and output
randWord = random.randint(0, len(motivatingWord)-1)
print(f"\nToday is {weekList[dayOfWeek]} and you will \
have a {motivatingWord[randWord]} day!")

# BASED ON THE INPUT, OUTPUT THE DAY'S SCHEDULE
if dayOfWeek == 0:
    print("I will stay at the gym from 3p.m. to 5p.m.")
    print("Today we will work out our legs and abs")
elif dayOfWeek == 1:
    print("I will stay at the gym from 3p.m. to 5p.m.")
    print("Today we will work out our shoulders and back")
elif dayOfWeek == 2:
    print("I will stay at the gym from 3p.m. to 5p.m.")
    print("Today we will work out our chest and biceps")
elif dayOfWeek == 3:
    print("We will stay at the gym from 5p.m. to 7p.m.")
    print("Today we will work out our shoulders and back")
elif dayOfWeek == 4:
    print("We will stay at the gym from 5p.m. to 7p.m.")
    print("Today we will work out our legs and abs")

else:
    if(workToday == 1):
        print("You do not need to work out today")
        print("Take a rest day!")
    elif(workToday == 0):
        randWorkOut = random.randint(0, 6)
        print("We will stay at the gym from 3p.m. to 5p.m.")
        print(f"We will work on our {musclesToWork[randWorkOut]} and tricepts")

# Decided if we need to run today
if(workToday == 1):
    print("Today you do not need to run the mile")
elif(workToday == 0):
    print("Before that we will start with a mile run on the treadmill")
