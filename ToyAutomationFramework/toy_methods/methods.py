import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.bidi.cdp import logger
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from ToyAutomationFramework.Utilities.Utils import Utilities

global driver
utils = Utilities()

def launch_browser():
    global driver
    service = Service(ChromeDriverManager().install())
    options = Options()
    # options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1920,1080')
    # options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(service=service, options=options)
    logger.info(f"---Launching browser---")
    return driver


def open_url(url):
    logger.info(f"---Opening URL: {url}---\n")
    driver.get(url)


def click_element(locator):
    logger.info(f"---Clicking element: '{locator}' ---")
    try:
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, locator)))
        driver.execute_script("arguments[0].click();", element)

    except NoSuchElementException:
        logger.warn(f"Error: Element '{locator}' not found. ✖")


def verify_text(expected_text):
    logger.info(f"---Verifying text: '{expected_text}'---")
    if expected_text in driver.page_source:
        utils.verifed_text(f"Verification Passed: '{expected_text}' is present on the page.")
    else:
        utils.raise_error(f"Verification Failed: '{expected_text}' is not present on the page.")


def wait(seconds):
    logger.log("Waiting for " + seconds + " seconds.")
    time.sleep(seconds)


def quit_browser():
    logger.info("Closing browser.")
    driver.quit()


def input_text(locator, text):
    logger.info(f"---Inputting text: '{text}' into element: '{locator}' ---")
    try:
        new_locator = locator.split("#")[1]
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, new_locator))).send_keys(text)

    except NoSuchElementException:
        logger.warn(f"Error: Element '{locator}' not found.")

def upload_file(choose_file_button_locator, file_name, upload_button_locator):
    current_dir = Path(__file__).parent
    testfile_path = str(current_dir).split("..")
    logger.info(f"---Uploading the file {file_name} using the element: '{choose_file_button_locator}' ---")
    file_to_upload = testfile_path[0]+"resources/"+file_name
    choose_file_button_locator = choose_file_button_locator.split("#")[1]
    file_input = driver.find_element(By.ID, choose_file_button_locator)
    file_input.send_keys(file_to_upload)
    driver.find_element(By.CSS_SELECTOR, upload_button_locator).click()
    utils.verifed_text("Successfully uploaded the file: "+file_to_upload)

def select_radio(locator):
    logger.info(f"---Selecting the radio button using element: '{locator}' ---")
    radio_button_locator = locator.split("#")[1]
    radio_button = driver.find_element(By.ID, radio_button_locator)
    radio_button.click()

def select_checkbox(locator):
    logger.info(f"---Selecting the checkbox button using element: '{locator}' ---")
    checkbox_locator = locator.split("#")[1]
    checkbox = driver.find_element(By.ID, checkbox_locator)
    if not checkbox.is_selected():
        # Click the checkbox to select it
        checkbox.click()
    if checkbox.is_selected():
        utils.verifed_text("Checkbox is selected successfully!")
    else:
        utils.raise_error("Failed to select the checkbox.")

def deselect_checkbox(locator):
    logger.info(f"---Deselecting the checkbox button using element: '{locator}' ---")
    checkbox_locator = locator.split("#")[1]
    checkbox = driver.find_element(By.ID, checkbox_locator)
    if checkbox.is_selected():
        # Click the checkbox to deselect it
        checkbox.click()

    if checkbox.is_selected():
        utils.raise_error("Failed to deselect checkbox!")
    else:
        utils.verifed_text("Checkbox is deselected successfully!")


def alert_accept(locator):
    driver.find_element(By.ID, locator.split("#")[1]).click()
    time.sleep(1)  # Wait for alert to appear

    alert = driver.switch_to.alert

    print("Simple Alert Text:", alert.text)
    alert.accept()
    utils.verifed_text("Simple Alert Handled")

def confirmation_alert_accept(locator):
    driver.find_element(By.ID, locator.split("#")[1]).click()
    time.sleep(1)

    alert = driver.switch_to.alert

    print("Confirmation Alert Text:", alert.text)
    alert.accept()
    utils.verifed_text("Confirmation Alert Accepted")

def confirmation_alert_dismiss(locator):
    driver.find_element(By.ID, locator.split("#")[1]).click()
    time.sleep(1)

    alert = driver.switch_to.alert

    print("Confirmation Alert Text:", alert.text)
    alert.dismiss()
    utils.verifed_text("Confirmation Alert Accepted")

def prompt_alert_accept(locator, text):
    driver.find_element(By.ID, locator.split("#")[1]).click()
    time.sleep(1)

    alert = driver.switch_to.alert

    print("Prompt Alert Text:", alert.text)
    alert.send_keys(text)
    alert.accept()
    utils.verifed_text("Prompt Alert Accepted")

def select_value_from_dropdown(locator, value):
    logger.info(f"---Selecting the {value} from the dropdown using element: '{locator}' ---")
    dropdown_element = driver.find_element(By.ID, locator.split("#")[1])

    dropdown = Select(dropdown_element)
    dropdown.select_by_visible_text(value)