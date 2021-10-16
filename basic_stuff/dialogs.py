#!/usr/bin/python

from PyQt6.QtWidgets import (QWidget, QPushButton, QLineEdit,
        QInputDialog, QApplication, QFrame, QColorDialog, 
        QSizePolicy, QLabel, QFontDialog, QTextEdit, QFileDialog)
from PyQt6.QtGui import QColor, QAction, QIcon
import sys
from pathlib import Path


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        ### Name bit
        self.btn = QPushButton('Change Name', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)
        ################################
        
        ### Color bit
        col = QColor(0, 0, 0)
        self.btn_color = QPushButton('Pick color', self)
        self.btn_color.move(20, 60)
        self.btn_color.clicked.connect(self.showColorDialog)
        
        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }"
                               % col.name())
        self.frm.setGeometry(130, 60, 200, 200)
        ################################
        
        ### Font Picker bit
        self.btn_font = QPushButton('Dialog', self)
        self.btn_font.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.btn_font.move(20, 300)
        
        self.btn_font.clicked.connect(self.showFontPickerDialog)
        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(130, 300)
        ################################

        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Input dialog')
        self.show()


    def showDialog(self):

        text, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Enter your name:')

        if ok:
            self.le.setText(str(text))

    def showColorDialog(self):

        col = QColorDialog.getColor()

        if col.isValid():

            self.frm.setStyleSheet("QWidget { background-color: %s }" 
                                   % col.name())
    
    def showFontPickerDialog(self):

        font, ok = QFontDialog.getFont()

        if ok:
            self.lbl.setFont(font)

def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()