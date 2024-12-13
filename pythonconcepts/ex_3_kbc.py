print("Welcome To Kaun Banega Crorepati!!!~~~~~~~")

questions = [
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"\nQuestion for Rs. {levels[i]}")
    print(f"a. {question[1]}        b. {question[2]} ")
    print(f"c. {question[3]}        d. {question[4]} ")
    reply = int(input("Enter your answer (1-4) or 0 to quit:\n"))
    if(reply == 0):
        money = levels[i-1]
        break
    if reply == question[-1]:
        print(f"Correct Answer, you've won Rs. {levels[i]}")
        if(i ==4):
            money = 10000
        elif(i == 9):
            money = 32000
        elif(i == 14):
            money = 10000000
    else:
        print("Wrong Answer!")
        break

print(f"Your take home money is {money}")