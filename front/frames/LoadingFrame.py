from PySide.QtCore import *
from PySide.QtGui import *

class LoadingFrame(QWidget):
	@Slot(str)
	def setLoadingText(self, info_text):
		self.label_loading_info.setText(info_text)

	def showEvent(self, event):
		self.label_loading_anim.movie().start()

	def hideEvent(self, event):
		self.label_loading_anim.movie().stop()

	def __init__(self, loading_anim_movie):
		QWidget.__init__(self)

		self.layout = QVBoxLayout()
		self.layout.setAlignment(Qt.AlignHCenter)

		# Setup animation 
		loading_anim_movie.setSpeed(400)

		self.label_loading_anim = QLabel()
		self.label_loading_anim.setStyleSheet('background:transparent;')
		self.label_loading_anim.setMovie(loading_anim_movie)

		# Set animation tint
		self.effect = QGraphicsColorizeEffect(self)
		self.effect.setStrength(1)
		self.effect.setColor(QColor('#2F9599'))
		self.label_loading_anim.setGraphicsEffect(self.effect)

		# Info string about current action
		self.label_loading_info = QLabel("Loading info")
		self.label_loading_info.setAlignment(Qt.AlignCenter)

		# Lay widgets out
		self.layout.addWidget(self.label_loading_anim)
		self.layout.addStretch()
		self.layout.addWidget(self.label_loading_info)
		self.layout.addStretch()

		# Set layout
		self.setLayout(self.layout)


