from ToyAutomationFramework.loggenerator.logger import Logger
from ToyAutomationFramework.toy_methods.methods import launch_browser


class Setup:
    def setup_environment(self):
        logger = Logger.get_logger(__name__)
        logger.info("Initializing test suite...")
        launch_browser()


