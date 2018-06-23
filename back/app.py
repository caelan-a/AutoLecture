import User
import settings
import LinkUtil
from LectureHandler import LectureHandler, Lecture, Week
import LmsNavigator
import download
import os.path

USER_SAVE_PATH = "save\\user.pkl"

os.path.join(os.path.dirname(__file__))

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

	def startBrowser(self):
		settings.startBrowser()

	def closeBrowser(self):
		settings.closeBrowser()

	def __init__(self):
		self.isNewUser = self.isNewUser() #	Check if new user for loading or creating
		self.user = User()

		#settings.startBrowser()
		#LmsNavigator.login(settings.userData.user, settings.userData.password)
		#self.cal = settings.userData.subjects[2].lectureCalender
		#self.cal.setDateLastDownloaded("September 22")
		#cal.updateLectureList()
		#self.lectures_to_dl = cal.getUndownloadedScheduledLectures()
		#self.lectures_to_dl = [l for l in lectures_to_dl if l not in lectures_to_dl[1:4]]
		#self.download.downloadLectures(cal, lectures_to_dl)
		#settings.closeBrowser()

		#settings.userData.updateLectureCalenders()
		#settings.userData.downloadNewLectures()
