import sys
from PySide.QtCore import *
from PySide.QtGui import *

from GUI.gui import Window  

qt_app = QApplication(sys.argv)
app = Window()
app.setInitialScreen(app.screen_setup)
app.run(qt_app)


# 1. Change schedule in settings using lecture_list available sessions algo
# 2. Allow alternate viewing of ALL lectures to download specific unscheduled lectures
# 3. 
#
#
#
#
#
#
#
#
#
