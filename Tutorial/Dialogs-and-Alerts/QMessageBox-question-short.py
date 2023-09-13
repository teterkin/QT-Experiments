import sys

from PySide6.QtWidgets import (
    QApplication, QMainWindow, 
    QMessageBox, QPushButton
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):

        button = QMessageBox.question(self, "Question dialog", 
                                      "\nIs this message longer?\n")

        if button == QMessageBox.Yes:
            print("Yes!")
        else:
            print("No!")

app = QApplication(sys.argv)

window = MainWindow()
window.setGeometry(1200,600,480,320)
window.show()

app.exec()