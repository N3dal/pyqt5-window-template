from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from main_window import MainWindow


def main():

    app = QApplication(sys.argv)

    root = MainWindow(name="Application-MainWindow")

    root.show()

    exit(app.exec())


if __name__ == "__main__":
    main()
