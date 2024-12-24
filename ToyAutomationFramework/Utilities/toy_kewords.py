from ToyAutomationFramework.loggenerator.logger import Logger
from ToyAutomationFramework.Utilities.Utils import Utilities
from ToyAutomationFramework.toy_methods.methods import open_url, prompt_alert_accept, alert_accept, \
    confirmation_alert_dismiss, confirmation_alert_accept, input_text, select_radio, select_checkbox, deselect_checkbox, \
    select_value_from_dropdown, upload_file, click_element, verify_text


class ToyKeywordImplementation:
    def __init__(self):
        self.logger = Logger.get_logger(__name__)

    def fetch_the_commands(self,test_file):
        utilities = Utilities()
        # Reading commands from the test file
        commands = utilities.read_commands_from_test_file(test_file)
        return commands

    def execute_keyword(self, commands):
        """
        Executes a keyword-based command.
        """
        utilities = Utilities()
        for new_command in commands:
            command=new_command.split("\t")

            action = command[0]
            locator = command[1] if len(command) > 1 else None
            value = command[2] if len(command) > 2 else None

            try:
                if action == "OPEN":
                    open_url(locator)

                elif action == "PROMPT_ALERT":
                    prompt_alert_accept(locator, value)

                elif action == "ALERT_ACCEPT":
                    alert_accept(locator)

                elif action == "CONFIRMATION_ALERT_DISMISS":
                    confirmation_alert_dismiss(locator)

                elif action == "CONFIRMATION_ALERT_ACCEPT":
                    confirmation_alert_accept(locator)

                elif action == "INPUT":
                    input_text(locator,value)

                elif action == "SELECT":
                    select_radio(locator)

                elif action == "CHECK":
                    select_checkbox(locator)

                elif action == "UNCHECK":
                    deselect_checkbox(locator)

                elif action == "SELECT_FROM_DROPDOWN":
                    select_value_from_dropdown(locator, value)

                elif action == "UPLOAD":
                    upload_file(locator, value, command[3])

                elif action == "CLICK":
                    click_element(locator)

                elif action == "VERIFY":
                    verify_text(value)

                else:
                    utilities.raise_error('Unknown keyword:' + command[0] + ' in the file.Please check.')

            except Exception as e:
                self.logger.error(f"Error executing keyword '{action}': {e}")
