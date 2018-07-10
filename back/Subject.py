import download
import pickle
import datetime
import os.path

import LmsNavigator
import settings
import LectureHandler
from SubjectSchedule import SubjectSchedule

class Subject(object):
	def __init__(self, title, semester, year, code, course_id):
		self.TITLE = title
		self.CODE = code
		self.semester = semester
		self.year = year
		self.course_id = course_id
		self.lectureHandler = []
		self.subject_schedule = []

		self.raw_lecture_list = []	#	raw lecture list from echo

	def createLectureCalender(self):
		self.lectureHandler = LectureHandler.LectureHandler(self)

	def setTimeTable(self, timetable):
		self.timetable = timetable

	def save(self):
		pickle.dump(self, open("save\\"+self.CODE+".pkl", "wb"))

	def setSubjectSchedule(self):
		pass

	def setRawLectureList(self, lecture_list):
		pass

	def getCourseID(self):
		return self.course_id