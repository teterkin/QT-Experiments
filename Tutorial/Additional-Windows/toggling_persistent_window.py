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

        self.w = AnotherWindow()
        self.w.setGeometry(1465,600,250,150)

        self.button = QPushButton("Show me Window")
        self.button.clicked.connect(self.toggle_window)
        self.setCentralWidget(self.button)

    def toggle_window(self, checked):
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()
        

app = QApplication(sys.argv)
w = MainWindow()
w.setGeometry(1200,600,250,150)
w.show()
app.exec()
