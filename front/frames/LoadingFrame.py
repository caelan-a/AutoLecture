from PySide.QtCore import *
from PySide.QtGui import *

from workthreads.GetSubjectInfoThread import GetSubjectInfoThread

class LoadingFrame(QWidget):
	@Slot(str)
	def setLoadingText(self, info_text):
		self.label_loading_info.setText(info_text)

	def startGetSubjectInfoThread(self):
		if not self.get_subject_info_thread.isRunning():
			self.get_subject_info_thread.exiting=False
			self.get_subject_info_thread.start()

	def show(self):
		super().show()
		# Setup thread to get subject info
		self.get_subject_info_thread = GetSubjectInfoThread(self, self.setLoadingText)
		self.startGetSubjectInfoThread()
		self.label_loading_anim.movie().start()

	def __init__(self, loading_anim_movie):
		QWidget.__init__(self)

		# Setup thread to get subject info
		self.get_subject_info_thread = GetSubjectInfoThread(self, self.setLoadingText)

		self.layout = QVBoxLayout()
		self.layout.setAlignment(Qt.AlignHCenter)

		# Setup animation
		self.label_loading_anim = QLabel()
		self.label_loading_anim.setStyleSheet('background:transparent;')
		loading_anim_movie.setSpeed(400)
		self.label_loading_anim.setMovie(loading_anim_movie)

		self.effect = QGraphicsColorizeEffect(self)
		self.effect.setStrength(1)
		self.label_loading_anim.setGraphicsEffect(self.effect)
		self.effect.setColor(QColor('#2F9599'))

		# Info string about current action
		self.label_loading_info = QLabel("Loading info")
		self.label_loading_info.setAlignment(Qt.AlignCenter)

		self.layout.addWidget(self.label_loading_anim)
		self.layout.addStretch()
		self.layout.addWidget(self.label_loading_info)
		self.layout.addStretch()
		self.setLayout(self.layout)


