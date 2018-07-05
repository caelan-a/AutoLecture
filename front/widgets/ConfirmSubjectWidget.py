from PySide.QtCore import *
from PySide.QtGui import *

from stylesheets.StyleSheets import setStyleSheet

BIG_TILE_SIZE = [280,200]
SMALL_TILE_SIZE = [250,150]

TILE_NON_GLOW_COLOUR = QColor(0,0,0,100)
TILE_GLOW_COLOUR = QColor(47, 149, 153,250)
NON_GLOW_STRENGTH = 3
GLOW_STRENGTH = 15

TILE_ICON_PADDING_FACTOR = 3


class ConfirmSubjectWidget(QWidget):
	def resizeEvent(self, event):
		# Resize icon if subject tiles change size
		self.button_confirm.setIconSize(QSize(self.button_confirm.parent().size().width()/TILE_ICON_PADDING_FACTOR, self.button_confirm.parent().size().height()/TILE_ICON_PADDING_FACTOR));

	def setShadow(self, shadow, x_off, y_off, strength):
		shadow.setBlurRadius(strength)
		shadow.setOffset(x_off,y_off)

	@Slot()
	def toggleSelected(self):
		if self.confirm_bool == True:
			self.shadow.setColor(TILE_NON_GLOW_COLOUR)
			self.shadow_anim.setStartValue(GLOW_STRENGTH)
			self.shadow_anim.setEndValue(NON_GLOW_STRENGTH)
			self.shadow_anim.start()
			self.confirm_bool = False
		else:
			#	Colour gives glow
			self.shadow.setColor(TILE_GLOW_COLOUR)
			self.shadow_anim.setStartValue(NON_GLOW_STRENGTH)
			self.shadow_anim.setEndValue(GLOW_STRENGTH)
			self.shadow_anim.start()
			self.confirm_bool = True

	def __init__(self, title, semester, year, subject_icon, size):
		QWidget.__init__(self)
		self.confirm_bool = False

		# Size policy

		self.layout = QVBoxLayout()

		self.frame = QPushButton()
		self.frame.setObjectName("subjectFrame")
		
		self.policy = QSizePolicy.Maximum
		self.setSizePolicy(self.policy,self.policy)

		self.main_layout = QVBoxLayout(self)

		setStyleSheet(self, "subject_tile")

		self.setStyleSheet(self.styleSheet)

		self.title = QLabel(title, self)
		self.semester = QLabel("Semester " + semester, self)
		self.year = QLabel(year, self)
		self.year.setObjectName("year")

		if size == "big":
			self.frame.setMinimumSize(BIG_TILE_SIZE[0], BIG_TILE_SIZE[1])
			self.title.setObjectName("title_big")
			self.semester.setObjectName("subtext_big")
			self.year.setObjectName("subtext_big")
		else:
			self.frame.setMinimumSize(SMALL_TILE_SIZE[0], SMALL_TILE_SIZE[1])
			self.title.setObjectName("title_small")
			self.semester.setObjectName("subtext_small")
			self.year.setObjectName("subtext_small")

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
		self.button_confirm.clicked.connect(self.toggleSelected)

		self.frame.clicked.connect(self.toggleSelected)
		self.layout.addWidget(self.button_confirm, 0, Qt.AlignCenter)
		self.layout.addWidget(self.title, 0, Qt.AlignCenter)
		self.layout.addStretch()
		self.layout.addWidget(self.semester, 0, Qt.AlignCenter)
		self.layout.addWidget(self.year, 0, Qt.AlignCenter)
		self.frame.setLayout(self.layout)

		self.main_layout.addWidget(self.frame)
