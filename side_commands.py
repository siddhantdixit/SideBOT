import re
import json
import datetime
import side_functions
import whatsappTasks
from whatsappTasks import Tasks

help_cmd = "#sidebot help"
help_pls = "#sidebot pls help"

change_group = "#sidebot pls come here"
change_group2 = "#sidebot come here"

sidebot_status = "#sidebot status"

tag_everyone = "#sidebot tag everyone"
plstag_everyone = "#sidebot pls tag everyone"

who_is_on9 = "#sidebot whoisonline"

# Images Command

# pls_slp = "#sidebot pls slap "
pls_slp = '#sidebot pls slap @.*'

pls_congrats = '#sidebot pls congrats @.*'
pls_congrats2 = '#sidebot congrats @.*'


pls_wanted = '#sidebot wanted @.*'
pls_danger = '#sidebot danger @.*'
pls_jail = '#sidebot jail @.*'

command_functions = {
    sidebot_status: side_functions.already_there_in_grp,
    change_group: side_functions.already_there_in_grp,
    change_group2: side_functions.already_there_in_grp,
    tag_everyone: side_functions.tag_everyone,
    plstag_everyone: side_functions.tag_everyone,
    who_is_on9: side_functions.who_is_online,
    pls_slp: side_functions.pls_slap,
    help_cmd: side_functions.pls_help,
    help_pls: side_functions.pls_help,
    pls_congrats: side_functions.pls_congrats,
    pls_congrats2: side_functions.pls_congrats,
    pls_wanted: side_functions.make_wanted,
    pls_danger: side_functions.in_danger,
    pls_jail: side_functions.in_jail
}



class LogWrite:

    temp = dict()
    data = None

    def __init__(self):
        with open('res/log_files/command_log.json') as json_file:
            self.data = json.load(json_file)
            self.temp = self.data['logs']

    @staticmethod
    def write_json(data, filename='res/log_files/command_log.json'):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)


logfile = LogWrite()
print("LOGGING FILE OPENED")



def perform_function(task_obj, sender, command):
    x = False
    for cmd in command_functions:
        # print(cmd)
        if re.search(cmd, command):
            command_functions[cmd](task_obj, sender, command)
            # print("Found = ", cmd)
            details = {
                "time": str(datetime.datetime.now()),
                "sender": sender,
                "command": command
            }
            logfile.temp.append(details)
            logfile.write_json(logfile.data)
            x = True
            break

    if not x:
        side_functions.invalid_messege(task_obj)

    # if command in command_functions:
    #     command_functions[command](task_obj, sender, command)
    #
    # else:
    #     side_functions.invalid_messege(task_obj)
