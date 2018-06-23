from PySide.QtCore import *
from PySide.QtGui import *

class Assets():
	def loadAssets(self):
		self.pixmap_tick_green = QPixmap("resources/icons/icon_tick_green.png")
		self.pixmap_tick_white = QPixmap("resources/icons/icon_tick_white.png")
		self.pixmap_tick_grey = QPixmap("resources/icons/icon_tick_grey (1).png")

		self.icon_tick_green = QIcon(self.pixmap_tick_green)
		self.icon_tick_white = QIcon(self.pixmap_tick_white)
		self.icon_tick_grey = QIcon(self.pixmap_tick_grey)

	def __init__(self):
		self.loadAssets()