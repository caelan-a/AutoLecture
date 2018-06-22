from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep

import settings

def getLinkByText(link_text):
	delay = 15

	try:
	    el_wait = WebDriverWait(delay).until(EC.presence_of_element_located((By.LINK_TEXT, link_text)))
	except TimeoutException:
	    print("Element does not exist or connection too slow")
	    return 
	links = settings.driver.find_elements_by_link_text(link_text)
	assert links, "Link failed: {}".format(link_text)
	return links[0]

def getLinkByPartialText(link_text):
	delay = 15

	try:
	    el_wait = WebDriverWait(settings.driver, delay).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, link_text)))
	except TimeoutException:
	    print("Element does not exist or connection too slow")
	    return 
	links = settings.driver.find_elements_by_partial_link_text(link_text)
	assert links, "Link failed: {}".format(link_text)
	return links[0]

def getLinkByID(link_id):
	delay = 15

	try:
	    el_wait = WebDriverWait(settings.driver,delay).until(EC.presence_of_element_located((By.ID, link_id)))
	except TimeoutException:
	    print ("Loading took too much time!")
	links = settings.driver.find_elements_by_id(link_id)
	assert links, "Link failed: {}".format(link_id)
	return links[0]

def getLinkByXPath(link_xpath):
	delay = 15

	try:
	    el_wait = WebDriverWait(settings.driver, delay).until(EC.presence_of_element_located((By.XPATH, link_xpath)))
	except TimeoutException:
	    print ("Loading took too much time!")
	links = settings.driver.find_elements_by_xpath(link_xpath)
	assert links, "Link failed: {}".format(link_xpath)
	return links[0]

def getLinkByClass(link_class):
	delay = 15

	try:
	    el_wait = WebDriverWait(settings.driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, link_class)))
	except TimeoutException:
	    print ("Loading took too much time!")
	links = settings.driver.find_elements_by_class_name(link_class)
	assert links, "Link failed: {}".format(link_class)
	return links[0]

def checkLinkByText(link_text):
	links = settings.driver.find_elements_by_link_text(link_text)
	if links:
		return True
	else:
		return False