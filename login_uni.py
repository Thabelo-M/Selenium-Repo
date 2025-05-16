import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TestLoginPopup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        file_path = os.path.abspath("Login_Page.html")
        self.driver.get("file://" + file_path)

    def test_un_popup(self):
        driver = self.driver
        driver.find_element(By.CLASS_NAME, "email").send_keys("Selenium25@gmail.com")
        driver.find_element(By.CLASS_NAME, "password").send_keys("Y0uMade1t&3&&")
        driver.find_element(By.ID, "login-btn").click()
        #Wait for the popup to appear
        wait = WebDriverWait(driver, 10)
        popup = wait.until(EC.visibility_of_element_located((By.ID, "login-popup")))
        popup_message = driver.find_element(By.ID, "login-popup-message").text
        #Assertions
        self.assertTrue(popup.is_displayed(), "Login did not display the popup")
        self.assertIn("successfully", popup_message.lower(), f"Unexpected message: {popup_message}")
        time.sleep(5)

        def tearDown(self):
            self.driver.quit()
    if __name__ == "__main__":
        unittest.main()