import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QLineEdit, QMessageBox, QLabel, QHBoxLayout
from PyQt6.QtGui import QIcon, QColor, QFont
from PyQt6 import QtCore
from PyQt6.QtCore import pyqtSlot

import random
from test import *


class TestBox(QWidget):
    def __init__(self):
        super().__init__()

    def textb(self, x, y):
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(x, y)
        self.textbox1.resize(40, 40)
        self.textbox1.setStyleSheet("background-color: white;")
        self.textbox1.setFont(QFont('Arial', 20))
        self.textbox1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.textbox1.setMaxLength(1)
        return self.textbox1

    def textb2(self, x, y, letter):
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(x, y)
        self.textbox1.resize(40, 40)
        self.textbox1.setStyleSheet("background-color: white;")
        self.textbox1.setFont(QFont('Arial', 20))
        self.textbox1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.textbox1.setMaxLength(1)
        self.textbox1.setText(letter)
        self.textbox1.setReadOnly(True)
        return self.textbox1

    def buttons(self, x, y, letter):
        self.button = QPushButton(letter, self)
        self.button.setStyleSheet("background-color: white;")
        self.button.move(x, y)
        self.button.setFont(QFont('Arial', 20))
        return self.button

    def wordbank(self, arr2):
        arr = []
        arr.extend(arr2)
        letters = []
        for word in arr:
            for letter in word:
                letters.append(letter)
        size = len(letters)
        x = 90  # for box
        y = 20  # first row
        for i in range(size):  # i x aixs
            self.newtb = TestBox.buttons(self, x, y, letters[i])
            return self.newtb
            x += 60
            if x == 330:
                y += 60
                x = 90

    # self.newtb.clicked.connect(self.on_click)
    # @pyqtSlot()
    # def on_click2(self):
    #     print_letter(self)
    #     self.match()
    # def print_letter(lineEdit):
    #     print(f"{lineEdit.text()} was clicked")
