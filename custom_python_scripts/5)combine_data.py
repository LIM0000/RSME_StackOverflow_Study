# combine result_2.1.csv and result_2.2.csv
# Output -> result_3.csv

import csv
import xml.etree.cElementTree as ET

user_id_set = set()

# Set userid set
with open("D:\\Download (From Chrome)\\result_1.csv") as f:
    next(f)
    csvreader = csv.reader(f)
    for row in csvreader:
        user_id_set.add(row[2])

# ============================================================================================= #

print("Starting accumulation...")

user_dict = {}

# 0-th idx is PostTypeId = 1
# 2-th idx is PostTypeId = 2
for user_id in user_id_set:
    user_dict[user_id] = [0, 0, 0, 0, ""]

# Manage questions
with open("D:\\Download (From Chrome)\\result_2.1.csv") as f:
    next(f)
    csvreader = csv.reader(f)
    for row in csvreader:
        if int(row[3]) >= 500: user_dict[row[2]][1] += 1 
        user_dict[row[2]][0] += 1

# Manage answered
with open("D:\\Download (From Chrome)\\result_2.2.csv") as f:
    next(f)
    csvreader = csv.reader(f)
    for row in csvreader:
        if int(row[3]) >= 100: user_dict[row[2]][3] += 1
        user_dict[row[2]][2] += 1

# ============================================================================================= #

print("Starting getting date...")

context = ET.iterparse("D:\\Download (From Chrome)\\Users.xml", events=("end",))
# loop through each data <row>
for i, (event, element) in enumerate(context):
    try:
        if element.attrib["Id"] in user_id_set:
            user_dict[element.attrib["Id"]][4] = element.attrib["LastAccessDate"]
    except KeyError as kee:
        pass
    except Exception as e:
        raise(e)

    element.clear()

# ============================================================================================= #

print("Starting writing...")

columns = ["OwnerUserId", "TotalQuestions", "TotalQualityQuestions", "TotalAnswered", "TotalQualityAnswered" ,"LastAccessDate"]

with open("D:\\Download (From Chrome)\\result_3.csv", 'a', newline='') as f:
    writer = csv.writer(f)

    for user_id in user_id_set:
        writer.writerow([user_id, user_dict[user_id][0], user_dict[user_id][1], user_dict[user_id][2], user_dict[user_id][3], user_dict[user_id][4]])