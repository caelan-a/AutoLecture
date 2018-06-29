from PySide.QtCore import *
from PySide.QtGui import *

class SubjectSelectionScreen(QWidget):
	def __init__(self,assets):
		QWidget.__init__(self)
		self.setMinimumSize(QSize(800, 800))
		self.setWindowTitle('Autolecture')

		self.layout = QVBoxLayout()
		self.list = QListWidget(self)
		self.list.setMinimumSize(QSize(600,600))

	def run(self):
        # Show the form
		self.show()
		# Run the qt application
		qt_app.exec_()
