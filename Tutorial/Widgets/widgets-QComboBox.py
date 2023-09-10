import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDial,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QSlider,
    QSpinBox,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        combobox = QComboBox()
        combobox.addItems(["One", "Two", "Three"])

        combobox.currentTextChanged.connect(self.text_changed)
        combobox.currentIndexChanged.connect(self.index_changed)
        # combobox.setEditable(True)
        # combobox.setMaxCount(10)
        # combobox.setInsertPolicy(QComboBox.InsertAtCurrent)

        self.setCentralWidget(combobox)

    def text_changed(self, text):
        print(text)

    def index_changed(self, index):
        print(index)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()