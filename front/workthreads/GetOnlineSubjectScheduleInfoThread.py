import sys, time
from PySide.QtGui import *
from PySide.QtCore import *

class MySignal(QObject):
        new_loading_text = Signal(str)

class GetOnlineSubjectScheduleInfo(QThread):
        def __init__(self, parent, back_end, set_loading_text_function):
                QThread.__init__(self, parent)
                self.exiting = False
                self.back_end = back_end

                #       Connect loading text functionality
                self.sig = MySignal()
                self.sig.new_loading_text.connect(set_loading_text_function)

                #       Backend
                self.back_end = back_end

        def setLoadingText(self, text):
                self.sig.new_loading_text.emit(text)

        def run(self):
                while self.exiting == False:
                        self.setLoadingText('Fetching subjects from LMS')
                        self.back_end.getTimeTable()
                        self.back_end.getSubjectsToAddScheduleInfo()
                        self.setLoadingText('Subjects have been fetched')
                        self.exiting = True



                        
