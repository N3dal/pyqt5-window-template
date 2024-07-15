from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from defaults import *


class MainWindow(QMainWindow):

    class Signals(QObject):
        pass

    def __init__(self, name=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__signals = MainWindow.Signals()

        self.__window_name = "Application-MainWindow" if name is None else name

    def set_window_name(self, name: str) -> None:
        self.__window_name = name

        return None

    @property
    def signals(self) -> QObject:
        return self.__signals

    @property
    def name(self):
        return self.__window_name
