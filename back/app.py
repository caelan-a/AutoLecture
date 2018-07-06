import os, sys
sys.path.append(os.path.dirname(__file__))

from User import User
import settings
import LinkUtil
from LectureHandler import LectureHandler, Lecture
import LmsNavigator
import download
import pickle
from Subject import Subject
from SubjectSchedule import SubjectSchedule

USER_SAVE_PATH = "save\\user.pkl"


__author__ = "Caelan Anderson"
__copyright__ = "Copyright 2017"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Caelan Anderson"
__email__ = "caelan.anderson@student.unimelb.edu.au"
__status__ = "Production"

class AutoLectureApp():	
	def isNewUser(self):
		fname = USER_SAVE_PATH
		exists = os.path.isfile(fname) 
		return not exists

	def loadUser(self):
		self.user = pickle.load(open(USER_SAVE_PATH, "rb"))

	def printLecturesForSubject(self,i):
		for l in settings.userData.subjects[i].lectureCalender.getLecturesFromWeeks(settings.userData.subjects[1].lectureCalender.weeks_scheduled):
			print("Week {}, Lecture {}".format(l.week_num, l.day_num))

	def setLoginInfo(self, username, password):
		self.user.setLoginInfo(username, password)

	def getLoginInfo(self):
		return [self.user.username, self.user.password]

	def setUniversity(self, uni):
		self.user.setUniversity(uni)

	def startBrowser(self):
		settings.startBrowser()

	def closeBrowser(self):
		settings.closeBrowser()

	def getTimeTable(self):
		if self.user.timetable == None:
			settings.startBrowser()
			self.user.timetable = LmsNavigator.getTimeTable("caelana", "cael1998", 2)

			timetable_info = self.user.timetable.pop("info")
			if int(timetable_info["semester"]) != self.user.current_term or int(timetable_info["year"]) != self.user.current_year:
				print("Wrong timetable (Sem {} {}) downloaded. AutoLecture needs Sem {} {}".format(timetable_info["semester"],timetable_info["year"],self.user.current_term, self.user.current_year))

			self.user.save()
		else:
			pass

	def getSubjectsToAddScheduleInfo(self):
		for subject in self.subjects_to_add["current"]:
			if self.user.timetable != None:
				subject.setSubjectSchedule(self.user.timetable[subject_key])

		for subject in self.subjects_to_add["past"]:
			pass
	def fillSubjectsToAdd(self, info_subjects_to_add):
		info = info_subjects_to_add["current"]
		for subject_key in info:
			subject = Subject(info[subject_key]["title"], info[subject_key]["semester"],info[subject_key]["year"],info[subject_key]["code"], info[subject_key]["course_id"])
			self.subjects_to_add["current"].append(subject)

		info = info_subjects_to_add["past"]
		for subject_key in info:
			subject = Subject(info[subject_key]["title"], info[subject_key]["semester"],info[subject_key]["year"],info[subject_key]["code"], info[subject_key]["course_id"])
			self.subjects_to_add["past"].append(subject)

	def getSubjectLMSInfo(self):
		"""Return subjects in a dictionary of 2 elements"""
		if self.user.raw_subject_info == None:
			username = self.getLoginInfo()[0]
			password = self.getLoginInfo()[1]

			self.startBrowser()
			LmsNavigator.goToLms(username, password)
			info_subjects = LmsNavigator.getLmsSubjectInfo()

			info_current_subjects = {}
			info_past_subjects = {}

			for subject in info_subjects:
				if info_subjects[subject].get("semester") == self.user.current_term and info_subjects[subject].get("year") == self.user.current_year:
					info_current_subjects[subject] = info_subjects[subject]
				else:
					info_past_subjects[subject] = info_subjects[subject]
				
			self.user.raw_subject_info = {"current": info_current_subjects, "past": info_past_subjects }
			self.user.save()
		else:
			pass

	def __init__(self):
		self.isNewUser = self.isNewUser() #	Check if new user for loading or creating
		self.subjects_to_add = {"current": [], "past": []} 	#	Used to store partial information when adding subjects throughout adding process, see scheduling modules, dict of past and current

		self.user = User()
