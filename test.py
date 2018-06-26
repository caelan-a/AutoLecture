import sys, os
import datetime
import back.settings as settings
import back.LmsNavigator as LmsNavigator
import back.UniversityTools as UniversityTools
from back.app import AutoLectureApp

os.path.join(os.path.dirname(__file__))

autolecture_app = AutoLectureApp()
# autolecture_app.user.setUniversity("University of Melbourne", UniversityTools.universities.get("University of Melbourne"))
autolecture_app.user.setLoginInfo("caelana", "cael1998")
autolecture_app.startBrowser()
# LmsNavigator.goToTimeTable(autolecture_app.user.username,autolecture_app.user.password)
# autolecture_app.user.timetable = LmsNavigator.getOnlineTimeTable() 

LmsNavigator.goToLms(autolecture_app.user.username,autolecture_app.user.password)
autolecture_app.user.subject_info = LmsNavigator.getLmsSubjectInfo()
subject_info = LmsNavigator.getLmsSubjectInfo()

def containsPreviousSubjects(current_year, current_sem, subject_info):
	for subject in subject_info:
		if subject_info[subject].get("semester") != current_sem or subject_info[subject].get("year") != current_year:
			return True
	return False
print(subject_info)
print()
print("Does contain previous subjects: {}".format(containsPreviousSubjects(2018, 2, subject_info)))

autolecture_app.closeBrowser()