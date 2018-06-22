import sys
import datetime
sys.path.insert(0,'C:\\Users\\cande\\Google Drive\\Projects\\AutoLecture v1.31\\AutoLecture')
#sys.path.insert(0,'C:\\Users\\Caelan\\Google Drive\\Projects\\AutoLecture v1.31\\AutoLecture')
import AutoLecture.settings as settings
import AutoLecture.LmsNavigator as LmsNavigator
import AutoLecture.UniversityTools as UniversityTools
from AutoLecture.app import AutoLectureApp

autolecture_app = AutoLectureApp()
#autolecture_app.user.setUniversity("University of Melbourne", UniversityTools.universities.get("University of Melbourne"))
#autolecture_app.user.setLoginInfo("caelana", "cael1998")
#autolecture_app.startBrowser()
#LmsNavigator.goToTimeTable(autolecture_app.user.username,autolecture_app.user.password)
#autolecture_app.user.timetable = LmsNavigator.getOnlineTimeTable() 

#LmsNavigator.goToLms(autolecture_app.user.username,autolecture_app.user.password)
#autolecture_app.user.subject_info = LmsNavigator.getLmsSubjectInfo()

#autolecture_app.user.save()
autolecture_app.loadUser()


#for key in autolecture_app.user.subject_info:
	#print(autolecture_app.user.subject_info[key]["code"])

print((autolecture_app.user.subject_info))


#print(autolecture_app.user.subject_info[" The Secret Life of Language"]["code"])
"""
if autolecture_app.isNewUser:
	autolecture_app.user.setUniversity("University of Melbourne", UniversityTools.universities.get("University of Melbourne"))
	autolecture_app.user.setLoginInfo("caelana", "cael1998")

	autolecture_app.startBrowser()

	if not is_summer_term:
		LmsNavigator.goToTimeTable(autolecture_app.user.username,autolecture_app.user.password)
		timetable = LmsNavigator.getOnlineTimeTable()
	elif is_summer_term:
		print("Do stuff for summer term")
		#	Add in functionality

	LmsNavigator.goToLms(autolecture_app.user.username,autolecture_app.user.password)
	subjects_lms_info = LmsNavigator.getLmsSubjectInfo()  

	#	Create subjects
	autolecture_app.user.createSubjects(subjects_info)

	#	Create for individual subject
	autolecture_app.user.subjects[0].createLectureCalender()
	#available_sessions = autolecture_app.user.subjects[0].lectureHandler.getAvailableSessions()
	#timetable = LmsNavigator.getOnlineTimeTable()

	autolecture_app.user.subjects[0].lectureHandler.timetable.setFreqInfo(available_sessions)
	autolecture_app.user.subjects[0].lectureHandler.timetable.setTimes(datetime.datetime.strptime('4:20PM', '%I:%M%p').time(),0,datetime.datetime.strptime('4:20PM', '%I:%M%p').time(),0,datetime.datetime.strptime('4:20PM', '%I:%M%p').time())

	autolecture_app.user.save()

	available_sessions = autolecture_app.user.subjects[0].lectureHandler.getAvailableSessions()
	print(available_sessions)


	autolecture_app.closeBrowser()
	#autolecture_app.user.setFolderPath("C:\\Users\\cande\\Videos")
	
else:
	autolecture_app.loadUser()
	autolecture_app.user.subjects[0].lectureHandler.timetable.setTimes(datetime.datetime.strptime('4:20PM', '%I:%M%p').time(),0,datetime.datetime.strptime('4:20PM', '%I:%M%p').time(),0,datetime.datetime.strptime('4:20PM', '%I:%M%p').time())
	print(autolecture_app.user.subjects[0].lectureHandler.timetable.getTime())
"""