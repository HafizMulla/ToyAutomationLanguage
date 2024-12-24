import time
from ToyAutomationFramework.Utilities.Utils import Utilities
from ToyAutomationFramework.toy_methods.methods import open_url, input_text, click_element, verify_text, \
    upload_file, select_radio, select_checkbox, alert_accept, confirmation_alert_accept, confirmation_alert_dismiss, \
    prompt_alert_accept, deselect_checkbox, select_value_from_dropdown

def collect_the_commands(test_file):
    utilities = Utilities()

    # Reading the keywords from the keyword file
    predefine_commands = utilities.read_predefine_keywords_from_keyword_file("resources/predefine_keywords.txt")

    # Reading commands from the test file
    commands = utilities.read_file(test_file)
    return commands

# Reading the commands from the text file
def fetching_the_commands(test_file):
    commands_dict = {}
    utilities = Utilities()

    # Reading the keywords from the keyword file
    predefine_commands = utilities.read_predefine_keywords_from_keyword_file("resources/predefine_keywords.txt")
    # Reading commands from the test file
    commands = utilities.read_commands_from_test_file(test_file)
    if len(commands)>0:
        for command in commands:
            # Checking the keyword is valid or not before proceeding
            if command[0].split(" ")[0] in predefine_commands:
                # If the command length is 2,e.g: OPEN url
                if len(command)==2:
                    commands_dict[command[0]]=[command[1],len(command)]

                # If the command length is 3,e.g: INPUT #username admin
                elif len(command)==3:
                    commands_dict[command[0]+" "+command[1]]=[command[2],len(command)]

                # If the command length is 4,e.g: UPLOAD #singleFileInput #singleFileForm>button testuploadfile.xlsx
                elif len(command)==4:
                    commands_dict[command[0]+" "+command[1]+" "+command[2]]=[command[3],len(command)]

            else:
                utilities.raise_error('Invalid Command:'+command[0]+' in the file.Please check.')
    return commands_dict

def execute_commands(file_commands):
    # Map actions to corresponding functions
    action_map = {
        "OPEN": open_url,
        "INPUT": input_text,
        "CLICK": click_element,
        "VERIFY": verify_text,
        "SELECT": select_radio,
        "CHECK": select_checkbox,
        "UNCHECK": deselect_checkbox,
        "SELECT_FROM_DROPDOWN": select_value_from_dropdown,
        "ALERT_ACCEPT": alert_accept,
        "CONFIRMATION_ALERT_ACCEPT": confirmation_alert_accept,
        "CONFIRMATION_ALERT_DISMISS": confirmation_alert_dismiss,
        "PROMPT_ALERT": prompt_alert_accept,
        "UPLOAD": upload_file
    }

    for key,value in file_commands.items():
        if value[1]==2:
            action_map[key](value[0])
            time.sleep(3)

        if value[1]==3:
            id=key.split(" ")[1]
            command = key.split(" ")[0]
            action_map[command](id,value[0])
            time.sleep(3)

        if value[1]==4:
            command = key.split(" ")[0]
            choose_file = key.split(" ")[1]
            upload_button=key.split(" ")[2]
            file_name = value[0]
            action_map[command](choose_file,upload_button,file_name)
