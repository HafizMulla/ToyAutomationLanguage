from ToyAutomationFramework.loggenerator.logger import Logger
from ToyAutomationFramework.toy_methods.methods import quit_browser

class Teardown:

    def teardown_environment(self):
        logger = Logger.get_logger(__name__)
        logger.info("Clearing the test suite...")
        quit_browser()
