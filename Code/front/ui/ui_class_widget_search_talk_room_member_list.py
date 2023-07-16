# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_search_talk_room_member_list.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_talk_room_member_list_widget(object):
    def setupUi(self, talk_room_member_list_widget):
        talk_room_member_list_widget.setObjectName("talk_room_member_list_widget")
        talk_room_member_list_widget.resize(554, 296)
        talk_room_member_list_widget.setStyleSheet("#talk_room_member_list_widget {\n"
"    background-color: #75C2F6;\n"
"    color: #1D5D9B;\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"    color: #1D5D9B;\n"
"    font: bold 16pt \"나눔고딕\";\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color:#F4D160;\n"
"    color: #1D5D9B;\n"
"    font: bold 12pt \"나눔고딕\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:#FFFF9D;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color:#FEF5AC;\n"
"}\n"
"\n"
"\n"
"#label_title{\n"
"    font: bold 20pt \"나눔고딕\";\n"
"    color: #F4D160;\n"
"}\n"
"\n"
"#frame_title{\n"
"    background-color: #1D5D9B;\n"
"}    \n"
"QLineEdit{\n"
"    color: #1D5D9B;\n"
"    font: bold 12pt \"나눔고딕\";\n"
"}\n"
"")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(talk_room_member_list_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(talk_room_member_list_widget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(449, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_flist_close = QtWidgets.QPushButton(self.frame)
        self.btn_flist_close.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_flist_close.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_flist_close.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_flist_close.setIcon(icon)
        self.btn_flist_close.setObjectName("btn_flist_close")
        self.horizontalLayout.addWidget(self.btn_flist_close)
        self.verticalLayout.addWidget(self.frame)
        self.scrollArea = QtWidgets.QScrollArea(talk_room_member_list_widget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.widget_user_list = QtWidgets.QWidget()
        self.widget_user_list.setGeometry(QtCore.QRect(0, 0, 532, 218))
        self.widget_user_list.setObjectName("widget_user_list")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_user_list)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_to_add_item = QtWidgets.QWidget(self.widget_user_list)
        self.widget_to_add_item.setObjectName("widget_to_add_item")
        self.verticalLayout_3.addWidget(self.widget_to_add_item)
        self.widget_to_spacer = QtWidgets.QWidget(self.widget_user_list)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_to_spacer.sizePolicy().hasHeightForWidth())
        self.widget_to_spacer.setSizePolicy(sizePolicy)
        self.widget_to_spacer.setObjectName("widget_to_spacer")
        self.verticalLayout_3.addWidget(self.widget_to_spacer)
        self.scrollArea.setWidget(self.widget_user_list)
        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(talk_room_member_list_widget)
        QtCore.QMetaObject.connectSlotsByName(talk_room_member_list_widget)

    def retranslateUi(self, talk_room_member_list_widget):
        _translate = QtCore.QCoreApplication.translate
        talk_room_member_list_widget.setWindowTitle(_translate("talk_room_member_list_widget", "Form"))
        self.label.setText(_translate("talk_room_member_list_widget", "참여 인원 목록"))
from Code.front.ui import my_qrc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    talk_room_member_list_widget = QtWidgets.QWidget()
    ui = Ui_talk_room_member_list_widget()
    ui.setupUi(talk_room_member_list_widget)
    talk_room_member_list_widget.show()
    sys.exit(app.exec_())
