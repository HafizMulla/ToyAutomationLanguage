from Utilities.toy_keyword_implementation import fetching_the_commands, execute_commands, collect_the_commands
from ToyAutomationFramework.Utilities.toy_kewords import ToyKeywordImplementation
from ToyAutomationFramework.toy_methods.setup import Setup
from ToyAutomationFramework.toy_methods.teardown import Teardown
from ToyAutomationFramework.Utilities.Utils import Utilities


class TestRunner:

    def run_test(self,test_file):
        setup = Setup()
        teardown = Teardown()
        toykeywordimplementation = ToyKeywordImplementation()

        setup.setup_environment()

        print(f"Running tests from file: {test_file}")
        user_commands = toykeywordimplementation.fetch_the_commands(test_file)
        if len(user_commands) > 0:
            # execute_commands(user_commands)
            toykeywordimplementation.execute_keyword(user_commands)
        else:
            utils.raise_error("No user command passed. Please check")

        teardown.teardown_environment()

if __name__ == "__main__":
    utils = Utilities()
    runner = TestRunner()
    utils.argument_parser(runner.run_test)
