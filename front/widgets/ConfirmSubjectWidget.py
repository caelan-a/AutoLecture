from PySide.QtCore import *
from PySide.QtGui import *

BUTTON_STYLE_SHEET_PATH = "front/stylesheets/subject_tile.stylesheet"

class confirmSubjectWidget(QWidget):
	def setShadow(self, shadow, x_off, y_off, strength):
		shadow.setBlurRadius(strength)
		shadow.setOffset(x_off,y_off)

	@Slot()
	def toggleSelected(self):
		if self.confirm_bool == True:
			#self.setShadow(self.shadow, 0, 1, 3)
			self.shadow.setColor(QColor(0,0,0,100))
			self.shadow_anim.setStartValue(15)
			self.shadow_anim.setEndValue(3)
			self.shadow_anim.start()
			print("unselected")
			self.confirm_bool = False
		else:
			#self.setShadow(self.shadow, 2, 4, 5)
			self.shadow.setColor(QColor(47, 149, 153,250))
			self.shadow_anim.setStartValue(3)
			self.shadow_anim.setEndValue(15)
			self.shadow_anim.start()
			print("selected")
			self.confirm_bool = True

	def __init__(self, title, semester, year, code, subject_icon):
		QWidget.__init__(self)
		self.confirm_bool = False

		self.main_layout = QVBoxLayout(self)
		self.layout = QVBoxLayout()

		self.frame = QPushButton()
		self.frame.setFixedSize(100,250)
		self.frame.setObjectName("subjectFrame")

		sshFile=BUTTON_STYLE_SHEET_PATH
		with open(sshFile,"r") as fh: 
			self.styleSheet = fh.read()

		self.setStyleSheet(self.styleSheet)

		self.title = QLabel(title)
		self.title.setObjectName("title")
		self.semester = QLabel("Semester " + semester)
		self.semester.setObjectName("semester")
		self.year = QLabel(year)
		self.year.setObjectName("year")

		self.shadow = QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(3)
		self.shadow.setOffset(1,5)
		self.shadow.setColor(QColor(0,0,0,100))

		self.frame.setGraphicsEffect(self.shadow)

		self.shadow_anim = QPropertyAnimation(self.shadow, "blurRadius")
		self.shadow_anim.setDuration(200)
		self.shadow_anim.setEasingCurve(QEasingCurve.OutQuad)

		self.button_confirm = QPushButton()
		self.button_confirm.setIcon(subject_icon)
		self.button_confirm.setObjectName("tickButton")
		self.button_confirm.setIconSize(QSize(100,100));
		self.button_confirm.clicked.connect(self.toggleSelected)

		self.frame.clicked.connect(self.toggleSelected)
		self.layout.addWidget(self.button_confirm, 0, Qt.AlignCenter)
		self.layout.addWidget(self.title, 0, Qt.AlignCenter)
		self.layout.addStretch()
		self.layout.addWidget(self.semester, 0, Qt.AlignCenter)
		self.layout.addWidget(self.year, 0, Qt.AlignCenter)
		self.frame.setLayout(self.layout)

		self.main_layout.addWidget(self.frame)
