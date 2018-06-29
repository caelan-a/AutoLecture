import sys, time
from PySide.QtGui import *
from PySide.QtCore import *

class MySignal(QObject):
        sig = Signal(str)

class GetSubjectInfoThread(QThread):
        def __init__(self, parent, set_loading_text_function):
                QThread.__init__(self, parent)
                self.exiting = False

                self.new_loading_action_signal = MySignal()
                self.new_loading_action_signal.sig.connect(set_loading_text_function)

        def run(self):
                end = time.time()+5
                new_loading_action_text = 'Fetching subjects from LMS'
                self.new_loading_action_signal.sig.emit(new_loading_action_text)
                while self.exiting==False:
                        sys.stdout.write('*')
                        sys.stdout.flush()
                        time.sleep(1)
                        now = time.time()
                        if now>=end:
                                self.exiting=True 
                new_loading_action_text = 'Subjects have been fetched'
                self.new_loading_action_signal.sig.emit(new_loading_action_text)
