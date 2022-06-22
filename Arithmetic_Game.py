from random import randrange
print("Welcome to the Arithmetic Game")
print("Enter your player name:")

player_name = input()
print(f"Hello,", player_name)
score = 0

def addition():
    print("Addition Mode:")
    num1 = randrange(0, 9)
    num2 = randrange(0, 9)
    sum = num1 + num2
    print(num1,"+",num2)
    answer = int(input())
    if sum==answer:
        print("Correct!")
        global score 
        score += 1
    else:
        print("Incorrect!")

def subtraction():
    print("Subtraction Mode:")
    num1 = randrange(0, 9)
    num2 = randrange(0, 9)
    if num1 > num2:
        difference = num1 - num2
        print(num1,"-",num2)
    else:
        difference = num2 - num1
        print(num2,"-",num1)
    answer = int(input())
    if difference==answer:
        print("Correct!")
        global score 
        score += 1
    else:
        print("Incorrect!")

def multiplication():
    print("Multiplication Mode:")
    num1 = randrange(0, 9)
    num2 = randrange(0, 9)
    product = num1 * num2
    print(num1,"x",num2)
    answer = int(input())
    if product==answer:
        print("Correct!")
        global score 
        score += 1
    else:
        print("Incorrect!")

def division():
    print("Division Mode:")
    num1 = randrange(0, 9)
    num2 = randrange(0, 9)
    if num1 > num2:
        quotient = num1 / num2
        print(num1,"/",num2)
    else:
        quotient = num2 / num1
        print(num2,"/",num1)
    answer = int(input())
    print(answer)
    if quotient==answer:
        print("Correct!")
        global score 
        score += 1
    else:
        print("Incorrect!")

def random_mode():
    print("Random Mode")
    mode = randrange(1,4)
    if mode==1:
        addition()
    elif mode==2:
        subtraction()
    elif mode==3:
        multiplication()
    else:
        division()

def scores():
    f = open("RecentScores.txt", "r")
    print("Recent Scores:")
    print(f.read())
    
response = 0
while response != 5:
 print(f"Your score:",score)
 print("\nEnter Game Mode:")
 print("1.) Addition")
 print("2.) Subtraction")
 print("3.) Multiplication")
 print("4.) Division")
 print("5.) Random")
 print("6.) Scores")
 print("7.) Exit")

 print("\nEnter Game Mode:")
# menu input
 response = input()
# switch
 if response == "1":
    addition()
 elif response == "2":
    subtraction()
 elif response == "3":
    multiplication()
 elif response == "4":
    division()
 elif response == "5":
    random_mode()
 elif response == "6":
    scores()
 elif response == "7":
    print("Thanks for playing!")
    score = str(score)
    RecentScores = open('RecentScores.txt','a')
    RecentScores.write(player_name)
    RecentScores.write('\n')
    RecentScores.write(score)
    RecentScores.write('\n')
    RecentScores.close()
    quit()
 else:
    print("Invalid response")


    
    