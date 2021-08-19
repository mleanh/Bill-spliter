import random
attendants_dict = {}
names = []
while True:
    print("Enter the number of friends joining (including you):")
    attendants = int(input())
    if attendants <= 0:
        print("No one is joining for the party")
        break
    else:
        print("Enter the name of every friend (including you), each on a new line:")
        for _ in range(0, attendants):
            names.append(input())
        print("Enter the total bill value")
        bill = int(input())
        print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:")
        answer = input()
        if answer == "Yes":
            name = random.choice(names)
            print(name + " is the lucky one!")
            split = round(bill / (attendants - 1), 2)
            attendants_dict = dict.fromkeys(names, split)
            attendants_dict.update({name: 0})
        else:
            print("No one is going to be lucky")
            split = round(bill / attendants, 2)
            attendants_dict = dict.fromkeys(names, split)
        print(attendants_dict)
        break
