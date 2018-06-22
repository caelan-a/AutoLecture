import download
import pickle
import datetime
import os.path

import LmsNavigator
from Subject import Subject

class User(object):
	def __init__(self):
		self.username = ""
		self.password = ""
		self.university = ""
		self.uni_info = {}	#	Contains calender datesl
		self.folder_path = ""

		self.subjects = {}
		self.missing_subjects = {}

		self.timetable = []
		self.subject_info = [] #	Delete (only for testing)

	def getCurrentTerm(self):
		current_date = datetime.datetime.now().date()

		if current_date < self.uni_info.get("semester_1_start_date").date():
			return 0 #	0 = Summer
		elif  current_date < self.uni_info.get("semester_2_start_date").date():
			return 1	#	1 = Semester 1
		elif current_date < self.uni_info.get("semester_2_exam_end").date():
			return 2  # 2 = Semester 2
		#	Insert 4 = Winter =

	def getCurrentYear(self):
		return datetime.datetime.now().year

	def addMissingSubject(self, missing_subject_code, missing_subject_timetable):
		self.missing_subjects[missing_subject_code] = missing_subject_timetable

	def setLoginInfo(self, username, password):
		self.username = username
		self.password = password

	def setFolderPath(self, path):
		self.folder_path = path

	def setUniversity(self, university, uni_info):
		self.university = university
		self.uni_info = uni_info

	def getUniInfo(self):
		return self.uni_info

	def save(self):
		pickle.dump(self, open("save\\user.pkl", "wb"))

	def setTimeTable(self, timetable):
		self.timetable = timetable

	def createSubject(self, title, semester, year, code, course_id, timetable = []):
		new_subject = Subject(title, semester, year, code, course_id, time_table = timetable)
		self.subjects[code] = new_subject

	#	Batch methods
	def updateLectureCalenders(self):
		print("Finding new lectures for:\n")
		LmsNavigator.login(self.user, self.password)
		for s in settings.userData.subjects:
			print("{}\n".format(s.TITLE))
			cal = s.lectureHandler
			cal.updateLectureList()
		self.save()

	def downloadNewLectures(self):
		print("Downloading new lectures...\n")
		for s in settings.userData.subjects:
			cal = s.lectureHandler
			cal.downloadNewLectures()
		print("All lectures up to date\n") 


