import sys, os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

sys.path.append(os.path.dirname(__file__))

import settings
import datetime
import time as timelib
from time import sleep
from SubjectSchedule import SubjectSchedule

import LinkUtil
import LectureHandler

def goToLms(username, password):
	print("Logging in..\n")

	settings.driver.get("https://app.lms.unimelb.edu.au")

	if settings.driver.find_elements_by_id('user_id'):
		elem_user = settings.driver.find_element_by_id('user_id')
		elem_user.clear()
		elem_user.send_keys(username)

		elem_pass = settings.driver.find_element_by_id('password')
		elem_pass.clear()
		elem_pass.send_keys(password)

		elem_user.send_keys(Keys.RETURN)
	else:
		print("Already logged in..")

	settings.driver.get("https://app.lms.unimelb.edu.au/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_5_1")

def isSummerTimeTable():
	#	Insert logic to check for summer timetable
	return false

def goToSummerTimeTable():
	subject_schedules_and_info = {}
	return subject_schedules_and_info

def goToTimeTable(username, password):
	timetable_url = 'https://prod.ss.unimelb.edu.au/student/SM/StudentTtable10.aspx?r=%23UM.STUDENT.APPLICANT&f=%24S1.EST.TIMETBL.WEB&sid=911038&cfn=s1prod\%20direct&tkn=RcrNMK3nQu2LTgKwSg9WWo6fN573IbZH'
	#timetable_url = 'file:///C:/Users/cande/Desktop/timetable_page.html'
	settings.driver.get(timetable_url)

	USERNAME = username
	PASSWORD = password

	if settings.driver.find_elements_by_id('ctl00_Content_txtUserName_txtText'):
		elem_user = settings.driver.find_element_by_id('ctl00_Content_txtUserName_txtText')
		elem_user.clear()
		elem_user.send_keys(USERNAME)

		elem_pass = settings.driver.find_element_by_id('ctl00_Content_txtPassword_txtText')
		elem_pass.clear()
		elem_pass.send_keys(PASSWORD)

		elem_user.send_keys(Keys.RETURN)
	else:
		print("Already logged in..")

def getOnlineTimeTable():
	subject_schedules_and_info = {}

	info_root_raw = LinkUtil.getLinkByXPath('//*[@id="ctl00_Content_ctlFilter_CboStudyPeriodFilter_elbList"]')
	info_raw_list = info_root_raw.find_elements_by_xpath('*')
	info_raw = ""

	for i in info_raw_list:	
		if i.get_attribute("selected") == "true":
			info_raw = i.get_attribute('value')
	info_raw = info_raw.split('-')

	print(info_raw)

	#	Get semester/year info
	info = {}
	info["year"] = info_raw[0]
	info["semester"] = info_raw[1][-1]
	info["start_date"] = datetime.datetime.strptime(info_raw[2],"%b %d, %Y")

	subject_schedules_and_info["info"] = info

	timetable_root = LinkUtil.getLinkByXPath('//*[@id="ctl00_Content_ctlNav_ctl04"]')
	subject_list = timetable_root.find_elements_by_xpath('*') # Gives list of immediate children

	for s in subject_list:
		subject_schedule = SubjectSchedule()
		subject_schedule.code = s.find_element_by_class_name('cssTtableSspNavMasterSpkInfo2').get_attribute('innerText').strip()
		subject_schedule.title = s.find_element_by_class_name('cssTtableSspNavMasterSpkInfo3').get_attribute('innerText').strip()

		#	Fetch session info, eg workshop, practical, lecture times
		session_list = s.find_elements_by_class_name('cssTtableSspNavActvGrid')[0].find_elements_by_xpath('*')[0].find_elements_by_xpath('*') 
		del session_list[0] # As first index is junk

		sessions = {}

		for session in session_list:
			session_instance = {} #	Dictionary for storing parsed data and passing off to SubjectSchedule object

			session_type_number_raw = session.find_element_by_class_name('cssTtableSspNavActvNm').get_attribute('innerText').strip()

			session_instance["type"] = session_type_number_raw[:-2]
			session_instance["number"] = session_type_number_raw[-1:]

			# Parse day_time raw info
			session_time_day_raw = session.find_element_by_class_name('cssTtableNavMainWhen').find_element_by_class_name('cssTtableNavMainContent').get_attribute('innerText').strip()

			for i in range(0,len(session_time_day_raw)):
				if session_time_day_raw[i].isdigit():
					session_instance["day"] = session_time_day_raw[:i].strip()
					times = session_time_day_raw [i:].split('-') # split times into list of [start_time, end_time]
					session_instance["start_time"] = times[0]
					session_instance["end_time"] = times[1]
					break;

			location_raw = session.find_element_by_class_name('cssTtableNavMainWhere').get_attribute('innerText')
			session_instance["location"] = location_raw[len("Location:"):].strip()

			if session_instance["type"] not in sessions:
				sessions[session_instance["type"]] = []
				sessions[session_instance["type"]].append(session_instance)
			elif session_instance["type"] in sessions:
				sessions[session_instance["type"]].append(session_instance)

		subject_schedule.addSessions(sessions) 

		subject_schedules_and_info[subject_schedule.code] = subject_schedule
	return subject_schedules_and_info

