import random
import yaml

# Load the questions from the YAML file
with open('CodeQuiz.yaml', 'r') as f:
    questions = yaml.safe_load(f)

# Shuffle the questions
random.shuffle(questions)

# Loop through each question and prompt the user
for question in questions:
    # Shuffle the options
    random.shuffle(question['options'])

for i, question in enumerate(questions):
    # Print the question number and the question text
    print(f"\nQuestion {i+1}: {question['question']}")
    print(f"\nCode {i+1}: {question['code']}")
    
    # Shuffle the options
    random.shuffle(question['options'])
    
    # Print the options
    for i, option in enumerate(question['options']):
        #print(f"{chr(65 + i)}. {option}")
        print(f"{chr(65 + i)}. {option.split('. ')[1]}")



    # Get user input
    user_input = input("Your answer: ").strip().upper()

    # Check if the answer is correct
    if user_input == question['answer']:
        print("Correct!")
    else:
        print("Incorrect. Generating testMe.py file...")

        # Generate the testMe.py file
        with open('testMe.py', 'w') as f:
            # Write the function signature
            f.write(f"{question['code']}():\n")

