import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_title(self):
        self.driver.get("http://localhost:8000")
        self.assertEqual(self.driver.title, "Hola Mundo")

    def test_heading(self):
        self.driver.get("http://localhost:8000")
        heading = self.driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual(heading.text, "Hola Mundo")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
