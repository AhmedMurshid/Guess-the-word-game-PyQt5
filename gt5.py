import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication,
                             QWidget, QPushButton,QAction,
                             QLineEdit, QMessageBox, QLabel,
                             QHBoxLayout)
from PyQt5.QtGui import QIcon,QColor, QFont
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random
from TextBox import TestBox
class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Guess the Word'
        self.left = 500
        self.top = 300
        self.width = 400
        self.height = 140
        self.points = 0
        self.initUI()
        self.bg()
        self.word1 = "word"
        self.wordToFind = ""
        self.get_User_word()
        self.match()
        self.wait()
        
    def bg(self):
        self.setStyleSheet("background-color:cornflowerblue;"
                           "border: 3px solid black;")
        self.show
    def initUI(self):
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        # Create textbox for each letter 
        self.textbox1 = TestBox.textb(self,90,20)
        self.textbox2 = TestBox.textb(self,150,20)
        self.textbox3 = TestBox.textb(self,210,20)
        self.textbox4 = TestBox.textb(self,270,20)
        # Create a button in the window
        self.button = QPushButton('Enter', self)
        self.button.setStyleSheet("background-color: white;")
        self.button.move(90,80)
        
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        #self.is_a_word(word)

        self.show()
    
    #@pyqtSlot()
    def on_click(self):
        QApplication.processEvents()

        value1 = self.textbox1.text()
        value2 = self.textbox2.text()
        value3 = self.textbox3.text()
        value4 = self.textbox4.text()
        #QMessageBox.question(self, 'Message - enter', "You typed: " + value1, QMessageBox.Ok)
        word = (value1+value2+value3+value4)
        self.points
        self.set_User_word(word)
        self.word_to_find()
        self.get_User_word()
        self.match()
        QApplication.processEvents()
      
    def set_User_word(self,wordone):
        self.word1 = wordone
    def get_User_word(self):
        print("Your word: ",self.word1)
    def word_to_find(self):
        word = ["cool","time","more"]
        
        self.wordToFind = random.choice(word)
        print("Looking for:",self.wordToFind)
    def match(self):
        if(self.wordToFind == self.word1):
            QApplication.processEvents()
            self.points += 1
            print("True")
            self.textbox1.clear()
            self.textbox2.clear()
            self.textbox3.clear()
            self.textbox4.clear()
            self.setStyleSheet("background-color:green;"
                           "border: 3px solid black;")
            self.show
            self.wait()
            QApplication.processEvents()
            self.setStyleSheet("background-color:cornflowerblue;"
                           "border: 3px solid black;")
            self.show
            return True
        elif(self.wordToFind == ""):
            return
        else:
            self.setStyleSheet("background-color:red;"
                           "border: 3px solid black;")
            self.show
            self.wait()
            QApplication.processEvents()
            self.setStyleSheet("background-color:cornflowerblue;"
                           "border: 3px solid black;")
            self.show
            return False
    # wait function
    def wait(self):
        for i in range(1, 200):
            #print(i)
            # Sleep five seconds in total
            for _ in range(5 * 10):
                # Process events between short sleep periods
                QApplication.processEvents()
                #QtCore.QTime().sleep(0.1)
        
            
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
