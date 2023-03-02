import yaml
import random
import time
import select
from django.shortcuts import render
from openpyxl import Workbook

def trivia(request):
    # Load the questions from the YAML file
    with open('python.yaml') as file:
        questions = yaml.load(file, Loader=yaml.FullLoader)

    # Shuffle the questions randomly
    random.shuffle(questions)

    # Select the first 10 questions
    questions = questions[:10]

    # Create a new workbook and worksheet for the results
    workbook = Workbook()
    worksheet = workbook.active

    # Write the header row to the worksheet
    worksheet.append(['Question', 'User Answer', 'Correct Answer'])

    # Iterate over the shuffled questions
    for i, question in enumerate(questions):
        # Shuffle the options randomly
        random.shuffle(question['options'])

        # Prompt the user to enter their answer within 30 seconds
        start_time = time.time()
        user_answer = None
        while (time.time() - start_time) < 30:
            if select.select([request], [], [], 1)[0]:
                user_answer = request.POST.get('answer')
                break

        # Check if the user's answer is correct
        if user_answer is None:
            is_correct = 'No (timed out)'
        elif question['options'][int(user_answer)-1] == question['answer']:
            is_correct = 'Yes'
        else:
            is_correct = 'No'

        # Write the question number, user's answer, and correct answer to the worksheet
        worksheet.append([question['question'], question['options'][int(user_answer)-1] if user_answer is not None else '', question['answer']])

        # Add a column for whether the user's answer is correct
        worksheet.cell(row=i+2, column=4, value=is_correct)

    # Save the workbook to an XLSX file
    workbook.save('python_trivia_results.xlsx')

    return render(request, 'trivia.html')
