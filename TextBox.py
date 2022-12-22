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


class TestBox:
    def __init__(self):
        super().__init__()
    def textb(self,x,y):
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(x,y)#(90, 20)
        self.textbox1.resize(40,40)
        self.textbox1.setStyleSheet("background-color: white;")
        self.textbox1.setFont(QFont('Arial', 20))
        self.textbox1.setAlignment(QtCore.Qt.AlignCenter)
        self.textbox1.setMaxLength(1)
        return self.textbox1