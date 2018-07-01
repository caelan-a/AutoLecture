from PySide.QtCore import *
from PySide.QtGui import *

class Widget(QWidget):
	def float():
		

	def __init__(self):
		QWidget.__init__(self)
		timer = QTimer()
		timer.timeout.connect(tick)
		timer.start(1000)
widget = Widget()