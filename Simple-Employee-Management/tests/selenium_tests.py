from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TestUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:5000")  # Change URL based on your setup

    def test_title(self):
        self.assertIn("Employee Management", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
