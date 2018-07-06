Paths = {"subject_tile": "front/stylesheets/subject_tile.stylesheet",
		 "main": "front/stylesheets/button.stylesheet"}

def setStyleSheet(self, stylesheet_name):
	sshFile=Paths[stylesheet_name]
	with open(sshFile,"r") as fh:
		self.styleSheet = fh.read()
	self.setStyleSheet(self.styleSheet)