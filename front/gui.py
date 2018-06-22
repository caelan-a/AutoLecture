import sys
sys.path.insert(0,'C:\\Users\\cande\\Google Drive\\Projects\\AutoLecture v1.31\\GUI')
from PySide.QtCore import *
from PySide.QtGui import *

from GUI.Assets import Assets

class Window(QWidget):
	def switchScreen(self, next):
		self.active_screen.hide()
		next.show()
		self.active_screen = next
	def setInitialScreen(self,screen):
		self.active_screen = screen
		self.switchScreen(screen)

	def __init__(self):
		QWidget.__init__(self)

		global assets
		assets = Assets()
		
		sshFile="GUI/button.stylesheet"
		with open(sshFile,"r") as fh: 
			self.styleSheet = fh.read()

		self.setStyleSheet(self.styleSheet)


		QApplication.setStyle(QStyleFactory.create('Cleanlooks'))
        
		self.setMinimumSize(QSize(1600,1000))
		self.setWindowIcon(QIcon('GUI/images/logo_taskbar.png'))  
		self.setWindowTitle(' ')

		self.layout = QVBoxLayout()
		self.layout.setContentsMargins(0,0,0,0)
		#	Screens 
		self.screen_setup = SetupScreen()
		self.screen_settings = SettingsScreen()
		self.screen_menu = MenuScreen()
		self.layout.addWidget(self.screen_setup)
		self.layout.addWidget(self.screen_settings)
		self.layout.addWidget(self.screen_menu)
		self.screen_setup.hide()
		self.screen_settings.hide()
		self.screen_menu.hide()

		self.setLayout(self.layout)

	def run(self, qt_app):
        # Show the form
		self.show()
		# Run the qt application
		qt_app.exec_()

class InputField(QWidget):
	def __init__(self, title, value):
		QWidget.__init__(self)
		self.layout = QVBoxLayout()
		self.layout.setContentsMargins(0,0,0,0)
		self.heading = QLabel(title)
		self.input = QLineEdit(self)
		self.input.setText(value)
		self.layout.addWidget(self.heading)
		self.layout.addWidget(self.input)
		self.setLayout(self.layout)

class UserFrame(QWidget):
	def __init__(self, parent):
		super(UserFrame,self).__init__(parent)

		#	Confirmation box for reset
		self.buttonBox = QMessageBox()
		self.buttonBox.addButton(QPushButton("Yes",self),QMessageBox.AcceptRole)
		self.buttonBox.setText("	Are you sure?")
		self.buttonBox.setWindowTitle(' ')
		self.buttonBox.setWindowIcon(QIcon('GUI/images/logo_taskbar.png'))  
		self.buttonBox.setIcon(QMessageBox.NoIcon)
		sshFile="GUI/button.stylesheet"
		with open(sshFile,"r") as fh:
			self.styleSheet = fh.read()
		self.buttonBox.setStyleSheet(self.styleSheet)
		
		self.layout = QVBoxLayout()
		self.input_username = InputField("Username", "caelana")
		self.input_password = InputField("Password", "cael1998")
		self.input_downloadpath = InputField("Download Path", "C:/Users/caelan/Videos")
		self.button_reset = QPushButton("Reset Account")
		self.button_reset.setObjectName("criticalButton")
		self.button_reset.clicked.connect(self.buttonBox.exec_)


		#self.buttonBox.accepted.connect(self.accept)
		#self.buttonBox.rejected.connect(self.reject)

		self.button_save = QPushButton("Save")


		self.layout.addStretch()
		self.layout.addWidget(self.input_username)
		self.layout.addWidget(self.input_password)
		self.layout.addStretch()
		self.layout.addWidget(self.input_downloadpath)
		self.layout.addStretch()
		self.layout.addWidget(self.button_reset,0,Qt.AlignCenter)
		self.layout.addStretch()
		self.layout.addWidget(self.button_save)

		self.setLayout(self.layout)
		
