from PyQt5 import QtWidgets
import speech_recognition as sr
from asrInterface import Ui_MainWindow
import sys
import win32api
import threading
import time


def fun_timer():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        audio = r.listen(source)
    command = r.recognize_sphinx(audio).lower()
    if fun_timer() == "website":
        win32api.ShellExecute(0, 'open', 'http://www.baidu.com', '','',1)
    elif fun_timer() == "notebook":
        win32api.ShellExecute(0, 'open', 'notepad.exe', '','',1)
    global timer
    return command 

class myWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        self.myCommand = " "
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.listen()
    
    def listen(self):     
        timer = threading.Timer(3, fun_timer)
        timer.start() 
        time.sleep(15)

if __name__ == '__main__':       
    app = QtWidgets.QApplication(sys.argv)
    application = myWindow()
    sys.exit(app.exec())
    
    
    