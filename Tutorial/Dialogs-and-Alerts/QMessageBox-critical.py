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

        button = QMessageBox.critical(
            self, 
            "Oh dear!",
            "\nSomething went very wrong.\n",
            buttons=QMessageBox.Discard | 
            QMessageBox.NoToAll | QMessageBox.Ignore,
            defaultButton=QMessageBox.Discard
            )

        if button == QMessageBox.Discard:
            print("Discard!")
        elif button == QMessageBox.NoToAll:
            print("No to all!")
        else:
            print("Ignore!")

app = QApplication(sys.argv)

window = MainWindow()
window.setGeometry(1200,600,480,320)
window.show()

app.exec()