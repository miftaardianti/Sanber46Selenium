import unittest
from selenium import webdriver


class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.python.org")

    def test_search_in_python_org(self):
         self.driver.get("http://www.python.org")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()