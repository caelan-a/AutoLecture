from operator import itemgetter


class SubjectSchedule(object):

	def __init__(self):
		self.title = []
		self.code = []
		self.sessions = {}

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

