# Result for RQ2

import csv
from datetime import datetime

active_user = {
    "quality_post": 0,
    "inquality_post": 0
}

inactive_user = {
    "quality_post": 0,
    "inquality_post": 0
}

with open("D:\\Download (From Chrome)\\result_3.csv") as f:
    next(f)
    csvreader = csv.reader(f)

    data_dump_date = datetime.strptime("2023-03-08", "%Y-%m-%d").date()

    for row in csvreader:
        # row[1] -> totalQuestions
        # row[2] -> totalQualityQuestions
        # row[3] -> totalAnswered
        # row[4] -> totalQualityAnswered
        # row[5] -> LastAccessDate

        difference_in_days =  (data_dump_date - datetime.fromisoformat(row[5]).date()).days

        # If more than 14 days, we considered inactive
        if difference_in_days <= 14 and (int(row[2]) + int(row[4])) >= 1:
            active_user["quality_post"] += 1
        elif difference_in_days <= 14 and (int(row[2]) + int(row[4])) == 0:
            active_user["inquality_post"] += 1
        elif difference_in_days > 14 and (int(row[2]) + int(row[4])) >= 1:
            inactive_user["quality_post"] += 1
        elif difference_in_days > 14 and (int(row[2]) + int(row[4])) == 0:
            inactive_user["inquality_post"] += 1

    print(active_user)
    print(inactive_user)