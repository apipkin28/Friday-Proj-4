import random
print("Welcome to the PowerBall number generator.")
userResponse = input("Would you like some PowerBall numbers? (yes/no): ")
if userResponse == "yes":
    ball1 = random.randint(1, 69)
    ball2 = random.randint(1, 69)
    ball3 = random.randint(1, 69)
    ball4 = random.randint(1, 69)
    ball5 = random.randint(1, 69)
    ball6 = random.randint(1, 26)
    print("Your PowerBall numbers are: "+str(ball1)+"  "+str(ball2)+"  "+str(ball3)+"  "+str(ball4)+"  "+str(ball5)+"    "+str(ball6)+".")
    print("Thanks for using the PowerBall number generator. Goodbye!")
else:
    print("Understandable. Have a great day.")