import os
import unittest
import sys
from selenium import webdriver

username = os.environ.get("LT_USERNAME")
access_key = os.environ.get("LT_ACCESS_KEY")


class FirstSampleTest(unittest.TestCase):

	# setUp runs before each test case
	def setUp(self):
		desired_caps = {
			'LT:Options': {
				"user": username,
				"accessKey": access_key,
				"build": "Python-Selenium-Sample",
				"name": "Python-Selenium-Test",
				"platformName": "Windows 11",
				"selenium_version": "4.0.0"
			},
			"browserName": "Chrome",
			"browserVersion": "latest",
		}

		self.driver = webdriver.Remote(
			command_executor="http://hub.lambdatest.com:80/wd/hub",
			desired_capabilities=desired_caps)


# tearDown runs after each test case

	def tearDown(self):
		self.driver.quit()

	def test_verify_download(self):
			# try:
			driver = self.driver
			driver.get('https://chromedriver.storage.googleapis.com/index.html?path=79.0.3945.36/')
			driver.maximize_window()
			sleep(2)
			driver.find_element_by_xpath("/html/body/table/tbody/tr[]/td[2]/a").click()
			sleep(5)
			if(driver.execute_script("lambda-file-exists=chromedriver_win32.zip") == True):
				driver.execute_script("lambda-status=passed")
				print("Tests are run successfully!")
			else:
				driver.execute_script("lambda-status=failed")
	
if __name__ == "__main__":

	#run testcases
	unittest.main()
