import yaml
import random
from openpyxl import Workbook

# Load the questions from the YAML file
with open('music_trivia.yaml') as file:
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

    # Prompt the user to enter their answer
    user_answer = input("Enter your answer (1-4): ")

    # Check if the user's answer is correct
    if question['options'][int(user_answer)-1] == question['answer']:
        print("Correct!")
        is_correct = 'Yes'
    else:
        print(f"Incorrect. The correct answer is {question['answer']}.") #
        is_correct = 'No'

    # Write the question number, user's answer, and correct answer to the worksheet
    worksheet.append([question['question'], question['options'][int(user_answer)-1], question['answer']])

    # Add a column for whether the user's answer is correct
    worksheet.cell(row=i+2, column=4, value=is_correct)

    # the reason why we are using i+2 is because we have a header row and index starts at 0 so we need to add 2

# Save the workbook to an XLSX file
workbook.save('music_trivia_results.xlsx')
