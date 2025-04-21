import re  # Importing regular expression library
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (NoSuchElementException, TimeoutException, InvalidArgumentException)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time

def update_profile(driver, profile, file):
    """
    Update individual profile details such as name, email, and file.
    """
    name = profile['name']
    email = profile['email']
    upload_file_path = profile['file_path']

    try:
        # Locate and update the name field
        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'name'))
        )
        name_input.clear()
        name_input.send_keys(name)

        # Locate and update the email field
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'email'))
        )
        email_input.clear()
        email_input.send_keys(email)

        # Handle file upload
        choose_file_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.bg-primary.profile_update'))
        )
        choose_file_button.click()

        time.sleep(2)
        pyautogui.press('esc')  # Close the file dialog

        try:
            file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
            file_input.send_keys(upload_file_path)

            save_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="submit"]'))
            )
            save_button.click()

            time.sleep(2)
        except InvalidArgumentException:
            error_msg = f"File not found: {upload_file_path}\n"
            file.write(error_msg)
            print(error_msg)

        # Check for error messages after profile update
        try:
            error_msg_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'span.invalid-feedback.text-danger.text-xs'))
            )
            if error_msg_element.is_displayed():
                error_msg = f"Passed:: Failed to update profile with Name: '{name}' and Email: '{email}'. Error: {error_msg_element.text.strip()}\n"
                file.write(error_msg)
                print(error_msg)
            else:
                # Check if the name contains any numbers
                if re.search(r'\d', name):
                    success_message = f"Failed:: Profile updated with Name: '{name}' and Email: '{email}' Reason:: Title should have only alphabet.\n"
                else:
                    success_message = f"Passed:: Profile updated with Name: '{name}' and Email: '{email}'\n"
                file.write(success_message)
                print(success_message)

        except TimeoutException:
            # If no error message is found, proceed with success messages based on name validation
            if re.search(r'\d', name):
                success_message = f"Failed:: Profile updated with Name: '{name}' and Email: '{email}' Reason:: Title should have only alphabet.\n"
            else:
                success_message = f"Passed:: Profile updated with Name: '{name}' and Email: '{email}'\n"
            file.write(success_message)
            print(success_message)

    except (NoSuchElementException, TimeoutException) as e:
        error_msg = f"Error updating profile with Name: {profile['name']} and Email: {profile['email']}: {str(e)}\n"
        file.write(error_msg)
        print(error_msg)


def update_profiles(driver, profiles, file):
    """
    Update a list of profiles sequentially, one by one.
    """
    for profile in profiles:
        if profile['type'] == 'profile':  # Process only the profiles, ignoring other types
            update_profile(driver, profile, file)


def update_new_profiles(driver, profiles, file):
    """
    Update the profiles as 'new_profile'.
    """
    for profile in profiles:
        if profile['type'] == 'new_profile':  # Process only the new profiles
            update_profile(driver, profile, file)
