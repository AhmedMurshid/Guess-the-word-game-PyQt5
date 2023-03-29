import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QHBoxLayout
from PyQt6.QtGui import QIcon
from TextBox import TestBox
from Functions import *

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Guess the Word'
        self.left = 1000
        self.top = 100
        self.width = 500
        self.height = 340
        self.points = 0
        # self.word1 = ""
        self.wordToFind = ""
        # self.match()
        self.initUI()
        self.bg()

    def bg(self):
        self.setStyleSheet("background-color:cornflowerblue;"
                           "border: 3px solid black;")

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox for each letter
        text1 = TestBox.textb(self, 90, 20)
        text2 = TestBox.textb(self, 150, 20)
        text3 = TestBox.textb(self, 210, 20)
        text4 = TestBox.textb(self, 270, 20)

        # Create a button in the window
        self.button = QPushButton('Enter', self)
        self.button.setStyleSheet("background-color: white;")
        self.button.move(90, 300)

        # connect button to function on_click
        # self.button.clicked.connect(AppFunctions.on_click(text1,text2,text3,text4, wordToFind = self.word_to_find))
        wordToFind = self.word_to_find()
        # self.button.clicked.connect(lambda: AppFunctions.on_click(self, w1 = text1, w2 = text2, w3 = text3, w4 = text4, wordToFind))
        # self.button.clicked.connect(lambda _, w1=text1, w2=text2, w3=text3, w4=text4: AppFunctions.on_click(self, w1, w2, w3, w4, wordToFind))
        self.button.clicked.connect(lambda _, w1=text1, w2=text2, w3=text3, w4=text4: AppFunctions.on_click(self, w1, w2, w3, w4, self.word_to_find()))



        self.show()
    def word_to_find(self):
            word = ["cool","time","more"]
            # wordToFind.append(word)
            
            wordToFind1 = random.choice(word)
            print("Looking for:", wordToFind1)
            return wordToFind1
    def wait(self):
            for i in range(1, 200):
                # Sleep five seconds in total
                for _ in range(5 * 10):
                    # Process events between short sleep periods
                    QApplication.processEvents()
                    #QtCore.QTime().sleep(0.1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())
