import logging
from ToyAutomationFramework.Utilities.Utils import Utilities

utils = Utilities()

class Logger:
    @staticmethod
    def get_logger(self):
    # Configure the logging system
        current_datetime = utils.getcurrentdatetime()
        logging.basicConfig(
                level=logging.INFO,  # Set the logging level
                format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                handlers=[
                    logging.FileHandler("reports/automation_test_"+str(current_datetime)+".log"),
                    logging.StreamHandler()
                ]
            )

        logger = logging.getLogger("ToyAutomationTestSuite")
        return logger
