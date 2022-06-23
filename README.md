# How to verify file download in automation test in Python-selenium on [LambdaTest](https://www.lambdatest.com/?utm_source=github&utm_medium=repo&utm_campaign=Python-selenium-verify-download)

If you want to verify file download in automation test in Python-selenium on LambdaTest, you can follow the below steps. You can refer to sample test repo [here](https://github.com/LambdaTest/python-selenium-sample).

# Steps:


## Step 1: Add test case

You can use the following testcase to verify download in automation test:

```python

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
```

## Step 2: Run your test

```bash
python lambdatest.py
```

# Links:

[LambdaTest Community](http://community.lambdatest.com/)

