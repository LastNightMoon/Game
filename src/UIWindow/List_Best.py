# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'List_Best.ui'
#
# Created by: PyQt5 UIWindow code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_List_Best(object):
    def setupUi(self, List_Best):
        List_Best.setObjectName("List_Best")
        List_Best.resize(1076, 650)
        self.back_button = QtWidgets.QPushButton(List_Best)
        self.back_button.setGeometry(QtCore.QRect(10, 580, 181, 51))
        self.back_button.setStyleSheet("font: 22pt \"Berlin Sans FB\"; color: rgb(175,238,238);\n"
"background-color: rgb(204, 204, 204, 0);")
        self.back_button.setObjectName("back_button")

        self.pushvper = QtWidgets.QPushButton(List_Best)
        self.pushvper.setGeometry(QtCore.QRect(980, 80, 93, 341))
        self.pushvper.setStyleSheet("font: 42pt \"Berlin Sans FB\"; color: rgb(175,238,238);\n"
                                    "background-color: rgb(204, 204, 204, 0);")
        self.pushvper.setObjectName("pushvper")
        self.pushnaz = QtWidgets.QPushButton(List_Best)
        self.pushnaz.setGeometry(QtCore.QRect(0, 80, 93, 371))
        self.pushnaz.setStyleSheet("font: 42pt \"Berlin Sans FB\"; color: rgb(175,238,238);\n"
                                   "background-color: rgb(204, 204, 204, 0);")
        self.pushnaz.setObjectName("pushnaz")

        self.retranslateUi(List_Best)
        QtCore.QMetaObject.connectSlotsByName(List_Best)

    def retranslateUi(self, List_Best):
        _translate = QtCore.QCoreApplication.translate
        List_Best.setWindowTitle(_translate("List_Best", "Лучшие игроки"))
        self.back_button.setText(_translate("List_Best", "Назад"))
        self.pushnaz.setText(_translate("List_Best", "<"))
        self.pushvper.setText(_translate("List_Best", ">"))
