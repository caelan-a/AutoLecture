from PySide.QtCore import *
from PySide.QtGui import *

class Assets():
	def loadAssets(self):
		# Pixmaps
		self.pixmap_tick_green = QPixmap("resources/icons/icon_tick_green.png")
		self.pixmap_tick_white = QPixmap("resources/icons/icon_tick_white.png")
		self.pixmap_tick_grey = QPixmap("resources/icons/icon_tick_grey (1).png")
		self.pixmap_play_white = QPixmap("resources/icons/icon_lectures1")
		self.pixmap_settings_white = QPixmap("resources/icons/icon_settings")

		# Icons
		self.icon_tick_green = QIcon(self.pixmap_tick_green)
		self.icon_tick_white = QIcon(self.pixmap_tick_white)
		self.icon_tick_grey = QIcon(self.pixmap_tick_grey)
		self.icon_play_white = QIcon(self.pixmap_play_white)
		self.icon_settings_white = QIcon(self.pixmap_settings_white)

		# Movies
		self.movie_loading_anim = QMovie("resources/icons/loading1.gif")

	def __init__(self):
		self.loadAssets() 