class LectureTimesWidget(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.vbox_day = QVBoxLayout()
		self.label_title_day = QLabel("Monday")
		self.list_time = QComboBox(self)
		self.list_time.addItems(self.lecture_dates)
		self.vbox_day.addWidget(self.label_title_day)
		self.vbox_day.addWidget(self.list_time)
		self.hbox_times.addLayout(self.vbox_day)

class SubjectFrame(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.layout = QVBoxLayout()

		self.input_title = InputField("Subject Title", "Engineering")

		self.lecture_dates = ["September 4", "September 6", "September 8"]
		self.label_title_lastwatched = QLabel("Last Lecture Watched")
		self.list_lastwatched = QComboBox(self)
		self.list_lastwatched.addItems(self.lecture_dates)

		self.label_title_lastdownloaded =  QLabel("Last Lecture Downloaded")
		self.list_lastdownloaded = QComboBox(self)
		self.list_lastdownloaded.addItems(self.lecture_dates)

		self.label_title_lecturetimes = QLabel("Lecture Times for the Week")
		self.hbox_times = QHBoxLayout()

		self.vbox_day = QVBoxLayout()
		self.label_title_day = QLabel("Monday")
		self.list_time = QComboBox(self)
		self.list_time.addItems(self.lecture_dates)
		self.vbox_day.addWidget(self.label_title_day)
		self.vbox_day.addWidget(self.list_time)
		self.hbox_times.addLayout(self.vbox_day)


		self.button_save = QPushButton("Save")


		self.layout.addStretch()
		self.layout.addWidget(self.input_title)
		self.layout.addStretch()
		self.layout.addWidget(self.label_title_lastwatched)
		self.layout.addWidget(self.list_lastwatched)
		self.layout.addWidget(self.label_title_lastdownloaded)
		self.layout.addWidget(self.list_lastdownloaded)
		self.layout.addStretch()
		self.layout.addWidget(self.label_title_lecturetimes)
		self.layout.addLayout(self.hbox_times)
		self.layout.addStretch()
		self.layout.addWidget(self.button_save)
		self.setLayout(self.layout)

class MenuScreen(QWidget):
	@Slot()
	def goToSettings(self):
		self.parent().switchScreen(self.parent().screen_settings)

	def __init__(self):
		QWidget.__init__(self)

		self.layout = QVBoxLayout()
		self.hbox = QHBoxLayout()

		self.layout.addStretch()
		self.label_title = QLabel("AutoLecture")
		self.label_title.setObjectName("setupScreenTitle")
		self.label_title.setAlignment(Qt.AlignCenter)
		self.layout.addWidget(self.label_title)

		pixmap = QPixmap("GUI/images/icon_lectures1")
		icon = QIcon(pixmap)
		self.button_lectures = QPushButton("")
		self.button_lectures.setObjectName('menuIcon')
		self.button_lectures.setIcon(icon)
		self.button_lectures.setIconSize(QSize(150,150));
		self.hbox.addWidget(self.button_lectures)

		pixmap = QPixmap("GUI/images/icon_settings")
		icon = QIcon(pixmap)
		self.button_settings = QPushButton("")
		self.button_settings.setObjectName('menuIcon')
		self.button_settings.setIcon(icon)
		self.button_settings.setIconSize(QSize(150,150));
		self.button_settings.clicked.connect(self.goToSettings)
		self.hbox.addWidget(self.button_settings)


		self.layout.addStretch()
		self.layout.addLayout(self.hbox)
		self.layout.addStretch()
		self.setLayout(self.layout)

class SettingsScreen(QWidget):
	def switchSubFrame(self, next):
		self.active_subframe.hide()
		next.show()
		self.active_subframe = next

	def setInitialSubFrame(self, initial):
		self.active_subframe = initial
		initial.show()

	def __init__(self):
		QWidget.__init__(self)
		self.frame_user = UserFrame(self)
		self.frame_user.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
		self.frame_user.hide()

		self.frame_subject = SubjectFrame()
		self.frame_subject.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
		self.frame_subject.hide()


		self.layout = QHBoxLayout()
		self.layout.setContentsMargins(0,0,0,0)

		self.nav_bar = NavigationBar()
		self.nav_bar.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Preferred)
		self.nav_bar.addStretch()
		self.nav_bar.addItem("My Account", self.switchSubFrame, self.frame_user, selected=True)
		self.nav_bar.addStretch()
		self.nav_bar.addItem("Engineering", self.switchSubFrame,self.frame_subject)
		self.nav_bar.addItem("Linear Algebra",self.switchSubFrame, self.frame_user)
		self.nav_bar.addItem("Linguistics",self.switchSubFrame, self.frame_user)
		self.nav_bar.addItem("Physics",self.switchSubFrame, self.frame_user)
		self.nav_bar.addStretch()
		self.nav_bar.addStretch()
		self.nav_bar.addStretch()
		self.nav_bar.addStretch()
		self.nav_bar.setContentsMargins(0,0,0,0)

		self.setInitialSubFrame(self.frame_user)

		self.layout.addWidget(self.nav_bar)
		self.layout.addWidget(self.frame_subject)
		self.layout.addWidget(self.frame_user)
		self.setLayout(self.layout)

class TitleFrame(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		self.layout = QVBoxLayout()

		self.label_title = QLabel("AutoLecture")
		self.label_title.setObjectName("setupScreenTitle")
		self.label_title.setAlignment(Qt.AlignCenter)
		self.label_title.setFixedHeight(400)

		self.layout.addWidget(self.label_title)
		self.setLayout(self.layout)


class SetupScreen(QWidget):
	def switchSubFrame(self, next):
		self.active_subframe.hide()
		next.show()
		self.active_subframe = next

	def toggleTitle(self):
		if self.title_frame.isHidden():
			self.title_frame.hide()
		else:
			self.title_frame.show()

	def __init__(self):
		QWidget.__init__(self)

		#	Frames
		self.title_frame = TitleFrame()
		self.login_frame = LoginFrame()
		self.welcome_frame = WelcomeFrame()
		self.loading_frame = LoadingFrame()
		self.subjectConfirmation_frame = SubjectConfirmationFrame(self)

		self.login_frame.hide()
		self.welcome_frame.hide()
		self.loading_frame.hide()
		self.subjectConfirmation_frame.hide()

		self.active_subframe = self.welcome_frame
		self.switchSubFrame(self.welcome_frame)
		####

		self.layout = QVBoxLayout()

		self.layout.addWidget(self.title_frame)			# Top frame

		self.layout.addWidget(self.login_frame)		# Bottom frame
		self.layout.addWidget(self.welcome_frame)
		self.layout.addWidget(self.loading_frame)
		self.layout.addWidget(self.subjectConfirmation_frame)
		
		self.setLayout(self.layout)

class NavigationBar(QWidget):
	@Slot()
	def goToMenu(self):
		self.parent().parent().switchScreen(self.parent().parent().screen_menu)

	@Slot()
	def onSelection(self, button, action, arg1):
		if button != self.selected_button:
			print("Set style")
			button.setProperty('selected', True)
			button.setStyle(button.style())
			self.selected_button.setProperty('selected', False)
			self.selected_button.setStyle(button.style())
			self.selected_button = button
			action(arg1)

	def addStretch(self):
		self.layout.addStretch()

	def addItem(self, text, action, arg1, selected = False):
		button = QPushButton(text)
		button.setObjectName('listButton')
		button.clicked.connect(lambda: self.onSelection(button, action, arg1))

		if selected:
			self.selected_button = button
			button.setProperty('selected', True)
			button.setStyle(button.style())

		self.layout.addWidget(button)


	def __init__(self):
		QWidget.__init__(self)
		self.layout = QVBoxLayout()

		self.hbox_top = QHBoxLayout()

		self.button_back = QPushButton()
		self.button_back.setObjectName('backButton')
		self.pixmap_back = QPixmap("GUI/images/icon_backbutton.png")
		self.icon_back = QIcon(self.pixmap_back)
		self.button_back.setIcon(self.icon_back)
		self.button_back.setIconSize(QSize(80,80));
		self.button_back.clicked.connect(self.goToMenu)
	

		self.label_title = QLabel("Settings")
		self.label_title.setObjectName('settingsTitle')
		self.hbox_top.addWidget(self.button_back)
		self.hbox_top.addWidget(self.label_title)
		self.selected_button = self.button_back

		self.layout.addLayout(self.hbox_top)
		self.setAutoFillBackground(True)
		self.setPalette(QColor('#2F9599'))
		self.setLayout(self.layout)

class WelcomeFrame(QWidget):
	@Slot()
	def start(self):
	    self.parent().switchSubFrame(self.parent().login_frame)
	
	def __init__(self):
		QWidget.__init__(self)

		self.layout = QVBoxLayout()

		self.university_names = ['University of Melbourne', 'Monash University']
		self.uni_list = QComboBox(self)
		self.uni_list.setFixedWidth(800)
		self.uni_list.addItems(self.university_names)
		self.layout.addWidget(self.uni_list,0,Qt.AlignCenter)

		self.pushbutton_login = QPushButton("Start")
		self.pushbutton_login.clicked.connect(self.start)

		self.layout.addStretch()
		self.layout.addWidget(self.pushbutton_login, 0, Qt.AlignCenter)
		self.setLayout(self.layout)

class confirmSubjectWidget(QWidget):
	@Slot()
	def uncomfirmSubject(self):
		if self.confirm_bool == True:
			self.button_confirm.setIcon(assets.icon_tick_grey)
			self.confirm_bool = False
		else:
			self.button_confirm.setIcon(assets.icon_tick_green)
			self.confirm_bool = True

	def __init__(self, title, semester, year, code):
		QWidget.__init__(self)
		self.confirm_bool = False
		self.layout = QHBoxLayout()
		letter_count = len(title +semester + year + code)
		spacing = int((60 - letter_count) / 2)
		if spacing % 2 != 0:
			spacing -= 1
		self.title = QLabel(title + (spacing * " ") + "Semester " + semester + " " + year + (spacing) *  " " + code )
		self.title.setObjectName("rounded")
		#self.semester = QLabel("Semester " + semester)
		#self.semester.setObjectName("rounded")
		#self.year = QLabel(year)
		#self.year.setObjectName("rounded")
		#self.code = QLabel(code)
		#self.code.setObjectName("rounded")

		self.button_confirm = QPushButton()
		self.button_confirm.setObjectName('tickButton')
		self.button_confirm.setIcon(assets.icon_tick_green)
		self.button_confirm.setIconSize(QSize(100,100));
		self.button_confirm.clicked.connect(self.uncomfirmSubject)

		self.layout.addStretch()
		self.layout.addStretch()
		self.layout.addStretch()
		self.layout.addWidget(self.title)
		#self.layout.addWidget(self.code)
		#self.layout.addWidget(self.semester)
		#self.layout.addWidget(self.year)
		self.layout.addWidget(self.button_confirm)
		self.setLayout(self.layout)


class SubjectConfirmationFrame(QWidget): 
	def __init__(self, parent):
		QWidget.__init__(self)
		self.setParent(parent)

		self.label_question = QLabel("These are the subjects we found")
		self.label_question.setObjectName("question")
		self.button_confirm = QPushButton("Next")
		#self.button_confirm.setObjectName("nextButton")

		self.layout = QVBoxLayout()
		self.layout.addStretch()
		self.layout.addWidget(self.label_question, 0, Qt.AlignCenter)
		self.layout.addWidget(confirmSubjectWidget("Linear Algebra", "2", "2017", "MAST10007"), 0, Qt.AlignCenter)
		self.layout.addWidget(confirmSubjectWidget("Engineering Systems Design", "2", "2017", "ENGR10003"), 0, Qt.AlignCenter)
		self.layout.addWidget(confirmSubjectWidget("Physics", "2", "2017", "PHYC10004"), 0, Qt.AlignCenter)
		
		self.layout.addStretch()
		self.layout.addStretch()
		self.layout.addWidget(self.button_confirm, 0, Qt.AlignCenter)
		
		self.setLayout(self.layout)

	def show(self):
		super().show()
		self.parent().title_frame.hide()


class LoginFrame(QWidget):
	@Slot()
	def getLoginInfo(self):
	    print("Username: {}\nPassword: {}".format(self.lineedit_login.text(),self.lineedit_password.text()))
	    self.parent().switchSubFrame(self.parent().loading_frame)
	
	def __init__(self):
		QWidget.__init__(self)

		self.layout = QVBoxLayout()

		self.setLayout(self.layout)
		self.layout.setAlignment(Qt.AlignHCenter)

		form_width = 800
		self.vbox_input = QVBoxLayout()
		self.lineedit_login = QLineEdit()
		self.lineedit_password = QLineEdit()
		self.lineedit_login.setPlaceholderText("Username")
		self.lineedit_password.setPlaceholderText("Password")
		self.lineedit_login.setFixedWidth(form_width)
		self.lineedit_password.setFixedWidth(form_width)

		self.vbox_input.addWidget(self.lineedit_login)
		self.vbox_input.addWidget(self.lineedit_password)

		self.pushbutton_login = QPushButton("Login")
		self.pushbutton_login.clicked.connect(self.getLoginInfo)

		self.layout.addLayout(self.vbox_input)
		self.layout.addStretch()
		self.layout.addWidget(self.pushbutton_login, 0, Qt.AlignCenter)

class LoadingFrame(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		self.layout = QVBoxLayout()

		self.layout.setAlignment(Qt.AlignHCenter)

		self.label_loading_anim = QLabel()
		self.label_loading_anim.setStyleSheet('background:transparent;')
		self.movie_loading_anim = QMovie("GUI/images/loading1.gif")
		self.movie_loading_anim.setSpeed(400)
		self.label_loading_anim.setMovie(self.movie_loading_anim)

		self.effect = QGraphicsColorizeEffect(self)
		self.effect.setStrength(1)
		self.label_loading_anim.setGraphicsEffect(self.effect)
		self.effect.setColor(QColor('#2F9599'))

		self.movie_loading_anim.start()

		self.layout.addWidget(self.label_loading_anim)
		self.layout.addStretch()
		self.setLayout(self.layout)

class ImageFileList(QListWidget):
	def __init__(self, dirpath, parent=None):
		QListWidget.__init__(self, parent)

class SubjectSelectionScreen(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.setMinimumSize(QSize(800, 800))
		self.setWindowTitle('Autolecture')

		self.layout = QVBoxLayout()
		self.list = QListWidget(self)
		self.list.setMinimumSize(QSize(600,600))



	def supported_image_extensions():
		''' Get the image file extensions that can be read. '''
		formats = QImageReader().supportedImageFormats()
		# Convert the QByteArrays to strings
		return [str(fmt) for fmt in formats]
	
	def run(self):
        # Show the form
		self.show()
		# Run the qt application
		qt_app.exec_()
