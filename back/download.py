import os
import sys
import urllib
import settings
import LectureHandler
import User

def downloadUrl(url, path): 
  	def dlProgress(count, blockSize, totalSize):
  		percent = int(count*blockSize*100/totalSize)
  		sys.stdout.write("\r" + "%d%%" % percent)
  		sys.stdout.flush()

  	urllib.request.urlretrieve(url, path, reporthook=dlProgress)

def downloadLectures(lectureCalender, lectures_to_dl):
	for lecture in lectures_to_dl:
		if lecture.date == lectureCalender.getWeek(lecture.week_num).start_date:
			print("\n\tWeek {}".format(lecture.week_num))
			print("_______________________________")
		print("Downloading Lecture #{}".format(lecture.day_num))

		full_path = settings.userData.folder_path+'\\'+lectureCalender.subject.TITLE+'\\'+'Week '+str(lecture.week_num) + ' ({})'.format(lectureCalender.getWeek(lecture.week_num).start_date)

		if not os.path.exists(full_path): 	#	Create Directory if necessary
			os.makedirs(full_path)

		path = os.path.join(full_path+'\\'+'Lecture '+str(lecture.day_num)+'.m4v')
		downloadUrl(lecture.url, path)

		print("\nLecture Downloaded\n")

		lectureCalender.date_last_watched = lecture.date
		print("Date last watched: {}".format(lectureCalender.date_last_watched))
		settings.user.save()

	print("Lectures up to date")