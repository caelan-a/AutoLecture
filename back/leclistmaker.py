import pickle
import datetime
import os.path

import LmsNavigator
from LectureCalender import LectureCalender, Lecture

lecs = pickle.load(open("eng_lec_original.pkl", "rb"))
lecs = [lecs[i] for i in range(0,52) if i not in range(10,14)]
for i in range(0,len(lecs)):
	print("{} [{}]".format(lecs[i].date, i))
pickle.dump(lecs,open("eng_lec.pkl","wb"))