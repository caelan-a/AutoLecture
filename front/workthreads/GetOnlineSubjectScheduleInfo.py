import sys, time
from PySide.QtGui import *
from PySide.QtCore import *

class MySignal(QObject):
        new_loading_text = Signal(str)
        go_to_next_frame = Signal()

class GetOnlineSubjectScheduleInfo(QThread):
        def __init__(self, parent, back_end, set_loading_text_function, subject_confirmation_frame):
                QThread.__init__(self, parent)
                self.exiting = False
                self.back_end = back_end
                self.subject_confirmation_frame = subject_confirmation_frame

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
                        self.back_end.getSubjectLMSInfo()
                        self.setLoadingText('Subjects have been fetched')
                        self.exiting = True



                        
