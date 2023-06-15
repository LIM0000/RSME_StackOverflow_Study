# Get all available users in lists from result_1.csv
# Filter answers data with PostTypeId="1" (we take all questions, does not matter how many user has questioned)
# Output -> result_2.1.csv
# script takes about 40 mins

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

print("Starting filter...")

previous_stopped_position = 0
columns = ["Id", "PostTypeId", "OwnerUserId", "Score"]

try:
    context = ET.iterparse("D:\\Download (From Chrome)\\Posts.xml", events=("end",))
    with open("D:\\Download (From Chrome)\\result_2.1.csv", 'a', newline='') as f:
        writer = csv.writer(f)

        # loop through each data <row>
        for i, (event, element) in enumerate(context):
            if i < previous_stopped_position: 
                element.clear()
                continue

            try:
                # Check is PostTypeId = 2
                if element.attrib["PostTypeId"] == "1" and element.attrib["OwnerUserId"] in user_id_set:
                    writer.writerow([element.attrib[column] for column in columns])
            except KeyError as kee:
                pass
            except Exception as e:
                raise(e)

            element.clear()
except KeyboardInterrupt:
    print("Last index from enumeration: " + str(i))
except Exception as e:
    print("Error: " + str(e))
    print("Last index from enumeration: " + str(i))