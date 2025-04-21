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

from login_logout_utilities import login, logout  # Importing login and logout functions

# Tester information
tester_name = "Mehjabin Hossain"
test_date = datetime.now().strftime("%d-%m-%Y")  # Get the current date in DD-MM-YYYY format

credentials = [
    {'email': 'floralgarden@yopmail.com', 'password': '12345678'},
    #{'email': 'company@example.com', 'password': '123456'},
]

SCRIPTS_PATH = r"C:\Users\Mehjabin\Desktop\Selenium-Testing\test-project"  # Path to the scripts folder


# Output file for the Brand Settings script
output_file = os.path.join(SCRIPTS_PATH, 'System Settings Output.txt')



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


                # After clicking on "Company Settings", scroll down
                try:
                    # Scroll down to the "Currency Symbol Position" section
                    currency_symbol_position_post = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@type='radio' and @value='post']"))
                    )

                    # Scroll
                    driver.execute_script("arguments[0].scrollIntoView();", currency_symbol_position_post)
                    time.sleep(2)

                    # Click on the "Post" radio button
                    currency_symbol_position_post.click()
                    time.sleep(2)

                    print("Passed:: Successfully selected 'Post' as the currency symbol position.\n")
                    file.write("Passed:: Successfully selected 'Post' as the currency symbol position.\n")

                except Exception as e:
                    error_msg = f"Error while selecting currency symbol position: {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)

                # Click on the 'System Settings' button
                try:
                    # Wait for the 'Brand Settings' link to be present
                    system_settings_link = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.LINK_TEXT, "System Settings"))
                    )

                    # Click on the 'system Settings' link
                    system_settings_link.click()
                    time.sleep(2)

                    print("Passed:: Successfully clicked on the 'System Settings' button.\n")
                    file.write("Passed:: Successfully clicked on the 'System Settings' button.\n")

                except Exception as e:
                    error_msg = f"Error while clicking 'System Settings': {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)


                # After selecting the "Currency Symbol Position", now select an option from the "Amount Format" dropdown
                try:
                    # Locate the "Amount Format" dropdown
                    amount_format_dropdown = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "amount_format"))
                    )

                    # Create a Select object for the dropdown
                    select_amount_format = Select(amount_format_dropdown)

                    # Select an option by visible text (you can change this to whatever option you need to select)
                    select_amount_format.select_by_visible_text("00,000.00")

                    time.sleep(3)  # Add a brief pause to allow for selection

                    print("Passed:: Successfully selected '00,000.00' as the amount format.\n")
                    file.write("Passed:: Successfully selected '00,000.00' as the amount format.\n")

                except Exception as e:
                    error_msg = f"Error while selecting amount format: {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)



                # After selecting the "Amount Format", now interact with the "Currency" input field
                try:
                    # Locate the "Currency" input field
                    currency_input = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "site_currency"))
                    )

                    # Clear any existing text in the input field
                    currency_input.clear()

                    # Send the desired currency (for example, let's change it to "USD")
                    currency_input.send_keys("USD")

                    time.sleep(2)  # Add a brief pause to allow for input

                    print("Passed:: Successfully entered 'USD' as the currency.\n")
                    file.write("Passed:: Successfully entered 'USD' as the currency.\n")

                except Exception as e:
                    error_msg = f"Error while entering currency: {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)

                    time.sleep(2)

                # try:
                #     # Locate the "Date Format" dropdown button
                #     date_format_dropdown = WebDriverWait(driver, 10).until(
                #         EC.presence_of_element_located((By.ID, "site_date_format"))
                #     )
                #
                #     # Click the dropdown to display the options
                #     date_format_dropdown.click()
                #
                #     # Wait for the options to be visible and click the desired option (for example, "dd-mm-yyyy")
                #     date_format_option = WebDriverWait(driver, 10).until(
                #         EC.presence_of_element_located((By.XPATH, "//option[text()='dd-mm-yyyy']"))
                #     )
                #
                #     # Click the option
                #     date_format_option.click()
                #
                #     time.sleep(3)  # Optional pause to ensure action is processed
                #
                #     print("Passed:: Successfully selected 'dd-mm-yyyy' as the date format.\n")
                #     file.write("Passed:: Successfully selected 'dd-mm-yyyy' as the date format.\n")
                #
                # except Exception as e:
                #     error_msg = f"Error while selecting date format: {str(e)}\n"
                #     file.write(error_msg)
                #     print(error_msg)

                try:

                    # Locate the "Time Format" dropdown
                    time_format_dropdown = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "site_time_format"))
                    )

                    # Create a Select object for the dropdown
                    select_time_format = Select(time_format_dropdown)

                    # Select an option by visible text (you can change this to whatever option you need to select)
                    select_time_format.select_by_visible_text("10:30 PM")

                    time.sleep(2)

                    print("Passed:: Successfully selected '10:30 PM' as the time format.\n")
                    file.write("Passed:: Successfully selected '10:30 PM' as the time format.\n")

                except Exception as e:
                    error_msg = f"Error while selecting time format: {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)


                try:
                    # Locate the "Invoice Prefix" input field by its ID
                    invoice_prefix_input = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "invoice_prefix"))
                    )

                    # Clear any existing text in the input field
                    invoice_prefix_input.clear()

                    # Send the desired invoice prefix
                    invoice_prefix_input.send_keys("#FGC")

                    time.sleep(2)

                    print("Passed:: Successfully entered '#FGC' as the invoice prefix.\n")
                    file.write("Passed:: Successfully entered '#FGC' as the invoice prefix.\n")

                except Exception as e:
                    error_msg = f"Error while entering invoice prefix: {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)

                # try:
                #     # Locate the "Invoice Starting Number" input field
                #     invoice_starting_number_input = WebDriverWait(driver, 10).until(
                #         EC.presence_of_element_located((By.ID, "invoice_starting_number"))
                #     )
                #
                #     # Ensure the readonly attribute is removed
                #     driver.execute_script("arguments[0].removeAttribute('readonly')", invoice_starting_number_input)
                #
                #     # Clear any existing text in the input field
                #     invoice_starting_number_input.clear()
                #
                #     # Send the desired starting number (e.g., "202")
                #     invoice_starting_number_input.send_keys("202")
                #
                #     time.sleep(2)  # Pause to ensure the input is processed
                #
                #     print("Passed:: Successfully entered '202' as the invoice starting number.\n")
                #     file.write("Passed:: Successfully entered '202' as the invoice starting number.\n")
                #
                # except Exception as e:
                #     error_msg = f"Error while entering invoice starting number: {str(e)}\n"
                #     file.write(error_msg)
                #     print(error_msg)


                try:
                    # Locate the "customer prefix" input field by its ID
                    customer_prefix_input = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "customer_prefix"))
                    )

                    # Clear any existing text in the input field
                    customer_prefix_input.clear()

                    # Send the desired invoice prefix (for example, let's change it to "#CUPE")
                    customer_prefix_input.send_keys("#CUPR")

                    time.sleep(2)  # Add a brief pause to allow for input

                    print("Passed:: Successfully entered '#CUPR' as the customer prefix.\n")
                    file.write("Passed:: Successfully entered '#CUPR' as the customer prefix.\n")

                except Exception as e:
                    error_msg = f"Error while entering customer prefix: {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)


                try:
                    # Locate the "Supplier Prefix" input field by its ID
                    vender_prefix_input = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "vender_prefix"))
                    )

                    # Clear any existing text in the input field
                    vender_prefix_input.clear()

                    # Send the desired Supplier Prefix
                    vender_prefix_input.send_keys("#SUPR")

                    time.sleep(2)

                    print("Passed:: Successfully entered '#CUPR' as the Supplier Prefix.\n")
                    file.write("Passed:: Successfully entered '#CUPR' as the Supplier Prefix.\n")

                except Exception as e:
                    error_msg = f"Error while entering Supplier Prefix: {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)


                try:
                    # Locate the "Vat Type" dropdown by its ID
                    vat_type_dropdown = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "vat_type"))
                    )

                    # Create a Select object for the dropdown
                    select_vat_type = Select(vat_type_dropdown)

                    # Select an option by visible text (you can change this to whatever option you need to select)
                    select_vat_type.select_by_visible_text("Excluded VAT")

                    time.sleep(2)

                    print("Passed:: Successfully selected 'Excluded VAT' as the VAT type.\n")
                    file.write("Passed:: Successfully selected 'Excluded VAT' as the VAT type.\n")

                except Exception as e:
                    error_msg = f"Error while selecting VAT type: {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)


                try:
                    # Locate the "Invoice Footer Notes" input
                    footer_notes_input = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "footer_notes"))
                    )

                    # Clear any existing text in the input field
                    footer_notes_input.clear()

                    # Send the desired Invoice Footer Notes
                    footer_notes_input.send_keys("DEMO NOTES")

                    time.sleep(2)

                    print("Passed:: Successfully entered 'DEMO NOTES' as the Invoice Footer Notes.\n")
                    file.write("Passed:: Successfully entered 'DEMO NOTES' as the Invoice Footer Notes.\n")

                except Exception as e:
                    error_msg = f"Error while entering Invoice Footer Notes: {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)

                # Locate the "Save Changes" button using its XPATH
                try:
                    # Wait for the 'Save Changes' button to be clickable
                    save_changes_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//*[@id='useradd-2']/form/div[2]/div/input"))
                    )

                    # Scroll the button into view to ensure it is visible and clickable
                    driver.execute_script("arguments[0].scrollIntoView(true);", save_changes_button)
                    time.sleep(2)


                    # Now click the button
                    save_changes_button.click()
                    time.sleep(2)

                    print("Passed:: Successfully clicked the 'Save Changes' button.\n")
                    file.write("Passed:: Successfully clicked the 'Save Changes' button.\n")

                except Exception as e:
                    error_msg = f"Error while clicking the 'Save Changes' button: {str(e)}\n"
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

