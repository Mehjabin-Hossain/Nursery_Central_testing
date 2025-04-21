from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login(driver, cred, file):
    try:
        driver.get('https://test-nursery-central.rebingtest.com/login')

        email_input = driver.find_element(By.ID, 'email')
        password_input = driver.find_element(By.ID, 'password')

        email_input.clear()
        password_input.clear()

        email_input.send_keys(cred['email'])
        password_input.send_keys(cred['password'])

        password_input.send_keys('\n')  # Submit login form

        time.sleep(2)

        try:
            error_message = driver.find_element(By.CSS_SELECTOR, '.invalid-feedback')
            if error_message.is_displayed():
                error_msg = f"Passed:: Login failed for '{cred['email']}': {error_message.text.strip()}\n"
                file.write(error_msg)
                print(error_msg)
                return False
        except NoSuchElementException:
            pass

        # Check if login was successful
        dropdown_menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".theme-avtar"))
        )

        if dropdown_menu.is_displayed():
            success_msg = f"Passed:: Login successful for '{cred['email']}'\n"
            file.write(success_msg)
            print(success_msg)
            return True
    except (NoSuchElementException, TimeoutException) as e:
        error_msg = f"Error during login for {cred['email']}: {str(e)}\n"
        file.write(error_msg)
        print(error_msg)
        return False


def logout(driver, email, file):
    try:
        # Wait for the dropdown menu and attempt to click it
        dropdown_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".theme-avtar"))
        )

        # Scroll to the dropdown and click it
        driver.execute_script("arguments[0].scrollIntoView(true);", dropdown_menu)
        time.sleep(1)

        try:
            dropdown_menu.click()
        except ElementClickInterceptedException:
            driver.execute_script("arguments[0].click();", dropdown_menu)

        time.sleep(2)

        # Locate the logout form and submit it
        logout_form = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'frm-logout'))
        )
        driver.execute_script("arguments[0].submit();", logout_form)

        time.sleep(2)

        # Generate the custom logout message based on the current user's email passed to the function
        success_msg = f"Passed:: Successfully logged out for '{email}'\n"
        print(success_msg)
        file.write(success_msg)

    except (NoSuchElementException, TimeoutException) as e:
        error_msg = f"Failed to log out for {email}: {str(e)}\n"
        file.write(error_msg)
        print(error_msg)


