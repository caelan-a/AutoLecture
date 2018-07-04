from PySide.QtCore import *
from PySide.QtGui import *

DURATION = 500
START_VALUE = 0
END_VALUE = 1
EASING_CURVE = QEasingCurve.InQuart

class FadeWidget(QWidget):
	def showEvent(self, event):
		self.property_anim_fade_in.start(QPropertyAnimation.DeleteWhenStopped);

	def __init__(self):
			QWidget.__init__(self)
			self.setupFadeIn()

	def setupFadeIn(self):
		# Fade in
		self.effect_fade_in = QGraphicsOpacityEffect()
		self.setGraphicsEffect(self.effect_fade_in);
		self.property_anim_fade_in = QPropertyAnimation(self.effect_fade_in,"opacity");
		self.property_anim_fade_in.setDuration(DURATION);
		self.property_anim_fade_in.setStartValue(START_VALUE);
		self.property_anim_fade_in.setEndValue(END_VALUE);
		self.property_anim_fade_in.setEasingCurve(EASING_CURVE)
