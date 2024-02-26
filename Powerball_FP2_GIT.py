import random

def generate_powerball_numbers():
    # Generate the first five numbers (white balls)
    white_balls = [str(random.randint(1, 69)) for _ in range(5)]
    
    # Generate the last number (red ball)
    red_ball = str(random.randint(1, 26))
    
    # Join all numbers into a single string with appropriate spacing
    powerball_numbers = '  '.join(white_balls) + '    ' + red_ball
    
    return powerball_numbers

def main():
    print("Welcome to the PowerBall number generator!")
    response = input("Would you like some PowerBall numbers? (yes/no): ").lower()
    
    if response == 'yes':
        powerball_numbers = generate_powerball_numbers()
        print("Your PowerBall numbers are:", powerball_numbers)
    else:
        print("Okay, maybe next time!")
    
    print("Thank you for using the PowerBall number generator. Good luck!")

if __name__ == "__main__":
    main()