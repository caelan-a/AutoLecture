import itertools
import shutil
import datetime
import copy
import download

import LmsNavigator

DAYS_IN_WEEK = 7

class Schedule():
	def __init__(self):
		self.weeks_in_term = 0
		self.term_start_date = datetime.datetime(0,0,0)
		self.term_end_date = datetime.datetime(0,0,0)
		self.days_per_week = 0
		self.lecs_per_day = 0
		self.lecs_per_week = 0
		self.scheduled_days = [] #	Eg [1, 3, 5], where 1=mon, 3=tue, 5=fri
		self.scheduled_times = [] #	Eg [datetime.date('4:20pm', etc, etc], where each element is complement of scheduled_days

	def setTermInfo(self, weeks_in_term, term_start_date, term_end_date):
		self.weeks_in_term = weeks_in_term
		self.term_start_date = term_start_date
		self.term_end_date = term_end_date

	def setFreqInfo(self, days_per_week, lecs_per_day):
		self.days_per_week = days_per_week
		self.lecs_per_day = lecs_per_day
		self.lecs_per_week = self.days_per_week * self.lecs_per_day

	def setScheduledDays(self, scheduled_days):
		self.scheduled_days = scheduled_days

	def setScheduledTimes(self, scheduled_times):
		self.scheduled_times = scheduled_times

	def getScheduledDays(self):
		return scheduled_days

class Lecture():
	def __init__(self, date, start_time, duration, week_num, lecture_num_of_week, term_start_date):
		self.url = ""
		self.download_path = ""

		self.available = False
		self.downloaded = False
		self.fully_watched = False
		self.partially = False
		self.percentage_watched = 0
		
		self.date = date
		self.start_time = start_time
		self.duration = 0
		
		self.nameofday = self.date.strftime("%A")
		self.dayofweek = date.weekday()

		self.lecture_num_of_week = lecture_num_of_week
		self.week_num = week_num

	def setDuration(self, duration):
		self.duration = duration

	def setPartiallyWatched(self, percentage_watched):
		self.fully_watched = False
		self.partially_watched = True
		self.percentage_watched = percentage_watched

	def setWatched(self):
		self.fully_watched = True
		self.percentage_watched = 100
		self.partially_watched = False

	def isFullyWatched(self):
		return self.fully_watched

	def isPartiallyWatched(self):
		return self.partially_watched

	def getPercentageWatched(self):
		return self.percentage_watched

	def setAvailableInfo(self, url):
		self.available = True
		self.url = url

	def setDownloadedInfo(self, download_path):
		self.downloaded = True
		self.download_path = download_path

class LectureHandler():
	def __init__(self):	
		self.schedule = Schedule()
		# self.schedule.setTermInfo()
		# self.schedule.setFreqInfo()
		# self.schedule.setScheduledDays()
		# self.schedule.setScheduledTimes()

		self.lecture_streams = []

	def createLectureNewStream(self, term_start_date, weeks_in_term, scheduled_days, scheduled_times):
		lectures = []

		for week in range(1, weeks_in_term):
			week_start_date = term_start_date + datetime.timedelta(days=DAYS_IN_WEEK)
			
			for index, day in enumerate(scheduled_days):
				lecture_scheduled_date = week_start_date + datetime.timedelta(days=day-1)
				lecture_scheduled_time = scheduled_times[index]
				lecture_num_of_week = index+1
				lecture = Lecture(lecture_scheduled_date, lecture_scheduled_time, week, lecture_num_of_week, term_start_date)
				lectures.append(lecture)
		

