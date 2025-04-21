import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime  # Importing datetime module to get the current date
import time
import pyautogui

from login_logout_utilities import login, logout  # Importing login and logout functions

SCRIPTS_PATH = r"C:\Users\Mehjabin\Desktop\Selenium-Testing\test-project"  # Path to the scripts folder

# Output file for the Brand Settings script
output_file = os.path.join(SCRIPTS_PATH, 'Brand Settings Output.txt')

# Tester information
tester_name = "Mehjabin Hossain"
test_date = datetime.now().strftime("%d-%m-%Y")  # Get the current date in DD-MM-YYYY format

credentials = [
   # {'email': 'testcompany@example.com', 'password': '12334'},
    {'email': 'floralgarden@yopmail.com', 'password': '12345678'},
]


with open(output_file, 'w') as file:  # Writing to the new output file
    # Display and write tester's name and test date
    header = f"Tester's Name: {tester_name.strip()}\nTest Date: {test_date.strip()}\n\n"
    print(header)  # Print to the terminal
    file.write(header)  # Write to the file

    driver = webdriver.Chrome()

    try:
        driver.maximize_window()

        for cred in credentials:
            if not login(driver, cred, file):
                continue

            try:
                # Wait for the dropdown menu to be present
                dropdown_menu = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".theme-avtar"))
                )

                time.sleep(2)  # Adding some delay to make sure the page is fully loaded

                # Locate the "Settings" button by its visible text
                settings_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//span[text()='Settings']"))
                )

                # Click on the "Settings" button
                ActionChains(driver).move_to_element(settings_button).click().perform()
                time.sleep(2)  # Adding a brief pause to allow actions to complete

                print("Passed:: Successfully clicked on the Settings button.\n")
                file.write("Passed:: Successfully clicked on the Settings button.\n")

                # Now, scroll down to the "Company Settings" link and click it
                company_settings_link = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.LINK_TEXT, "Company Settings"))
                )

                # Scroll into view using JavaScript
                driver.execute_script("arguments[0].scrollIntoView();", company_settings_link)
                time.sleep(2)

                # Click on the "Company Settings" link
                company_settings_link.click()
                time.sleep(2)

                print("Passed:: Successfully clicked on the Company Settings.\n")
                file.write("Passed:: Successfully clicked on the Company Settings.\n")

                # Click on the 'Brand Settings' button
                try:
                    # Wait for the 'Brand Settings' link to be present
                    brand_settings_link = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.LINK_TEXT, "Brand Settings"))
                    )

                    # Click on the 'Brand Settings' link
                    brand_settings_link.click()
                    time.sleep(2)

                    print("Passed:: Successfully clicked on the 'Brand Settings' button.\n")
                    file.write("Passed:: Successfully clicked on the 'Brand Settings' button.\n")

                except Exception as e:
                    error_msg = f"Error while clicking 'Brand Settings': {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)

                # Adding the file upload functionality here
                try:
                    # Wait until the "Choose file here" button is visible
                    choose_file_button = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, ".bg-primary.dark_logo_update"))
                    )

                    # click choose_file_button
                    driver.execute_script("arguments[0].click();", choose_file_button)

                    time.sleep(2)

                    #  the file input element
                    file_input = driver.find_element(By.XPATH, "//input[@type='file']")

                    #  the path to the file
                    file_path_to_upload = r"C:\Users\Mehjabin\Downloads\Florar.png"  # Corrected file path format
                    file_input.send_keys(file_path_to_upload)

                    time.sleep(2)

                    print("Passed:: File uploaded successfully.\n")
                    file.write("Passed:: File uploaded successfully.\n")

                    time.sleep(2)

                    pyautogui.press('esc')  # Close the file dialog

                    # Input text into the Title Text field
                    title_text_input = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.ID, "title_text"))
                    )

                    #  click using JavaScript
                    driver.execute_script("arguments[0].click();", title_text_input)

                    time.sleep(2)

                    # Clear the field and send the new title text
                    title_text_input.clear()
                    new_title_text = "Flora"
                    title_text_input.send_keys(new_title_text)

                    time.sleep(2)

                    print("Passed:: Title text updated successfully.\n")
                    file.write("Passed:: Title text updated successfully.\n")

                    # Now, locate and click the "Save Changes" button
                    try:
                        save_button = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and @value='Save Changes']"))
                        )

                        # Scroll into view and click using JavaScript
                        driver.execute_script("arguments[0].scrollIntoView(true);", save_button)
                        driver.execute_script("arguments[0].click();", save_button)

                        time.sleep(2)  # Wait for any page action to complete

                        print("Passed:: Successfully clicked on Save Changes button.\n")
                        file.write("Passed:: Successfully clicked on Save Changes button.\n")

                    except Exception as e:
                        error_msg = f"Error while clicking the Save Changes button: {str(e)}\n"
                        file.write(error_msg)
                        print(error_msg)

                except Exception as e:
                    error_msg = f"Error during file upload process: {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)

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


