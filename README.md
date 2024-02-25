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

