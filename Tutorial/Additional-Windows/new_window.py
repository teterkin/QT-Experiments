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
        self.button = QPushButton("Push me for new Window!")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self, checked):
        if self.w is None:
            self.w = AnotherWindow()
        self.w.setGeometry(1465,600,250,150)
        self.w.show()    


app = QApplication(sys.argv)
w = MainWindow()
w.w = None
w.setGeometry(1200,600,250,150)
w.show()
app.exec()
