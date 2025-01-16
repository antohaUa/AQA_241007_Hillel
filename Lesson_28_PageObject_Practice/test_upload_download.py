import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

URL = 'http://127.0.0.1:8080'
download_path = os.path.join(os.getcwd(), "downloads")


class TestUploadDownload:

    @pytest.fixture
    def browser(self):
        # Set up Chrome options

        os.makedirs(download_path, exist_ok=True)
        # https://developer.chrome.com/docs/chromedriver/capabilities#set_download_directory
        chrome_options = webdriver.ChromeOptions()
        # mozilla_options = webdriver.FirefoxOptions()
        prefs = {
            "download.default_directory": download_path,  # Set download path
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        }
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(options=chrome_options)
        yield driver
        driver.quit()

    def test_upload_download(self, browser):

        # Open the Flask app URL
        browser.get(URL)  # Flask app URL
        wait = WebDriverWait(browser, 10)

        # File upload operation
        upload_button = wait.until(EC.presence_of_element_located((By.ID, "fileUpload")))  # File input field
        upload_button.send_keys("test.txt")
        print("File uploaded successfully!")

        # Submit the upload form
        submit_button = browser.find_element(By.ID, "uploadSubmit")  # Submit button
        submit_button.click()

        # Wait for the upload confirmation message to appear
        time.sleep(2)

        # File download operation
        download_button = wait.until(EC.element_to_be_clickable((By.ID, "fileDownload")))  # Download button
        download_button.click()
        print("Download initiated...")

        # Wait for the file to download completely
        time.sleep(5)  # Adjust based on file size and internet speed

        # Verify if the file is downloaded
        downloaded_file = os.path.join(download_path, "sample_file.txt")  # Expected downloaded file name
        if os.path.exists(downloaded_file):
            print(f"File downloaded successfully at {downloaded_file}")
        else:
            print("File download failed!")
