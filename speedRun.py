import yaml
import random
import time
from openpyxl import Workbook
import msvcrt

# Load the questions from the YAML file
with open('python.yaml') as file:
    questions = yaml.load(file, Loader=yaml.FullLoader)

# Shuffle the questions randomly
random.shuffle(questions)

# Select the first 20 questions
questions = questions[:20]

# Create a new workbook and worksheet for the results
workbook = Workbook()
worksheet = workbook.active

# Write the header row to the worksheet
worksheet.append(['Question', 'User Answer', 'Correct Answer'])

# Iterate over the shuffled questions
for i, question in enumerate(questions):
    # Print the question number and the question text
    print(f"\nQuestion {i+1}: {question['question']}")

    # Shuffle the options randomly
    random.shuffle(question['options'])

    # Iterate over the shuffled options and print each one
    for j, option in enumerate(question['options']):
        print(f"{j+1}. {option}")

    # Prompt the user to enter their answer within 30 seconds
    start_time = time.time() # this is the time when the question is asked
    while (time.time() - start_time) < 10: # this is the time when the question is asked + 30 seconds
        if msvcrt.kbhit(): # this is the time when the user enters the answer
            user_answer = msvcrt.getch() # this captures the user's answer
            break # this breaks the loop
    else:
        user_answer = '0' # this is the default value if the user doesn't enter the answer within 30 seconds

    # Check if the user's answer is correct
    if user_answer == '0': # if the user doesn't enter the answer within 30 seconds
        print("Time's up!")
        is_correct = 'No'
    elif question['options'][int(user_answer)-1] == question['answer']: # if the user enters the answer within 30 seconds and it's correct
        print("Correct!")
        is_correct = 'Yes'
    else:
        print(f"Incorrect. The correct answer is {question['answer']}.")
        is_correct = 'No'

    # Write the question number, user's answer, and correct answer to the worksheet
    worksheet.append([question['question'], question['options'][int(user_answer)-1], question['answer']])

    # Add a column for whether the user's answer is correct
    worksheet.cell(row=i+2, column=4, value=is_correct) # the reason why we are using i+2 is because we have a header row and index starts at 0 so we need to add 2

# Save the workbook to an XLSX file
workbook.save('python_results.xlsx')
