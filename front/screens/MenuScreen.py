from PySide.QtCore import *
from PySide.QtGui import *

from widgets.SubjectTile import SubjectTile
from widgets.SubjectTileSet import SubjectTileSet

class MenuScreen(QWidget):
	@Slot()
	def goToSettings(self):
		self.parent().switchScreen(self.parent().screen_settings)

	def __init__(self, assets):
		QWidget.__init__(self)

		self.layout = QVBoxLayout()

		# Current subjects
		self.current_subject_tiles = []
		self.current_subject_tiles.append(SubjectTile("Syntax", 2, 2018, assets.icon_subject_icon, "big"))
		self.current_subject_tiles.append(SubjectTile("Real Analysis", 2, 2018, assets.icon_subject_icon, "big"))
		self.current_subject_tiles.append(SubjectTile("Engineering Mechanics", 2, 2018, assets.icon_subject_icon, "big"))
		self.current_subject_tiles.append(SubjectTile("Electrical Networks", 2, 2018, assets.icon_subject_icon, "big"))

		self.current_set = SubjectTileSet(5,assets,"big")
		self.current_set.addSubjectTiles(self.current_subject_tiles)

		# Past subjects
		self.past_subject_tiles = []
		self.past_subject_tiles.append(SubjectTile("Phonetics", 1, 2017, assets.icon_subject_icon, "small"))
		self.past_subject_tiles.append(SubjectTile("Engineering Mathematics", 1, 2017, assets.icon_subject_icon, "small"))
		self.past_subject_tiles.append(SubjectTile("Quantum Physics", 2, 2017, assets.icon_subject_icon, "small"))
		self.past_subject_tiles.append(SubjectTile("Linguistics", 2, 2017, assets.icon_subject_icon, "small"))

		self.past_set = SubjectTileSet(5, assets, "small")
		self.past_set.addSubjectTiles(self.current_subject_tiles)
		
		self.label = QLabel("You have 0 lectures to watch")
		self.layout.addWidget(self.label)
		self.layout.addWidget(self.current_set)
		self.setLayout(self.layout)