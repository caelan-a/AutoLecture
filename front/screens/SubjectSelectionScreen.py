from PySide.QtCore import *
from PySide.QtGui import *

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
