from PySide6.QtWidgets import (
    QApplication, QMainWindow,
    QPushButton, QLabel,
    QVBoxLayout, QWidget
)
from random import randint
import sys


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another window № % d" % randint(0, 100))
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.window1 = AnotherWindow()
        self.window1.setGeometry(1465,600,250,150)

        self.window2 = AnotherWindow()
        self.window2.setGeometry(931,600,250,150)

        layout = QVBoxLayout()

        self.button1 = QPushButton("Show me Window 1")
        self.button1.clicked.connect(self.toggle_window1)
        layout.addWidget(self.button1)

        self.button2 = QPushButton("Show me Window 2")
        self.button2.clicked.connect(self.toggle_window2)
        layout.addWidget(self.button2)

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

    def toggle_window1(self, checked):
        if self.window1.isVisible():
            self.window1.hide()
            self.button1.setText("Show me Window 1")
        else:
            self.window1.show()
            self.button1.setText("Hide Window 1")

    def toggle_window2(self, checked):
        if self.window2.isVisible():
            self.window2.hide()
            self.button2.setText("Show me Window 2")
        else:
            self.window2.show()
            self.button2.setText("Hide Window 2")
        

app = QApplication(sys.argv)
w = MainWindow()
w.setGeometry(1200,600,250,150)
w.show()
app.exec()
