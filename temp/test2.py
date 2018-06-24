import sys
import datetime
sys.path.insert(0,'C:\\Users\\cande\\Google Drive\\Projects\\AutoLecture v1.31\\AutoLecture')
#sys.path.insert(0,'C:\\Users\\Caelan\\Google Drive\\Projects\\AutoLecture v1.31\\AutoLecture')
import AutoLecture.settings as settings
import AutoLecture.LmsNavigator as LmsNavigator
import AutoLecture.UniversityTools as UniversityTools
from AutoLecture.app import AutoLectureApp

autolecture_app = AutoLectureApp()

autolecture_app.loadUser()

current_term = autolecture_app.user.getCurrentTerm()
current_year = autolecture_app.user.getCurrentYear() 

if current_term == 0: # If in summer term
	if LmsNavigator.isSummerTimeTable():
		print("check subjects")
	else:
		print("No summer timetable exists. Wait until next semester")
		#	Check last terms subjects
elif current_term == 1 or current_term == 2:
	autolecture_app.startBrowser()
	#	Get subject timetable information
	# LmsNavigator.goToTimeTable(autolecture_app.user.username, autolecture_app.user.password)
	# autolecture_app.user.timetable = LmsNavigator.getOnlineTimeTable()

	print(autolecture_app.user.timetable)

	if autolecture_app.user.timetable["info"]["year"] == current_year and autolecture_app.user.timetable["info"]["semester"] == current_term: # If timetable matches current semester/term
		#	Get LMS listed subjects
		LmsNavigator.goToLms(autolecture_app.user.username,autolecture_app.user.password)
		autolecture_app.user.subject_info = LmsNavigator.getLmsSubjectInfo()

		#	Match Unimelb timetabled subjects with LMS subjects, if match, add, if no match, add to missing subjects in user
		for key in autolecture_app.user.timetable:
			if key in autolecture_app.user.subject_info:
				subj_info = autolecture_app.user.subject_info[key]
				autolecture_app.user.createSubject(subj_info["title"], subj_info["semester"], subj_info["year"], subj_info["code"], subj_info["course_id"], autolecture_app.user.timetable[key])
			else:
				autolecture_app.user.addMissingSubject(key, autolecture_app.user.timetable[key])
	elif autolecture_app.user.timetable["info"]["year"] == current_year and autolecture_app.user.timetable["info"]["semester"] != 1 :
		print("Semester *insert semester* subjects are yet to be released, we will get them ready when they're released on the *insert date* or *winter/summer* subjects if you do any")
	elif current_term == 4:
		print("Check winter term")

#	Ask user if they would like to store subjects from past semester

#print(autolecture_app.user.timetable["COMP20005"])
print(autolecture_app.user.subject_info)