def getLmsSubjectInfo():
	subjects = {} # each element is a list of info

	#//*[@id="_4_1termCourses_noterm"]/ul/li[1]/a
	html_list = LinkUtil.getLinkByXPath('//*[@id="_158_1termCourses_noterm"]/ul')

	el_list = html_list.find_elements_by_css_selector('[target^=_top]')

	for e in el_list:
		subject_info = {}

		# Extract code and title
		code_title = e.get_attribute('innerText')
		code_title = code_title.split(':')

		code_year_sem = code_title[0].split('_')
		subject_info["code"] = code_year_sem[0]
		subject_info["year"] = int(code_year_sem[1])
		subject_info["semester"] = int(code_year_sem[2][-1])

		title = code_title[1]  
		subject_info["title"] = title[1:] # Remove space at start of string

		# Extract id from course_id_raw
		raw_id = e.get_attribute('href')
		id_identifier = "Course&id="
		id_end_indentifier = "&url="
		id_start = raw_id.find(id_identifier) + len(id_identifier)
		id_end = raw_id.find(id_end_indentifier)

		subject_info["course_id"] = raw_id[id_start:id_end]
		
		subjects[subject_info["code"]] = subject_info

	return subjects

def getOnlineLectures(subject, date_last_indexed):
	#	Optimise using 2nd argument to only space down required amount
	#
	print("Finding lectures...\n")

	# settings.driver.get("https://content.lecture.unimelb.edu.au/ess/portal/section/"+subject.CODE) # Link to clean echo page
	lectures_url = "https://app.lms.unimelb.edu.au/webapps/blackboard/content/launchLink.jsp?course_id={}&tool_id=_4009_1&tool_type=TOOL&mode=view&mode=reset".format(subject.course_id)

	settings.driver.get(lectures_url)

	# Navigate to frame with echoes-list
	sleep(1)
	frame = LinkUtil.getLinkByXPath('//*[@id="contentFrame"]')
	settings.driver.switch_to.frame(frame)
	frame = LinkUtil.getLinkByXPath('/html/body/iframe')
	settings.driver.switch_to.frame(frame)
	frame = LinkUtil.getLinkByXPath('/html/body/div/iframe')
	settings.driver.switch_to.frame(frame)

	# Get echoes list
	html_list = LinkUtil.getLinkByXPath('//*[@id="echoes-list"]')
	items = html_list.find_elements_by_tag_name("li")

	# Focus on element in list to be able to scroll with keyboard
	actions = ActionChains(settings.driver);
	actions.move_to_element(items[0]).click()
	actions.click()
	actions.perform();

	# Hold space to scroll down and generate list elements, do so in groups of 4 to collect generated timestamps
	action_key_down_space = ActionChains(settings.driver).key_down(Keys.SPACE)
	action_key_up_space = ActionChains(settings.driver).key_up(Keys.SPACE)

	lectures = []

	scroll_duration = 4
	
	endtime = timelib.time() + scroll_duration
	while True:	
		action_key_down_space.perform()

		if timelib.time() > endtime:
			action_key_up_space.perform()
			break

	sleep(1)

	lectures = []

	elements = html_list.find_elements_by_tag_name("li")
	for e in elements:
		#	Extract url from element
		src_str = e.find_element_by_class_name('thumbnail').get_attribute('src')
		start_i = 0 # Start index of video id in src_str
		end_i = 0
		count = 0
		for i in range(1,len(src_str)):
			if src_str[i] == '/':
				count += 1
				if count == 4:
					start_i = i+1
				if count == 7:
					end_i = i

		video_id = src_str[start_i:end_i]
		
		url = 'https://download.lecture.unimelb.edu.au//{}/audio-vga.m4v?download'.format(video_id)

		#	Extract date and time
		date_time_str = e.find_element_by_class_name('echo-date').get_attribute('innerText')
		dt = datetime.datetime.strptime(date_time_str,"%B %d %I:%M %p").replace(2017)

		time = dt.time()
		date = dt.date()

		lec_new = LectureHandler.Lecture(url, date, time)
		lectures.append(lec_new)

	print("Number of lectures available: {}".format(len(lectures)))
	assert lectures, "List of available lectures is empty! Exiting.."

	lectures.reverse() # So earliest lectures are at beginning

	return lectures