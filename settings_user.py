import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select  # Importing Select for dropdown handling
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from login_logout_utilities import login, logout  # Importing login and logout functions
from datetime import datetime  # Importing datetime module to get the current date

SCRIPTS_PATH = r"C:\Users\Mehjabin\Desktop\Selenium-Testing\test-project"
output_file = os.path.join(SCRIPTS_PATH, 'Settings User Output.txt')


# Tester information
tester_name = "Mehjabin Hossain"
test_date = datetime.now().strftime("%d-%m-%Y")  # Get the current date in DD-MM-YYYY format

credentials = [
    {'email': 'floralgarden@yopmail.com', 'password': '12345678'},
   # {'email': 'company@example.com', 'password': '123456'},
]


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
                # Waiting for the dropdown menu to be present
                dropdown_menu = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".theme-avtar"))
                )

                time.sleep(2)

                # Locating the "Settings" button by its visible text
                settings_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//span[text()='Settings']"))
                )

                # Clicking on the "Settings" button
                ActionChains(driver).move_to_element(settings_button).click().perform()
                time.sleep(2)

                print("Passed:: Successfully clicked on the Settings button.\n")
                file.write("Passed:: Successfully clicked on the Settings button.\n")

                # Locating the "User" button
                user_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'dash-link') and text()='User']"))
                )

                # Clicking on the "User" button
                ActionChains(driver).move_to_element(user_button).click().perform()
                time.sleep(2)

                print("Passed:: Successfully clicked on the User button.\n")
                file.write("Passed:: Successfully clicked on the User button.\n")

                # Locating the "Create" button
                create_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//button[@data-ajax-popup='true' and @data-bs-original-title='Create New User']"))
                )

                # Clicking on the "Create" button
                ActionChains(driver).move_to_element(create_button).click().perform()
                time.sleep(2)

                print("Passed:: Successfully clicked on the Create button.\n")
                file.write("Passed:: Successfully clicked on the Create button.\n")

                # Locating the "Name" input field
                name_input = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@id='name' and @name='name']"))
                )

                # Inputting text into the "Name" field
                name_input.send_keys("User Testing")
                time.sleep(2)

                print("Passed:: Successfully entered name into the Name field.\n")
                file.write("Passed:: Successfully entered name into the Name field.\n")

                # Locating the "Email" input field
                email_input = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@id='email' and @name='email']"))
                )

                # Email to be used for creating a new user
                email_to_create = "TestUser@yopmail.com"

                # Entering text into the "Email" field
                email_input.send_keys(email_to_create)
                time.sleep(2)

                print("Passed:: Successfully entered email into the Email field.\n")
                file.write("Passed:: Successfully entered email into the Email field.\n")

                # Locating the "User Role" dropdown field
                role_dropdown = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//select[@id='role' and @name='role']"))
                )

                #  Selecting the "Test Collector" option
                select = Select(role_dropdown)
                select.select_by_index(1)
                time.sleep(2)

                print("Passed:: Successfully selected 'Test Collector1' from the User Role dropdown.\n")
                file.write("Passed:: Successfully selected 'Test Collector1' from the User Role dropdown.\n")

                # Locating the checkbox for "Can be a cleaner"
                cleaner_checkbox = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//label[@for='can_cleaner']"))
                )

                # Clicking on the "Can be a cleaner" checkbox
                cleaner_checkbox.click()
                time.sleep(2)

                print("Passed:: Successfully selected 'Can be a cleaner' checkbox.\n")
                file.write("Passed:: Successfully selected 'Can be a cleaner' checkbox.\n")

                # Locating the "Create" button
                submit_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//input[@type='submit' and @value='Create']"))
                )

                # Clicking on the "Create" button
                submit_button.click()
                time.sleep(2)

                print("Passed:: Successfully clicked on the Create button to submit the form.\n")
                file.write("Passed:: Successfully clicked on the Create button to submit the form.\n")

                time.sleep(2)

                #  the success or error message
                try:
                    notification_message = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, ".toast-body"))
                    )

                    # the text of the notification message
                    message_text = notification_message.text

                    if "User successfully added" in message_text:
                        result_message = "Passed: User was successfully created.\n"
                    # elif "The email has already been taken" in message_text:
                    #     result_message = "Passed:: The email has already been taken.\n"
                    #
                    #     print(result_message)
                    #     file.write(result_message)
                    #
                    #     # Quit the process as the email is already taken
                    #     driver.quit()
                    #     exit()


                    else:
                        result_message = "Passed:: The email has already been taken.\n"

                    # Printing and writing the result message only once
                    print(result_message)
                    file.write(result_message)



                except Exception as e:
                    error_msg = f"Failed to retrieve notification message: {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)

                # Finding the newly created user and clicking the Edit button using the same email
                try:

                    #  the table row containing the newly created user's email
                    user_row = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, f"//tr[td[text()='{email_to_create}']]"))
                    )

                    # Scroll to the element before clicking
                    edit_button = user_row.find_element(By.XPATH, ".//i[@class='ti ti-edit text-white']")
                    driver.execute_script("arguments[0].scrollIntoView(true);", edit_button)
                    time.sleep(2)

                    # Clicking the edit button
                    driver.execute_script("arguments[0].click();", edit_button)
                    time.sleep(2)

                    print("Passed:: Successfully clicked on the Edit button for the last created user.\n")
                    file.write("Passed:: Successfully clicked on the Edit button for the last created user.\n")

                    #  new values in the "Name" and "Email" fields For Edit
                    try:
                        #  the "Name" input field
                        name_input_edit = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, "//input[@id='name' and @name='name']"))
                        )

                        # Clearing the current value and inputting new text into the "Name" field
                        name_input_edit.clear()
                        name_input_edit.send_keys("Updated Test")
                        time.sleep(2)

                        print("Passed:: Successfully updated the Name field.\n")
                        file.write("Passed:: Successfully updated the Name field.\n")

                        # Locate the "Email" input field
                        email_input_edit = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, "//input[@id='email' and @name='email']"))
                        )

                        # Clearing the current value and inputting new text into the "Email" field
                        email_input_edit.clear()
                        email_input_edit.send_keys("updatedUserTest@yopmail.com")
                        time.sleep(2)

                        print("Passed:: Successfully updated the Email field.\n")
                        file.write("Passed:: Successfully updated the Email field.\n")

                        # Update the User Role dropdown and select a different role
                        try:
                            # Locating the "User Role" dropdown field
                            role_dropdown_edit = WebDriverWait(driver, 10).until(
                                EC.presence_of_element_located((By.XPATH, "//select[@id='role' and @name='role']"))
                            )

                            # Print all available options in the dropdown
                            select_edit = Select(role_dropdown_edit)
                            select_edit.select_by_index(2)
                            available_options = [option.text for option in select_edit.options]

                            time.sleep(2)

                            print("Passed:: Successfully selected 'collector' from the User Role dropdown.\n")
                            file.write("Passed:: Successfully selected 'collector' from the User Role dropdown.\n")

                            #  the "Can be a cleaner" checkbox
                            try:
                                # Locating the "Can handle production task" checkbox
                                task_checkbox_edit = WebDriverWait(driver, 10).until(
                                    EC.presence_of_element_located((By.XPATH, "//label[@for='handle_task']"))
                                )

                                #  the "Can handle production task" checkbox
                                task_checkbox_edit.click()
                                time.sleep(2)

                                print("Passed:: Successfully selected 'Can handle production task' checkbox.\n")
                                file.write("Passed:: Successfully selected 'Can handle production task' checkbox.\n")


                            except Exception as e:
                                error_msg = f"Failed to select 'Can handle production task' checkbox: {str(e)}\n"
                                file.write(error_msg)
                                print(error_msg)

                            # Clicking the "Update" button to save the changes
                            try:
                                update_button = WebDriverWait(driver, 10).until(
                                    EC.presence_of_element_located(
                                        (By.XPATH, "//input[@type='submit' and @value='Update']"))
                                )

                                update_button.click()
                                time.sleep(2)

                                print("Passed:: Successfully clicked on the 'Update button' to save changes.\n")
                                file.write("Passed:: Successfully clicked on the 'Update button' to save changes.\n")

                            except Exception as e:
                                error_msg = f"Failed to click on the 'Update button': {str(e)}\n"
                                file.write(error_msg)
                                print(error_msg)


                        except Exception as e:
                            error_msg = f"Failed to update the User Role or Checkbox: {str(e)}\n"
                            file.write(error_msg)
                            print(error_msg)



                    except Exception as e:
                        error_msg = f"Failed to update the Name or Email field: {str(e)}\n"
                        file.write(error_msg)
                        print(error_msg)


                except Exception as e:
                        error_msg = f"Failed to click on the Edit button for the user with email {email_to_create}: {str(e)}\n"
                        file.write(error_msg)
                        print(error_msg)



                except Exception as e:
                    error_msg = f"Failed to click on the Edit button: {str(e)}\n"
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