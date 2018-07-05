from selenium import webdriver
import logging
from selenium.webdriver.remote.remote_connection import LOGGER

global driver

def startBrowser():
	global driver
	LOGGER.setLevel(logging.WARNING)
	#	Start Chrome
	options = webdriver.ChromeOptions()
	options.add_argument('headless')
	options.add_argument('--log-level=3')
	options.add_argument("--window-size=1920,1080")
	driver = webdriver.Chrome(chrome_options=options)
	# driver = webdriver.Chrome()

def closeBrowser():
	driver.quit()



