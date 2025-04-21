from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time

def change_password(driver, current_password, new_password, file):
    """
    Function to change password for a user.
    """
    try:
        # Scroll to the password section
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        # Enter the current password
        old_password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'current_password'))
        )
        old_password_input.clear()
        old_password_input.send_keys(current_password)
        time.sleep(3)  # Ensure time for input reflection

        # Enter the new password
        new_password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'new_password'))
        )
        new_password_input.clear()
        new_password_input.send_keys(new_password)

        # Confirm the new password
        confirm_password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'confirm_password'))
        )
        confirm_password_input.clear()
        confirm_password_input.send_keys(new_password)

        # Click the save button
        save_password_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input.btn-password-update"))
        )
        save_password_button.click()

        # Wait for success message
        try:
            success_password_msg = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.toast-body"))
            )
            if "Password successfully updated" in success_password_msg.text:
                success_message = "Passed:: Password changed successfully.\n"
                file.write(success_message)
                print(success_message)
                return True
            else:
                error_msg = "The new password must be at least 6 characters.\n"
                file.write(error_msg)
                print(error_msg)
                return False
        except TimeoutException:
            error_msg = "Password change failed: No success message displayed.\n"
            file.write(error_msg)
            print(error_msg)
            return False

    except Exception as e:
        error_msg = f"Error during password change: {str(e)}\n"
        file.write(error_msg)
        print(error_msg)
        return False

