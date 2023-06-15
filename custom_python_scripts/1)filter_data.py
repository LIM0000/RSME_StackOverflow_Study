# DataDump from 2023-03-08

# Filter question data with PostTypeId="1" with "javascript" tags
# Output -> result_1.csv
# script takes about 30 mins

import xml.etree.cElementTree as ET
import csv
import traceback

# javascript total -> 2494276
previous_stopped_position = 0
columns = ["Id", "PostTypeId", "OwnerUserId"]

try:
    context = ET.iterparse("D:\\Download (From Chrome)\\Posts.xml", events=("end",))
    with open("D:\\Download (From Chrome)\\result_1.csv", 'a', newline='') as f:
        writer = csv.writer(f)

        # loop through each data <row>
        for i, (event, element) in enumerate(context):
            if i < previous_stopped_position: 
                element.clear()
                continue

            try:
                # Check has "Tag" attribute
                post_tags = element.attrib["Tags"]

                # If data has tag "javascript"
                if post_tags.find("javascript") != -1:
                    writer.writerow([element.attrib[column] for column in columns])
            except KeyError as kee:
                # traceback.print_exc()
                pass
            except Exception as e:
                raise(e)

            element.clear()
except KeyboardInterrupt:
    print("Last index from enumeration: " + str(i))
except Exception as e:
    print("Error: " + str(e))
    print("Last index from enumeration: " + str(i))