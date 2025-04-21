import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import time
import pyautogui
from login_logout_utilities import login, logout  # Importing login and logout functions
from profile_update_utilities import update_profiles, update_new_profiles  # Importing profile update functions
from password_change_utilities import change_password  # Importing password change function
from datetime import datetime  # Importing datetime module to get the current date

# Tester information
tester_name = "Mehjabin Hossain"
test_date = datetime.now().strftime("%d-%m-%Y")

credentials = [
    #{'email': 'demo@example.com', 'password': '12334'},
    {'email': 'superadmin@example.com', 'password': '123456'},
]

SCRIPTS_PATH = r"C:\Users\Mehjabin\Desktop\Selenium-Testing\test-project"  # Path to the scripts folder

output_file = os.path.join(SCRIPTS_PATH, 'Main Super Admin Output.txt')

profiles = [
    {'name': 'Test Admin 123', 'email': 'testadmin@example.com', 'file_path': r'C:\Users\Mehjabin\Downloads\pic2.jpg', 'type': 'profile'},
    {'name': 'MehjabinAdmin', 'email': 'mehjabin.com', 'file_path': r'C:\Users\Mehjabin\Downloads\pic1.png', 'type': 'new_profile'},
    {'name': 'Super Admin', 'email': 'superadmin@example.com', 'file_path': r'C:\Users\Mehjabin\Downloads\pic2.jpg', 'type': 'new_profile'},
]


# Function to retrieve and update password
def get_password_for_email(email, credentials):
    for credential in credentials:
        if credential['email'] == email:
            return credential['password']
    return None

with open(output_file, 'w') as file:  # Writing to the new output file
    # Display and write tester's name and test date
    header = f"Tester's Name: {tester_name}\nTest Date: {test_date}\n\n"
    print(header)  # Print to the terminal
    file.write(header)  # Write to the file

    driver = webdriver.Chrome()

    try:
        driver.maximize_window()

        for cred in credentials:
            current_password = get_password_for_email(cred['email'], credentials)
            if not current_password:
                print(f"No password found for email: {cred['email']}")
                continue

            if not login(driver, {'email': cred['email'], 'password': current_password}, file):
                continue
            try:
                dropdown_menu = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".theme-avtar"))
                )

                if dropdown_menu.is_displayed():
                    dropdown_menu.click()
                    time.sleep(2)

                    my_profile_link = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='/profile']"))
                    )
                    my_profile_link.click()

                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='name']"))
                    )
                    time.sleep(2)

                    # Update profiles first
                    update_profiles(driver, profiles, file)

                    # Update password for Test Admin (first profile)
                    if change_password(driver, current_password, "1234567", file):
                        current_password = "1234567"


                    logout(driver, profiles[0]['email'], file)

                    # Re-login using the new password
                    test_admin_cred = {'email': profiles[0]['email'], 'password': current_password}
                    if not login(driver, test_admin_cred, file):
                        continue

                    dropdown_menu = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, ".theme-avtar"))
                    )

                    try:
                        dropdown_menu.click()
                    except ElementClickInterceptedException:
                        driver.execute_script("arguments[0].click();", dropdown_menu)

                    time.sleep(2)

                    my_profile_link = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='/profile']"))
                    )
                    my_profile_link.click()

                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='name']"))
                    )

                    print(f"Passed:: Navigated to My Profile for {profiles[0]['email']}\n")
                    file.write(f"Passed:: Navigated to My Profile for {profiles[0]['email']}\n")


                    def update_password_in_credentials(email, new_password, credentials):
                        for credential in credentials:
                            if credential['email'] == email:
                                credential['password'] = new_password
                                return True
                        return False

                    # After re-login, update new profiles (MehjabinAdmin and Super Admin)
                    update_new_profiles(driver, profiles, file)

                    # Fetch new password for updating
                    new_password = get_password_for_email(cred['email'], credentials)
                    if new_password and change_password(driver, current_password, new_password, file):
                        current_password = new_password  # Update the local current password variable
                        update_password_in_credentials(cred['email'], new_password, credentials)

                        #print(f"Passed:: Password updated for '{cred['email']}'\n")

                    logout(driver, cred['email'], file)


            except Exception as e:
                error_msg = f"Error during login or post-login process: {str(e)}\n"
                file.write(error_msg)
                print(error_msg)

    except Exception as e:
        error_msg = f"Error in the main block: {str(e)}\n"
        file.write(error_msg)
        print(error_msg)

    finally:
        driver.quit()


