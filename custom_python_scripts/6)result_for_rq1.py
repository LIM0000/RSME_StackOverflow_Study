# Result for RQ1

import csv
from datetime import datetime


question_more_than_answer = {
    "active": 0,
    "inactive": 0
}

answer_more_than_question = {
    "active": 0,
    "inactive": 0
}

with open("D:\\Download (From Chrome)\\result_3.csv") as f:
    next(f)
    csvreader = csv.reader(f)

    data_dump_date = datetime.strptime("2023-03-08", "%Y-%m-%d").date()

    for row in csvreader:
        # row[1] -> totalQuestions
        # row[3] -> totalAnswered
        # row[5] -> LastAccessDate

        difference_in_days =  (data_dump_date - datetime.fromisoformat(row[5]).date()).days

        # If more than 14 days, we considered inactive
        if int(row[1]) > int(row[3]) and difference_in_days > 14:
            question_more_than_answer["inactive"] += 1
        elif int(row[1]) > int(row[3]) and difference_in_days <= 14:
            question_more_than_answer["active"] += 1
        elif int(row[1]) <= int(row[3]) and difference_in_days > 14:
            answer_more_than_question["inactive"] += 1
        elif int(row[1]) <= int(row[3]) and difference_in_days <= 14:
            answer_more_than_question["active"] += 1
        
    print(question_more_than_answer)
    print(answer_more_than_question)