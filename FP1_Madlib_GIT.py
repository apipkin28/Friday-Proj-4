def mad_lib():
    # Welcome message and instructions for the user
    print("Welcome to Mad Libs! Let's create a fun story together.")
    print("Please provide the following words when prompted: ")

# Prompting user for words
lgobj = input("Enter a large object: ")
lgobjs = input("Enter large objects: ")
adj = input("Enter an adjective: ")
bdypt = input("Enter a body part: ")
rest = input("Enter a restaurant: ")
food1 = input("Enter a food: ")
food2 = input("Enter another food: ")

# Story template with inserted words
story = f"I've had a very {adj} day.\n"
story += f"This morning, I dropped a box of {lgobjs} on my {bdypt}.\n"
story += f"Then, at lunch, I went to {rest} for their delicious {food1},\n"
story += f"But the waiter brought me {food2}, which I was not hungry for.\n"
story += f"Finally, on my way home, I was cut off by a van with a large {lgobj} strapped to the roof."

print("\nHere's your Mad Lib story:\n")
print(story)

# Calling the function to play the Mad Lib game
mad_lib()