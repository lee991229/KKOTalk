# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page_talk_room_list_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tk_room_list_widget(object):
    def setupUi(self, tk_room_list_widget):
        tk_room_list_widget.setObjectName("tk_room_list_widget")
        tk_room_list_widget.resize(600, 850)
        self.verticalLayout = QtWidgets.QVBoxLayout(tk_room_list_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(tk_room_list_widget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btn_tkroom_close = QtWidgets.QPushButton(self.frame_2)
        self.btn_tkroom_close.setObjectName("btn_tkroom_close")
        self.horizontalLayout_2.addWidget(self.btn_tkroom_close)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.frame_7)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.btn_tkroom_search = QtWidgets.QPushButton(self.frame_7)
        self.btn_tkroom_search.setObjectName("btn_tkroom_search")
        self.horizontalLayout_8.addWidget(self.btn_tkroom_search)
        self.btn_tallk_room_make = QtWidgets.QPushButton(self.frame_7)
        self.btn_tallk_room_make.setObjectName("btn_tallk_room_make")
        self.horizontalLayout_8.addWidget(self.btn_tallk_room_make)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.widget_3 = QtWidgets.QWidget(self.frame_3)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit_tkroom_search = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_tkroom_search.setObjectName("lineEdit_tkroom_search")
        self.horizontalLayout_6.addWidget(self.lineEdit_tkroom_search)
        self.btn_tkroom_click_search = QtWidgets.QPushButton(self.widget_3)
        self.btn_tkroom_click_search.setObjectName("btn_tkroom_click_search")
        self.horizontalLayout_6.addWidget(self.btn_tkroom_click_search)
        self.verticalLayout_3.addWidget(self.widget_3)
        self.frame_11 = QtWidgets.QFrame(self.frame_3)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_12 = QtWidgets.QFrame(self.frame_11)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.btn_friend_list_page = QtWidgets.QPushButton(self.frame_12)
        self.btn_friend_list_page.setObjectName("btn_friend_list_page")
        self.verticalLayout_7.addWidget(self.btn_friend_list_page)
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_7.addWidget(self.pushButton_11)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem2)
        self.horizontalLayout_9.addWidget(self.frame_12)
        self.frame_4 = QtWidgets.QFrame(self.frame_11)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.frame_4)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.tkroom_list_area = QtWidgets.QWidget()
        self.tkroom_list_area.setGeometry(QtCore.QRect(0, 0, 417, 585))
        self.tkroom_list_area.setObjectName("tkroom_list_area")
        self.scrollArea_2.setWidget(self.tkroom_list_area)
        self.verticalLayout_10.addWidget(self.scrollArea_2)
        self.verticalLayout_2.addLayout(self.verticalLayout_10)
        self.horizontalLayout_9.addWidget(self.frame_4)
        self.verticalLayout_3.addWidget(self.frame_11)
        self.frame = QtWidgets.QFrame(self.frame_3)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout_3.addWidget(self.frame)
        self.verticalLayout.addWidget(self.frame_3)

        self.retranslateUi(tk_room_list_widget)
        QtCore.QMetaObject.connectSlotsByName(tk_room_list_widget)

    def retranslateUi(self, tk_room_list_widget):
        _translate = QtCore.QCoreApplication.translate
        tk_room_list_widget.setWindowTitle(_translate("tk_room_list_widget", "Form"))
        self.label.setText(_translate("tk_room_list_widget", "크크오톡,채팅방 이름"))
        self.btn_tkroom_close.setText(_translate("tk_room_list_widget", "x"))
        self.label_6.setText(_translate("tk_room_list_widget", "채팅"))
        self.btn_tkroom_search.setText(_translate("tk_room_list_widget", "검색"))
        self.btn_tallk_room_make.setText(_translate("tk_room_list_widget", "방만들기"))
        self.btn_tkroom_click_search.setText(_translate("tk_room_list_widget", "PushButton"))
        self.btn_friend_list_page.setText(_translate("tk_room_list_widget", "친구"))
        self.pushButton_11.setText(_translate("tk_room_list_widget", "PushButton"))
        self.label_2.setText(_translate("tk_room_list_widget", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tk_room_list_widget = QtWidgets.QWidget()
    ui = Ui_tk_room_list_widget()
    ui.setupUi(tk_room_list_widget)
    tk_room_list_widget.show()
    sys.exit(app.exec_())
