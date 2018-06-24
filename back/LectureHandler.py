import itertools
import shutil
import datetime
import copy
import download

import LmsNavigator


class Schedule():
	def __init__(self):
		self.times = []

	def setTermInfo(self, weeks_in_term, term_start_date, term_end_date):
		self.weeks_in_term = weeks_in_term
		self.term_start_date = term_start_date
		self.term_end_date = term_end_date

	def setFreqInfo(days_per_week, lecs_per_day):
		self.days_per_week = days_per_week
		self.lecs_per_day = lecs_per_day
		self.lecs_per_week = self.days_per_week * self.lecs_per_day

	def setScheduledTimes(self, mon_times, tue_times, wed_times, thur_times, fri_times):
		self.times = [mon_times, tue_times, wed_times, thur_times, fri_times]

	def getScheduledTime(self, lecture):
		return self.times[lecture.dayofweek]

	def getLectureNumberOfWeek(self, lecture): # Ex Return 2 for 2nd lecture of 3
		lec_count = -1
		for t in self.times[lecture.dayofweek:]:
			if t != 0:
				lec_count += 1
		return self.days_per_week - lec_count 

class Day():
	def __init__(self, day_num, week_num):
		self.lectures = [] # Holds lectures in a given day of lectures for the week
		self.day_number = day_num # Index (starting from 1) of lectures days for week
		self.week_number = week_num

	def getLectures(self):
		return self.lectures

	def getLecture(self, i_of_lecture):
		return self.lectures[i_of_lecture-1]

	def getDayNumber(self):
		return self.day_number

	def addLecture(self, lecture):
		self.lectures.append(lecture)
		self.date = lecture.date

class Week(): #	Holds each day of lectures for the subject 
	def __init__(self, wk_num, start_date):
		self.days = [] # Holds lectures in a given day of lectures for the week
		self.week_number = wk_num
		self.start_date = start_date

	def addDay(self, day):
		self.days.append(day)

	def getDay(self, n_day):
		return self.days[n_day-1]

	def getDays(self):
		return self.days

	def getWeekNumber(self):
		return self.week_number

	def numOfDays(self):
		return len(self.days)

	def getLectures(self):
		lecs = []
		for d in self.days:
			lecs.append(d.getLectures())
			return list(itertools.chain.from_iterable(lecs))

class LectureHandler():
	def getWeek(self, n_week):
		return self.weeks[n_week-1]

	def getWeeks(self):
		return self.weeks

	def getNumWeeks(self):
		return len(self.weeks)

	def getDayByDate(self, week_list, date):
		for w in week_list:
			for d in w.days:
				if d.date == date:
					return d
		else:
			print("No day matches date requested..")

	def getWeeksScheduled(self):
		times = self.times

		weeks_scheduled = copy.deepcopy(self.getWeeks())

		for w in weeks_scheduled:
			days = w.days

			for i in range(0,len(days)):
				lecs_sched = []
				for l in days[i].lectures:
					if l.time == times[i]:
						lecs_sched.append(l)

				days[i].lectures = lecs_sched

		
		"""
		print("Scheduled Lectures")
		for w in weeks_scheduled:
			print("Week {}".format(w.week_number))
			for d in w.days:
				print("Day {}".format(d.day_number))
				for l in d.lectures:
					print(l.time)
		"""
		
		weeks_scheduled = self.fillMissingLectures(self.getWeeks(), weeks_scheduled)
		return weeks_scheduled
		"""
		print("Missing lectures filled Scheduled Week")
		for w in weeks_scheduled:
			print("Week {}".format(w.getWeekNumber()))
			for d in w.getDays():
				print("Day {} ({})".format(d.day_number,d.date))
				for l in d.lectures:
					print(l.time)
					"""

	def getDaysDifference(self,date1, date2):
		if date1 == date2:
			return 0

		dif_str = date2-date1
		dif_str_splt = str(dif_str).split(' ')
		return abs(int(dif_str_splt[0]))

	def parseLectureList(self, lecture_list):
		for l in lecture_list: 
			calender_week = l.isocalendar()[1]
			week_i = calender_week - self.initial_week

			self.weeks[week_i].append(l)


		"""
		print("All lectures: ")
		for w in week_list:
			print("Week {}".format(w.week_number))
			for d in w.days:
				print("Day {}".format(d.day_number))
				for l in d.lectures:
					print("Date: {}, Time: {}".format(l.date, l.time))
		print("\n\n")
		"""
		return week_list

	def getUndownloadedScheduledLectures(self):
		days = self.getDays(self.weeks_scheduled)

		if self.date_last_downloaded != 0:
			last_day_watched = self.getDayByDate(self.weeks_scheduled, self.date_last_watched)

			index_last_day_watched = 0
			for i in range(0, len(days)):
				if days[i] == last_day_watched:
					index_last_day_watched = i
					break
			else:
				print("No date matched last date watched")

			days_to_download = days[i+1:]
		else:
			days_to_download = days

		lectures = []
		for d in days_to_download:
			for l in d.lectures:
				lectures.append(l)

		return lectures

	def getLecturesFromWeeks(self, week_list):
		lectures = []
		for w in week_list:
			for d in w.days:
				for l in d.lectures:
					lectures.append(l)
		return lectures

	def getDays(self, week_list): # Returns list of all lectures in a list of Weeks
		days = []
		for w in week_list:
			for d in w.days:
				days.append(d)

		return days

	def updateLectureList(self):
		print("Updating lecture list for {}\n".format(self.subject.TITLE))
		new_lectures = LmsNavigator.getOnlineLectures(self.subject, self.date_last_indexed)

	#	Requires updateLectureList() to be called first to fill list with new lectures
	def downloadNewLectures(self):
		lectures_to_dl = self.getUndownloadedScheduledLectures()
		print("Downloading {} lecture(s)".format(len(lectures_to_dl)))
		download.downloadLectures(self, lectures_to_dl)

	def getAvailableSessions(self):
		#	Loop until day_index resets to weeks first lecture to fill entire week
		week_of_lectures = [] 
		current_day_index = 0
		for l in self.lecture_list:
			if l.dayofweek >= current_day_index:
				current_day_index = l.dayofweek
				week_of_lectures.append(l)
			else:
				break

		#	Sort into elements of ex. [Monday, 0, 4:20pm, 6:00pm]	
		available_sessions = []
		current_day_index = -1

		for l in week_of_lectures:
			if l.dayofweek == current_day_index:
				available_sessions[-1] = [available_sessions[-1], l.time]
			else:
				current_day_index = l.dayofweek 
				available_sessions.append([l.nameofday, current_day_index, l.time])

		return available_sessions


	def __init__(self, subject):	
		self.subject = subject
		self.date_last_downloaded = 0
		self.date_last_indexed = 0 # Last lecture to have been retrieved using LmsNavigator.getOnlineLectures
		self.schedule = Schedule()
		self.lecture_list = LmsNavigator.getOnlineLectures(self.subject, self.date_last_indexed)
		self.initial_week = self.lecture_list[0].date.isocalendar()[1]


class Lecture():
	def __init__(self, date, time):
		self.url = ""
		self.download_path = ""

		self.available = False
		self.downloaded = False
		
		self.date = date
		self.time = time
		
		self.nameofday = self.date.strftime("%A")
		self.dayofweek = date.weekday()

		self.week_num = 0
		self.day_num = 0 # Lecture number of week
		self.setChronology(date)

	def setAvailableInfo(self, url):
		self.available = True
		self.url = url

	def setDownloadedInfo(self, download_path):
		self.downloaded = True
		self.download_path = download_path

	# def setChronology(self, term_start_date, term_end_date, date):
		

