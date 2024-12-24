from datetime import datetime
from selenium.webdriver.common.bidi.cdp import logger
import sys
import os
from colorist import red, green
import argparse

class Utilities:

    def __init__(self):
        pass

    def raise_error(self, text):
        logger.warn(red(text))
        sys.exit(1)

    def verifed_text(self, text):
        logger.warn(green(text))

    def read_predefine_keywords_from_keyword_file(self, file_path):
        logger.info("Reading keyword from the predefine keyword file")
        try:
            file = open(file_path, "r")
            content = file.read().rstrip()
            if not content:
                self.raise_error("No keywords present in the predefine keyword file.Please check")
            return content

        except FileNotFoundError:
            self.raise_error(f"Error: The keyword file at {file_path} was not found.")


    def read_commands_from_test_file(self, file_path):
        logger.info("Reading keywords from the test file")
        try:
            with open(file_path, "r") as file:
                return [line.strip() for line in file.readlines()]

        except FileNotFoundError:
            self.raise_error(f"Error: The file at {file_path} was not found.")
        except IOError:
            self.raise_error(f"Error: An I/O error occurred while accessing the file {file_path}.")
        except Exception as e:
            self.raise_error(f"An unexpected error occurred: {e}")
        finally:
            try:
                file.close()
            except NameError:
                pass

    def getcurrentdatetime(self):
        current_datetime = datetime.now()
        current_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S").replace(" ","_")
        return current_datetime

    def argument_parser(self, run_test):
        # Set up the argument parser
        parser = argparse.ArgumentParser(description="Run test files.")
        test_folder = "test/"
        parser.add_argument(
            "test_file",
            type=str,
            nargs="?",  # Makes the argument optional
            help="Name of the test file to run (e.g., Test1). If not provided, all tests in the 'Test' folder will run."
        )

        # Parse the arguments
        args = parser.parse_args()

        if args.test_file:
            run_test(test_folder + args.test_file)
        else:
            # If no file is specified, run all files in the 'test' folder
            if os.path.exists(test_folder) and os.path.isdir(test_folder):
                test_files = [f for f in os.listdir(test_folder) if os.path.isfile(os.path.join(test_folder, f))]
                for test_file in test_files:
                    run_test(os.path.join(test_folder, test_file))
            else:
                self.raise_error(f"Error: The folder '{test_folder}' does not exist.")