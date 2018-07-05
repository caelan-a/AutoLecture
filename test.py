import sys, os
import datetime
import back.settings as settings
import back.LmsNavigator as LmsNavigator
import back.UniversityTools as UniversityTools
from back.app import AutoLectureApp

os.path.join(os.path.dirname(__file__))

autolecture_app = AutoLectureApp()
# autolecture_app.loadUser()

user = autolecture_app.user

autolecture_app.user.setUniversity("University of Melbourne")
autolecture_app.user.setLoginInfo("caelana", "cael1998")
autolecture_app.startBrowser()
LmsNavigator.goToLms(autolecture_app.user.username,autolecture_app.user.password)
# autolecture_app.user.subject_info = LmsNavigator.getLmsSubjectInfo()
subject_info = LmsNavigator.getLmsSubjectInfo()
autolecture_app.user.subject_info = subject_info
# autolecture_app.user.save()

subject_info = user.subject_info

def containsPreviousSubjects(current_year, current_sem, subject_info):
	for subject in subject_info:
		if subject_info[subject].get("semester") != current_sem or subject_info[subject].get("year") != current_year:
			return True
	return False
	

print("{} \n\t{}\n\tSemester {}\n".format(user.username, user.current_year, user.current_term))
for subject in user.subject_info:
	print("{} \n\t {} \n\t Semester {} \n\t  ".format(user.subject_info[subject]["title"],user.subject_info[subject]["year"], user.subject_info[subject]["semester"]))

print("Does contain in previous subjects: {}".format(containsPreviousSubjects(2018, 2, user.subject_info)))

# autolecture_app.closeBrowser()