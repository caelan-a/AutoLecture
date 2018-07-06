from PySide.QtCore import *
from PySide.QtGui import *

class FloatingDownArrow(QPushButton):

	def stopFloatAnimation(self):
		self.height_anim.stop()

	def startFloatAnimation(self, amplitude=10, duration=4000):
		self.animation_duration = duration
		self.animation_amplitude = amplitude

		self.start_pos = self.geometry()
		self.end_pos = QRect(self.start_pos.x(), self.start_pos.y()+self.animation_amplitude, self.start_pos.width(), self.start_pos.height())
		
		self.height_anim.setLoopCount(-1)
		self.height_anim.setDuration(duration/2)

		#	Animation down from initial
		self.height_anim.setStartValue(self.start_pos)
		self.height_anim.setKeyValueAt(0.5, self.end_pos)
		self.height_anim.setEndValue(self.start_pos)
		self.height_anim.start()

	def __init__(self, parent, object_name, arrow_icon, width=50, height=50):
		QPushButton.__init__(self)

		self.setIcon(arrow_icon)
		self.setObjectName(object_name)
		self.setIconSize(QSize(width,height))

		self.height_anim = QPropertyAnimation(self, "geometry")
		self.height_anim.setEasingCurve(QEasingCurve.InOutCirc)

		# self.timer = QTimer(self)
		# self.timer.setInterval(self.animation_duration)
		# self.connect(self.timer, SIGNAL("timeout()"), self.floatAnimation)
		# self.timer.start()