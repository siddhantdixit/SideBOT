import json
import datetime
# function to add to JSON


def write_json(data, filename='command_log.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


with open('command_log.json') as json_file:
    data = json.load(json_file)

    temp = data['logs']

    # python object to be appended
    y = {
         "time": str(datetime.datetime.now()),
         "sender": "nikhil@geeksforgeeks.org",
         "command": "Full Time"
         }

    # appending data to emp_details
    temp.append(y)

write_json(data)
