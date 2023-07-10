from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Code.front.ui.ui_class_page_join_ui import ui_join_widget

class JoinWidget(QWidget, ui_join_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
