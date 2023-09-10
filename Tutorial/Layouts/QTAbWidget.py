import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QTabWidget,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtGui import QPalette, QColor


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        tabs = QTabWidget()

        # To disable bubbled style of MacOS tabs:
        tabs.setDocumentMode(True)
        
        tabs.setTabPosition(QTabWidget.West)
        tabs.setMovable(True)

        for n, color in enumerate(["Red", "Green", "Blue", "Yellow"]):
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)

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
window.setGeometry(600,300,1000,700)
window.show()

app.exec()