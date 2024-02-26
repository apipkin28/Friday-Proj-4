# Friday-Proj-4
I will be using generative AI (ChatGPT) to improve my last three Friday Projects.

 # FP1_Madlib:
 a project in which a user will respond to prompts and be given a wacky story in return.
 
 def mad_lib()::
    Defines a function named mad_lib.
    
print("Welcome to Mad Libs! Let's create a fun story together."):
    Prints a welcome message to the user indicating the start of the game.

print("Please provide the following words when prompted:"):
    Instructs the user to provide words when prompted.

adjective = input("Enter an adjective: "):
    Prompts the user to input an adjective and stores the input in the variable adjective.

large_objects_plural = input("Enter a plural noun for large objects: "):
    Prompts the user to input a plural noun for large objects and stores the input in the variable large_objects_plural.

body_part = input("Enter a body part: "):
    Prompts the user to input a body part and stores the input in the variable body_part.

restaurant = input("Enter a restaurant name: "):
    Prompts the user to input a restaurant name and stores the input in the variable restaurant.

first_food = input("Enter a food item: "):
    Prompts the user to input a food item and stores the input in the variable first_food.

second_food = input("Enter another food item: "):
    Prompts the user to input another food item and stores the input in the variable second_food.

large_object_singular = input("Enter a singular noun for a large object: "):
    Prompts the user to input a singular noun for a large object and stores the input in the variable large_object_singular.

story = f"I’ve had a very {adjective} day.\n":
    Initializes the story variable with the beginning of the story template, using the provided adjective.

story += f"This morning, I dropped a box of {large_objects_plural} on my {body_part}.\n":
    Appends to the story variable the second part of the story template, incorporating the plural noun for large objects and the body part provided by the user.

story += f"Then, at lunch, I went to {restaurant} for their delicious {first_food},\n":
    Appends to the story variable the third part of the story template, using the provided restaurant name and the first food item.

story += f"But the waiter brought me {second_food}, which I was not hungry for.\n":
    Appends to the story variable the fourth part of the story template, incorporating the second food item provided by the user.

story += f"Finally, on my way home, I was cut off by a van with a large {large_object_singular} strapped to the roof.":
    Appends to the story variable the final part of the story template, using the singular noun for a large object.

print("\nHere's your Mad Lib story:\n"):
    Prints a message indicating that the Mad Lib story is about to be displayed.

print(story):
    Prints the completed Mad Lib story stored in the story variable.

mad_lib():
    Calls the mad_lib() function to start the execution of the Mad Lib game.

# Powerball_FP2:
a project in which a user can accept or decline a PowerBall number generation.

import random
    This line imports the random module, which provides functions for generating random numbers.

def generate_powerball_numbers():
    This line defines a function named generate_powerball_numbers that will generate PowerBall numbers.

white_balls = [str(random.randint(1, 69)) for _ in range(5)]
    This line generates a list comprehension to create a list of five random white ball numbers between 1 and 69.
    Each number is converted to a string using str() because the final output requires strings.
    The loop runs five times (range(5)), generating a random number each time.

red_ball = str(random.randint(1, 26))
    This line generates a random number for the red ball between 1 and 26 and converts it to a string.

powerball_numbers = '  '.join(white_balls) + '    ' + red_ball
    This line joins the white ball numbers into a single string separated by two spaces using the join() method.
    Four spaces are added after the white ball numbers and then concatenated with the red ball number.

return powerball_numbers
    This line returns the generated PowerBall numbers as a string.

def main():
    This line defines the main function of the program.

print("Welcome to the PowerBall number generator!")
    This line prints a greeting message to welcome the user.

response = input("Would you like some PowerBall numbers? (yes/no): ").lower()
    This line prompts the user with a question and waits for their response, which is converted to lowercase using the lower() method.

if response == 'yes':
    This line checks if the user's response is 'yes'.

powerball_numbers = generate_powerball_numbers()
    This line calls the generate_powerball_numbers() function to generate the PowerBall numbers.

print("Your PowerBall numbers are:", powerball_numbers)
    This line prints out the generated PowerBall numbers.

else:
    This line handles the case where the user's response is not 'yes'.

print("Okay, maybe next time!")
    This line prints a message indicating that the user declined to get PowerBall numbers.

print("Thank you for using the PowerBall number generator. Goodluck!")
    This line prints a farewell message to the user.

if __name__ == "__main__":
    This line checks if the script is being run directly as the main program.

main()
    This line calls the main() function if the script is being run directly.

# QuizBowl_FP3
a project in which a user can play a game of QuizBowl.

trivia_questions = {
    "What is the capital of France?": "Paris",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the chemical symbol for water?": "H2O",
    "Which planet is known as the Red Planet?": "Mars",
    "Who painted the Mona Lisa?": "Leonardo da Vinci"
}
This block of code defines a dictionary named trivia_questions where keys represent trivia questions and values represent their corresponding answers.

for question, answer in trivia_questions.items():
    This line starts a for loop that iterates over each key-value pair in the trivia_questions dictionary. The items() method is used to retrieve both the keys and values during each iteration.

print(question)
    This line prints the current question to the user.

user_answer = input("Your answer: ")
    This line prompts the user to input their answer and stores it in the variable user_answer.

if user_answer.lower() == answer.lower():  # Case insensitive comparison
    This line checks if the user's answer matches the correct answer. The lower() method is used to convert both the user's answer and the correct answer to lowercase for case-insensitive comparison.

    print("Correct!")
else:
    print("Incorrect. The correct answer is:", answer)
        These lines provide feedback to the user based on whether their answer is correct or incorrect. If the answers match, "Correct!" is printed. Otherwise, "Incorrect. The correct answer is:" followed by the correct answer is printed.

print()  # Print an empty line for better readability
    This line prints an empty line to create space between questions for better readability in the output. It is outside the loop to ensure it only prints once after each question.