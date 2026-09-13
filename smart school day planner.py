print("====Smart School Day Planner======")
print("Answer 3 questions quickly and I will plan your day!/n")

day= input("What day it is?(Monday to Sunday:").strip().capitalize()
weather=input("What is the weather?(sunny/rainy/cloudy):").strip().lower()
homework=input("Is your homeork done?(yes/no):").strip().lower()

print()
print(f"=== Your plan for {day}===")    
print("-"*35)

if day in ("Saturday", "Sunday"):
    print("Day type:Weekend-enjoy your free time!")
elif day == "Monday":
    print("Day type:Firsts day of the week. Pack your weekly planner,")
elif day == "Friday":
    print("Day type:Last school day. Return library books todaY.")
elif day in ("Tuesday", "Wednesday","Thursday"):
    print("Day type:Regular school day. Stay focused!")
else:
    print("Day type : Day not recognised. Please check the spelling.")

if weather == "Sunny" and homework == "yes":
    print("After school:Head to the park-great weatherand homework is done!")

if weather == "rainy" or weather == "cloudy":
    print("Weather tip:   Pack your umbrealla- it may get wet outside.")

if not (homework == "yes"):
    print("Homework:   Not done yet. Finish it before going out!")

if weather == "rainy" and not (homework == "yes"):
    print("Best plan:    Stay in, finish homework, then watch your favourite show,")

elif weather== "sunny" and homework == "yes" and not (day in ("Saturday", "Sunday")):
    print("Best plan  : All set for a great school day-you are prepared!")
elif day in ("Saturday", "Sunday") and weather == "sunny":
        print("Best plan : Perfect weekend weather - head outside and have fun!") 
else:
    print("Best plan:  Take it one step at a time- you have got this!")

print()
print("Plan complete! Have a wonderful day!")