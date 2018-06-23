import os, sys
from PySide.QtCore import *
from PySide.QtGui import *

from front.MainWindow import Window  

os.path.join(os.path.dirname(__file__))

qt_app = QApplication(sys.argv)
window = Window()
window.setInitialScreen(window.screen_setup)
window.run(qt_app)
