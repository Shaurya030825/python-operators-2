print("======Swimming Pool Entry Check======")
print("Answer 3 questions and i will tell you which pool you can use./n")

age=int(input("How old are you?"))
can_swim=input("Can you swim 25 metres?(yes/no):").lower()
adult_here=("Is an adult with you?(yes/no):").lower()

print()
print("====Entry Decision====")
print("-"*32)

if age<4:
    print("Age group: toddler-splash pool only,always with an adult.")
elif age<12:
    print("Age group :child- main pool with an adult.")
elif age <18:
    print("Age group :Teen- Main pool alone if you can swim.")
else:
    print("Age group :adult- all pools open forr you!")

if can_swim != "yes" and can_swim != "no":
    print("Input error :Please answer the swimming question with yes or no.")
    swim_known= False
else:
    swim_known= True

if adult_here != "yes" and adult_here != "no":
    print("Input error: Please answer the adult question with yes or no.")
    adult_known= False
else:
    adult_known= True

if can_swim == "yes" and adult_here == "yes":
    print("Deep pool :Allowed- you can swin and an adult is present.") 

if age<12 or can_swim == "no":
    print("Shallow only:Stay in the shallow end today.")

if adult_known== True and not (adult_here=="yes"):
    print("Reminder: No adult with you- the lifeguard muust be told.")

if swim_known== False or adult_known== False:
    print("Verdict: Cannot decide until you answer the questions properly.")

elif age>=18 and can_swim== "yes":
    print("Verdict: Full access. Enjoy your swim.")
elif age >= 12 and can_swim=="yes" and adult_here == "yes":
    print("Verdict:    Main pool access only when adult nearby.")
elif can_swim== "no" and not(adult_here== "yes"):
    print("Verdict : Shallow end only, and please find an adult first.")
else:
    ("Verdict: Shallow end only- come bacak with an adult for more>")

print()
print("Have a safe swim")
    