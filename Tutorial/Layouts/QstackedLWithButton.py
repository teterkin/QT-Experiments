import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtGui import QPalette, QColor


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        pagelayout = QVBoxLayout()

        button_layout = QHBoxLayout()
        
        btn1 = QPushButton("red")
        btn1.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(btn1)
        

        btn2 = QPushButton("green")
        btn2.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(btn2)
        

        btn3 = QPushButton("yellow")
        btn3.pressed.connect(self.activate_tab_3)
        button_layout.addWidget(btn3)

        self.stacklayout = QStackedLayout()
        self.stacklayout.addWidget(Color("red"))
        self.stacklayout.addWidget(Color("green"))
        self.stacklayout.addWidget(Color("yellow"))
        self.stacklayout.setCurrentIndex(1)


        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stacklayout)

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

    def activate_tab_1(self):
        self.stacklayout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stacklayout.setCurrentIndex(1)

    def activate_tab_3(self):
        self.stacklayout.setCurrentIndex(2)

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()