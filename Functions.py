from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QHBoxLayout

import random

class AppFunctions():
    def __init__(self): 
        # self =
        super().__init__()



    @pyqtSlot()
    def on_click(self,w1,w2,w3,w4,wordToFind):
        value1 = w1.text()
        value2 = w2.text()
        value3 = w3.text()
        value4 = w4.text()

        word = (""+(value1)+""+value2+""+value3+""+value4)
        print("the first letter:", value1)
        print("the word u picked",word)
        
        if wordToFind == word:
            # points += 1
            print("True")

            # textbox1.clear()
            # textbox2.clear()
            # textbox3.clear()
            # self.textbox4.clear()

            self.setStyleSheet("background-color:green;"
                                "border: 3px solid black;")
            # wait()
            for i in range(1, 200):
                # Sleep five seconds in total
                for _ in range(5 * 10):
                    # Process events between short sleep periods
                    QApplication.processEvents()

            self.setStyleSheet("background-color:cornflowerblue;"
                                "border: 3px solid black;")
        elif wordToFind == "":
            return 
        elif wordToFind != word:
            self.setStyleSheet("background-color:red;"
                                "border: 3px solid black;")
            # wait()
            for i in range(1, 200):
                # Sleep five seconds in total
                for _ in range(5 * 10):
                    # Process events between short sleep periods
                    QApplication.processEvents()

            self.setStyleSheet("background-color:cornflowerblue;"
                                "border: 3px solid black;")
    
    # wait function

