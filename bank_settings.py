import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
from selenium.webdriver.support.ui import Select
import time
import pyautogui
from selenium.webdriver.common.keys import Keys


from login_logout_utilities import login, logout  # Importing login and logout functions

# Tester information
tester_name = "Mehjabin Hossain"
test_date = datetime.now().strftime("%d-%m-%Y")  # Get the current date in DD-MM-YYYY format

credentials = [

    {'email': 'floralgarden@yopmail.com', 'password': '12345678'},
]

SCRIPTS_PATH = r"C:\Users\Mehjabin\Desktop\Selenium-Testing\test-project"  # Path to the scripts folder



# Output file for the Bank Settings script
output_file = os.path.join(SCRIPTS_PATH, 'Bank Settings Output.txt')



with open(output_file, 'w') as file:  # Writing to the new output file
    # Display and write tester's name and test date
    header = f"Tester's Name: {tester_name}\nTest Date: {test_date}\n\n"
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

                time.sleep(2)

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


                # Click on the 'Bank Settings' button
                try:
                    # Wait for the 'Bank Settings' link to be present
                    bank_settings_link = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.LINK_TEXT, "Bank Settings"))
                    )

                    # Scroll into view using JavaScript and click
                    driver.execute_script("arguments[0].scrollIntoView();", bank_settings_link)
                    time.sleep(2)

                    # Click on the 'Bank Settings' Option
                    bank_settings_link.click()
                    time.sleep(2)

                    print("Passed:: Successfully clicked on the 'Bank Settings' button.\n")
                    file.write("Passed:: Successfully clicked on the 'Bank Settings' button.\n")

                except Exception as e:
                    error_msg = f"Error while clicking 'Bank Settings': {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)



                # Bank name
                try:
                    # Wait for the Company Name input field to be present
                    bank_name_input = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "bank_name"))
                    )

                    time.sleep(2)

                    # Clear the existing bank name
                    bank_name_input.clear()

                    # Send the desired Invoice Footer Notes
                    bank_name_input.send_keys("Abc Bank")

                    time.sleep(2)

                    print("Passed:: Successfully entered 'Abc Bank' as the Bank Name.\n")
                    file.write("Passed:: Successfully entered 'Abc Bank' as the Bank Name.\n")


                except Exception as e:
                    error_msg = f"Error while entering Bank Name: {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)

                # Account Number
                try:
                    # Locate the Account Number input field
                    account_number_input = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "bank_account_no"))
                    )

                    # Clear any existing value in the Account Number field
                    account_number_input.clear()

                    # Input a new Account Number (you can change this value)
                    account_number = "7777ab"  # This should trigger a failure as it contains non-numeric characters
                    account_number_input.send_keys(account_number)

                    time.sleep(2)

                    # Validation: Check if the Account Number contains only digits
                    if account_number.isdigit():
                        print(f"Passed:: Successfully inputted valid Account Number: {account_number}.\n")
                        file.write(f"Passed:: Successfully inputted valid Account Number: {account_number}.\n")
                    else:
                        print(f"Failed:: Invalid Account Number entered: {account_number}.\n")
                        file.write(f"Failed:: Invalid Account Number entered: {account_number}.\n")

                except Exception as e:
                    error_msg = f"Error during the Account Number input: {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)

                # Company Identification Number
                try:
                    # Wait for the Company Identification Number input field to be present
                    company_identification_number_input = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "company_identification_number"))
                    )

                    time.sleep(2)

                    # Clear the existing Company Identification Number
                    company_identification_number_input.clear()

                    # Send the desired Invoice Footer Notes
                    company_identification_number_input.send_keys("99999")

                    time.sleep(2)

                    print("Passed:: Successfully entered '99999' as the Company Identification Number.\n")
                    file.write("Passed:: Successfully entered '99999' as the Company Identification Number.\n")


                except Exception as e:
                    error_msg = f"Error while entering Company Identification Number: {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)

                # Click the 'Save Changes' button under the Bank Settings section
                try:
                    # Locate the 'Save Changes' button using its XPath
                    save_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//*[@id='useradd-4']/form/div[2]/div/input"))
                    )

                    # Scroll into view and click using JavaScript
                    driver.execute_script("arguments[0].scrollIntoView(true);", save_button)
                    driver.execute_script("arguments[0].click();", save_button)

                    time.sleep(2)
                    print("Passed:: Successfully clicked on the 'Bank Settings Save Changes' button.\n")
                    file.write("Passed:: Successfully clicked on the 'Bank Settings Save Changes' button.\n")


                except Exception as e:
                    error_msg = f"Error while clicking 'Bank Settings Save Changes': {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)


                # Click on the 'Invoice Print Settings' button
                try:
                    # Wait for the 'Invoice Print Settings' link to be present
                    invoice_print_settings_link = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.LINK_TEXT, "Invoice Print Settings"))
                    )

                    # Scroll into view using JavaScript and click
                    driver.execute_script("arguments[0].scrollIntoView();", invoice_print_settings_link)
                    time.sleep(2)

                    # Click on the 'Invoice Print Settings' link
                    invoice_print_settings_link.click()
                    time.sleep(2)

                    print("Passed:: Successfully clicked on the 'Invoice Print Settings' button.\n")
                    file.write("Passed:: Successfully clicked on the 'Invoice Print Settings' button.\n")

                except Exception as e:
                    error_msg = f"Error while clicking 'Invoice Print Settings': {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)

                # File upload in Invoice Print Settings
                try:
                    # Wait for the file input to be present
                    file_input = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "invoice_logo"))
                    )

                    time.sleep(2)

                    # Provide the file path to upload (replace with the actual path of your file)
                    file_path = r"C:\Users\Mehjabin\Downloads\Florar.png"
                    file_input.send_keys(file_path)

                    time.sleep(2)

                    pyautogui.press('esc')

                    print("Passed:: Successfully uploaded the file in the Invoice Print Settings.\n")
                    file.write("Passed:: Successfully uploaded the file in the Invoice Print Settings.\n")

                except Exception as e:
                    error_msg = f"Error while uploading the file: {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)

                #Click the 'Save Changes' button after uploading the file
                try:
                    save_changes_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//*[@id='setting-form']/div[2]/div/input"))
                    )

                    # Scroll into view and click using JavaScript to ensure it's in view
                    driver.execute_script("arguments[0].scrollIntoView(true);", save_changes_button)
                    driver.execute_script("arguments[0].click();", save_changes_button)

                    time.sleep(2)  # Wait for the action to complete

                    print("Passed:: Successfully clicked on the 'Save Changes' button after uploading the file.\n")
                    file.write(
                        "Passed:: Successfully clicked on the 'Save Changes' button after uploading the file.\n")

                except Exception as e:
                    error_msg = f"Error while clicking 'Save Changes' button: {str(e)}\n"
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