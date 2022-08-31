print("\nWelcome to the roller-coaster!\n")
height = int(input("\nWhat's your height in cm? "))

if height > 120:
    print("\nPerfect, check the price!\n")
    age = int(input("\nwhat's your age? "))
    if age < 12:
        print("\nPlease answer another question, and pay $5.\n")
    elif 18 <= age:
        print("\nPlease answer another question, and pay $8")
    else:
        print("\nPlease answer another question, and pay $12")
    medical_condition = str(input("\nDo you have any medium or serious medical conditions?Y/N ").upper())
    if medical_condition == 'Y':
        print("\nI'm sorry, You're not allowed to ride the roller-coaster. ")
    else:
        print("\nHave Fun")
else:
