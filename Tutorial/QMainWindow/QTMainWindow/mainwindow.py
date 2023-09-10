# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("My App")
        button = QPushButton("Press me!")
        self.setFixedSize(QSize(400, 300))
        # self.setMinimumSize(QSize(400, 300))
        self.setMaximumSize(QSize(800, 600))
        self.setCentralWidget(button)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
