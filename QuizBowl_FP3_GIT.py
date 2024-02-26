# Define a dictionary with trivia questions and answers
print("Welcome to The QuizBowl! Your questions start now.")
questionsList = {"What is the tallest animal in the world? ":"Giraffe",
                 "What is the anatomical term for the collarbone? ":"Clavicle",
                 "What does the deepest point in the ocean measure (in meters)? ":"10,935",
                 "When was the first computer invented? ":"1822",
                 "What types of letters will cost you in Wheel of Fortune? ":"Vowels"}
score = 0
# Iterate over each question in the dictionary
for question, answer in questionsList.items():
    # Display the question to the user
    print(question)
    # Prompt the user to input their answer
    response = input("Your answer: ")

    # Check if the user's answer matches the correct answer
    if response == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is:", answer)

print("Quiz ended. Your score is "+str(score)+" out of 5.")