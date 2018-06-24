from PySide.QtCore import *
from PySide.QtGui import *

class LoadingFrame(QWidget):
	def __init__(self, loading_anim_movie):
		QWidget.__init__(self)

		self.layout = QVBoxLayout()

		self.layout.setAlignment(Qt.AlignHCenter)

		self.label_loading_anim = QLabel()
		self.label_loading_anim.setStyleSheet('background:transparent;')
		loading_anim_movie.setSpeed(400)
		self.label_loading_anim.setMovie(loading_anim_movie)

		self.effect = QGraphicsColorizeEffect(self)
		self.effect.setStrength(1)
		self.label_loading_anim.setGraphicsEffect(self.effect)
		self.effect.setColor(QColor('#2F9599'))

		loading_anim_movie.start()

		self.layout.addWidget(self.label_loading_anim)
		self.layout.addStretch()
		self.setLayout(self.layout)
