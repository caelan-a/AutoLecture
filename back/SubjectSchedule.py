from operator import itemgetter

def getScheduleFromRawLectures(title, code, raw_lecture_list):
	schedule = SubjectSchedule()
	schedule.title = title
	schedule.code = code

	#	list of dictionaries where each dictionary has a date as a key and list of times as value
	unique_sessions = {}
	for raw_lecture in raw_lecture_list:
		date = raw_lecture["date"]
		time = raw_lecture["time"]
		day_of_week = date.strftime("%A")

		#	If weekday hasn't been added, add new dictionary for weekday and add its accompanying time
		if day_of_week not in unique_sessions.keys():
			unique_sessions[day_of_week] = [time]
		#	If date has been added, check if time has been added to date dictionary, if not add
		elif time not in unique_sessions[day_of_week]:
			unique_sessions[day_of_week].append(time)

	#	Add session instances of type lecture for each unique session time and return a Schedule object of those
	
	session_instances = {"Lecture": []}
	for session in unique_sessions:
		for time in unique_sessions[session]:
			session_instance = {}
			session_instance["number"] = 0 #	To allow use of addSessions as it needs a ["number"] entry for sorting
			session_instance["type"] = "Lecture"
			session_instance["day"] = session
			session_instance["start_time"] = time
			session_instances["Lecture"].append(session_instance)
			print("Day: {}, Time: {}".format(session, time))

	schedule.addSessions(session_instances)
	return schedule

class SubjectSchedule(object):
	def __init__(self):
		self.title = []
		self.code = []
		self.sessions = {}
		self.chosen_lecture_sessions = []
		self.lecture_start_time_offset = 5 #	Time in mins from when lecture start

	def getTitle(self):
		return self.title

	def getCode(self):
		return self.code

	def sortSessionList(self, session_instances):	# Sessions instance refers to single list element of a given type such as Lectures, Worshops. Eg. [1, ['4:20 pm'], ['5:20 pm'], 'Location: This']
		return sorted(session_instances, key = itemgetter("number"))
		
	def addSessions(self, sessions): # input is dictionary of lists 
		self.sessions = sessions #	Session is dictionary entry of list of session instances for given type
		for session_type in self.sessions:
			self.sessions[session_type] = self.sortSessionList(self.sessions[session_type])

	def getSessionTypes(self):
		return list(self.sessions.keys())

	def getSessionInstances(self, session_type):
		return self.sessions[session_type]

