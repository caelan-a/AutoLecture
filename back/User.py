import download
import pickle
import datetime
import os.path
import UniversityTools

import LmsNavigator
from Subject import Subject

class User(object):
	def __init__(self):
		self.username = ""
		self.password = ""
		self.university = ""
		self.uni_info = UniversityTools.uni_info	#	Contains calender dates
		self.folder_path = ""

		self.subjects = {}
		self.missing_subjects = {}

		self.current_year = datetime.datetime.now().date().year
		self.current_term = self.getCurrentTerm()

		self.subject_info = [] # delete, only for testing

		self.timetable = []

	def getCurrentTerm(self):
		current_date = datetime.datetime.now().date()

		if current_date < self.uni_info.get("semester_1_start_date").date():
			return 0 #	0 = Summer
		elif  current_date < self.uni_info.get("semester_1_end_date").date():
			return 1	#	1 = Semester 1
		elif current_date < self.uni_info.get("semester_2_end_date").date():
			return 2  # 2 = Semester 2
		elif current_date > self.uni_info.get("semester_2_end_date").date():
			return 3

	def getCurrentYear(self):
		return datetime.datetime.now().year

	def addMissingSubject(self, missing_subject_code, missing_subject_timetable):
		self.missing_subjects[missing_subject_code] = missing_subject_timetable

	def setLoginInfo(self, username, password):
		self.username = username
		self.password = password

	def setFolderPath(self, path):
		self.folder_path = path

	def setUniversity(self, university):
		self.university = university
		self.uni_info = UniversityTools.universities[university]

	def getUniInfo(self):
		return self.uni_info

	def save(self):
		pickle.dump(self, open("save\\user.pkl", "wb"))

	def setTimeTable(self, timetable):
		self.timetable = timetable

	def createSubject(self, title, semester, year, code, course_id, timetable = []):
		new_subject = Subject(title, semester, year, code, course_id, time_table = timetable)
		self.subjects[code] = new_subject


