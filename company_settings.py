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



# Output file for the Company Settings script
output_file = os.path.join(SCRIPTS_PATH, 'Company Settings Output.txt')



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


                # Click on the 'Company Settings' Option
                try:
                    # Wait for the 'company Settings' link to be present
                    company_settings_link = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.LINK_TEXT, "Company Settings"))
                    )

                    # Scroll into view using JavaScript and click
                    driver.execute_script("arguments[0].scrollIntoView(true);", company_settings_link)
                    time.sleep(2)

                    # Click on the 'company Settings' Option
                    company_settings_link.click()
                    time.sleep(2)

                    print("Passed:: Successfully clicked on the 'Company Settings' Option.\n")
                    file.write("Passed:: Successfully clicked on the 'Company Settings' Option.\n")

                except Exception as e:
                    error_msg = f"Error while clicking 'Company Settings': {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)



               # Company Name
                try:
                    # Wait for the Company Name input field to be present
                    company_name_input = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "company_name"))
                    )

                    # Scroll into view using JavaScript if necessary
                    driver.execute_script("arguments[0].scrollIntoView(true);", company_name_input)
                    time.sleep(2)

                    # Clear the existing company name
                    company_name_input.clear()

                    # Send the desired Invoice Footer Notes
                    company_name_input.send_keys("FLORAR GARDEN")

                    time.sleep(2)

                    print("Passed:: Successfully entered 'FLORAR GARDEN' as the Company Name.\n")
                    file.write("Passed:: Successfully entered 'FLORAR GARDEN' as the Company Name.\n")


                except Exception as e:
                    error_msg = f"Error while entering Company Name: {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)


                #  Organization number
                try:
                    # Locate the "Invoice Footer Notes" input
                    registration_number_input = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "registration_number"))
                    )

                    # Clear any existing text in the input field
                    registration_number_input.clear()

                    # Send the desired Invoice Footer Notes
                    registration_number_input.send_keys("19999")

                    time.sleep(2)

                    print("Passed:: Successfully entered '199999' as the Organization number.\n")
                    file.write("Passed:: Successfully entered '199999' as the Organization number.\n")

                except Exception as e:
                    error_msg = f"Error while entering Organization number: {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)


                #VAT Number
                try:
                    #  VAT Number input field to be present
                    vat_number_input = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "vat_number"))
                    )


                    # Clear the existing VAT number
                    vat_number_input.clear()

                    # Input a new VAT number
                    vat_number = "2323abc"  # This should trigger a failure as it contains non-numeric characters
                    vat_number_input.send_keys(vat_number)

                    time.sleep(2)

                    # Validation: Check if the VAT number contains only digits
                    if vat_number.isdigit():
                        print(f"Passed:: Successfully inputted valid VAT Number: {vat_number}.\n")
                        file.write(f"Passed:: Successfully inputted valid VAT Number: {vat_number}.\n")
                    else:
                        print(f"Failed:: Invalid VAT Number entered: {vat_number}.\n")
                        file.write(f"Failed:: Invalid VAT Number entered: {vat_number}.\n")


                except Exception as e:
                    error_msg = f"Error during the VAT number input : {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)


                # Telephone Number

                try:
                    #  Telephone Number input field to be present
                    company_telephone_input = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "company_telephone"))
                    )


                    # Clear the existing telephone number
                    company_telephone_input.clear()

                    # Input a new telephone number
                    company_telephone = "+12121BBBB"
                    company_telephone_input.send_keys(company_telephone)

                    time.sleep(2)

                    # Validation: Check if the telephone number contains only digits
                    if company_telephone.isdigit():
                        print(f"Passed:: Successfully inputted valid elephone Number: {company_telephone}.\n")
                        file.write(f"Passed:: Successfully inputted valid telephone Number: {company_telephone}.\n")
                    else:
                        print(f"Failed:: Invalid telephone Number entered: {company_telephone}.\n")
                        file.write(f"Failed:: Invalid telephone Number entered: {company_telephone}.\n")


                except Exception as e:
                    error_msg = f"Error during the elephone number input : {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)


                # Email

                try:
                    #  Email input field to be present
                    email_input = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "company_email"))
                    )

                    # Scroll into view using JavaScript
                    #driver.execute_script("arguments[0].scrollIntoView(true);", email_input)
                    time.sleep(2)

                    # Clear the existing email value
                    email_input.clear()

                    # Input a new email (you can change this value)
                    email = "floral.com"
                    email_input.send_keys(email)

                    # Validation: Check if the email contains '@'
                    if "@" in email:
                        print(f"Passed:: Successfully inputted valid Email: {email}.\n")
                        file.write(f"Passed:: Successfully inputted valid Email: {email}.\n")
                    else:
                        print(f"Failed:: Invalid Email entered (missing '@'): {email}.\n")
                        file.write(f"Failed:: Invalid Email entered (missing '@'): {email}.\n")



                except Exception as e:
                    error_msg = f"Error during the Email input or save process: {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)


                # input Web

                try:
                    #  the Web input field to be present
                    web_input = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "web"))
                    )


                    time.sleep(2)

                    # Clear the existing web value
                    web_input.clear()

                    # Input a new web URL
                    web_url = "$"
                    web_input.send_keys(web_url)


                    print("Passed:: Successfully clicked on the  Web URL.\n")
                    file.write("Passed:: Successfully clicked on the  Web URL.\n")

                except Exception as e:
                    error_msg = f"Error during the Web URL input: {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)


                #Address
                try:
                    # Wait for the Address input field to be present
                    company_address_input = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "company_address"))
                    )

                    time.sleep(2)

                    # Clear the existing company address
                    company_address_input.clear()

                    # Send the desired Invoice Footer Notes
                    company_address_input.send_keys("Mirpur-12")

                    time.sleep(2)

                    print("Passed:: Successfully entered 'Mirpur-12' as the Company Address.\n")
                    file.write("Passed:: Successfully entered 'Mirpur-12' as the Company Address.\n")


                except Exception as e:
                    error_msg = f"Error while entering company address: {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)


                # Country selection
                try:
                    # Scroll to the country dropdown container and wait until it is clickable
                    WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, ".choices[data-type='select-one']"))
                    )
                    country_dropdown = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, ".choices__inner"))
                    )
                    country_dropdown.click()
                    time.sleep(2)

                    # Now focus on the input element within the dropdown that allows for typing/searching
                    country_search_input = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, ".choices__input--cloned"))
                    )
                    country_search_input.click()
                    country_search_input.clear()
                    country_search_input.send_keys("Bangladesh")
                    time.sleep(2)
                    country_search_input.send_keys(Keys.ENTER)

                    print("Passed:: Successfully selected 'Bangladesh' from the country dropdown.\n")
                    file.write("Passed:: Successfully selected 'Bangladesh' from the country dropdown.\n")

                except Exception as e:
                    error_msg = f"Error while selecting the country: {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)


                # City
                try:
                    #  the City Name input field
                    company_city_input = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "company_city"))
                    )

                    driver.execute_script("arguments[0].scrollIntoView(false);", company_city_input)
                    time.sleep(2)

                    # Clear the existing company name
                    company_city_input.clear()

                    # Send the desired Invoice Footer Notes
                    company_city_input.send_keys("DHAKA")

                    time.sleep(2)

                    print("Passed:: Successfully entered 'DHAKA' as the city Name.\n")
                    file.write("Passed:: Successfully entered 'DHAKA' as the city Name.\n")


                except Exception as e:
                    error_msg = f"Error while entering city Name: {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)

                # State
                try:
                    #  the State Name input field
                    company_state_input = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "company_state"))
                    )

                    driver.execute_script("arguments[0].scrollIntoView(true);", company_state_input)

                    # Clear the existing company name
                    company_state_input.clear()

                     # Send the desired Invoice Footer Notes
                    company_state_input.send_keys("State-1")

                    time.sleep(2)

                    print("Passed:: Successfully entered 'State-1' as the State Name.\n")
                    file.write("Passed:: Successfully entered 'State-1' as the State Name.\n")


                except Exception as e:
                    error_msg = f"Error while entering State Name: {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)


                # Zip/Post Code
                try:
                    #  the Zip/Post Code Name input field
                    company_zipcode_input = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "company_zipcode"))
                    )


                    # Clear the existing Zip/Post Code
                    company_zipcode_input.clear()

                    # Send the desired Invoice Footer Notes
                    company_zipcode_input.send_keys("1216")

                    time.sleep(2)

                    print("Passed:: Successfully entered '1216' as the Zip/Post Code.\n")
                    file.write("Passed:: Successfully entered '1216' as the Zip/Post Code.\n")


                except Exception as e:
                    error_msg = f"Error while entering Zip/Post Code: {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)


                # Post Office
                try:
                    #  the Post Office input field
                    company_post_office_input = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "company_post_office"))
                    )


                    # Clear the existing Post Office
                    company_post_office_input.clear()

                    # Send the desired Invoice Footer Notes
                    company_post_office_input.send_keys("Pallabi")

                    time.sleep(2)

                    print("Passed:: Successfully entered 'Pallabi' as the  Post Office.\n")
                    file.write("Passed:: Successfully entered 'Pallabi' as the Post Office.\n")


                except Exception as e:
                    error_msg = f"Error while entering Post Office: {str(e)}\n"
                    file.write(error_msg)
                    print(error_msg)

                # Save Change Button
                try:
                    # Locate the Save Changes button by its XPath
                    save_changes_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//*[@id='useradd-3']/form/div[2]/div/input"))
                    )

                    # Scroll to the Save Changes button using JavaScript to ensure visibility
                    driver.execute_script("arguments[0].scrollIntoView(true);", save_changes_button)
                    time.sleep(1)  # Adding a slight delay to ensure the button becomes fully visible

                    # Click the Save Changes button using JavaScript click as a fallback
                    driver.execute_script("arguments[0].click();", save_changes_button)

                    print("Passed:: Successfully clicked on the 'Save Changes' button.\n")
                    file.write("Passed:: Successfully clicked on the 'Save Changes' button.\n")

                except Exception as e:
                    error_msg = f"Error while clicking on 'Save Changes' button: {str(e)}\n"
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