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
        self.button1.clicked.connect(
            lambda checked: self.toggle_window(
                self.window1, 
                self.button1, 
                "1"
                )
        )
        layout.addWidget(self.button1)

        self.button2 = QPushButton("Show me Window 2")
        self.button2.clicked.connect(
            lambda checked: self.toggle_window(
                self.window2, 
                self.button2, 
                "2"
                )
        )
        layout.addWidget(self.button2)

        w = QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)

    def toggle_window(self, window, button, number):
        if window.isVisible():
            window.hide()
            button.setText("Show me Window " + number)
        else:
            window.show()
            button.setText("Hide Window " + number)
        

app = QApplication(sys.argv)
w = MainWindow()
w.setGeometry(1200,600,250,150)
w.show()
app.exec()
