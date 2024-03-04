# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'New_world.ui'
#
# Created by: PyQt5 UIWindow code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1076, 650)
        self.name_text = QtWidgets.QLabel(Form)
        self.name_text.setGeometry(QtCore.QRect(50, 30, 61, 51))
        self.name_text.setStyleSheet("font: 8pt \"Berlin Sans FB\"; color: rgb(175,238,238);\n"
"background-color: rgb(204, 204, 204, 0);")
        self.name_text.setObjectName("name_text")
        self.name_label = QtWidgets.QTextEdit(Form)
        self.name_label.setGeometry(QtCore.QRect(130, 40, 181, 31))
        self.name_label.setObjectName("name_label")
        self.accidentally_name_btn = QtWidgets.QPushButton(Form)
        self.accidentally_name_btn.setGeometry(QtCore.QRect(310, 40, 71, 31))
        self.accidentally_name_btn.setStyleSheet("font: 8pt \"Berlin Sans FB\"; color: rgb(175,238,238);\n"
"background-color: rgb(204, 204, 204, 0);")
        self.accidentally_name_btn.setObjectName("accidentally_name_btn")
        self.key_text = QtWidgets.QLabel(Form)
        self.key_text.setGeometry(QtCore.QRect(20, 80, 111, 31))
        self.key_text.setStyleSheet("font: 8pt \"Berlin Sans FB\"; color: rgb(175,238,238);\n"
"background-color: rgb(204, 204, 204, 0);")
        self.key_text.setObjectName("key_text")
        self.accidentally_key_btn = QtWidgets.QPushButton(Form)
        self.accidentally_key_btn.setGeometry(QtCore.QRect(310, 80, 71, 31))
        self.accidentally_key_btn.setStyleSheet("font: 8\n"
"pt \"Berlin Sans FB\"; color: rgb(175,238,238);\n"
"background-color: rgb(204, 204, 204, 0);")
        self.accidentally_key_btn.setObjectName("accidentally_key_btn")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(130, 80, 181, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.radioButton_litlle = QtWidgets.QRadioButton(Form)
        self.radioButton_litlle.setGeometry(QtCore.QRect(130, 220, 111, 17))
        self.radioButton_litlle.setStyleSheet("color: rgb(120, 255, 99);\n"
"")
        self.radioButton_litlle.setChecked(True)
        self.radioButton_litlle.setObjectName("radioButton_litlle")
        self.radioButton_average = QtWidgets.QRadioButton(Form)
        self.radioButton_average.setGeometry(QtCore.QRect(130, 237, 82, 20))
        self.radioButton_average.setStyleSheet("color: rgb(255, 153, 70);")
        self.radioButton_average.setObjectName("radioButton_average")
        self.radioButton_big = QtWidgets.QRadioButton(Form)
        self.radioButton_big.setGeometry(QtCore.QRect(130, 250, 71, 31))
        self.radioButton_average.setGeometry(QtCore.QRect(130, 237, 111, 20))
        self.radioButton_average.setStyleSheet("color: rgb(255, 153, 70);")
        self.radioButton_average.setObjectName("radioButton_average")
        self.radioButton_big = QtWidgets.QRadioButton(Form)
        self.radioButton_big.setGeometry(QtCore.QRect(130, 250, 111, 31))
        self.radioButton_big.setStyleSheet("color: rgb(255, 42, 63);")
        self.radioButton_big.setObjectName("radioButton_big")
        self.create_btn = QtWidgets.QPushButton(Form)
        self.create_btn.setGeometry(QtCore.QRect(330, 390, 251, 101))
        self.create_btn.setStyleSheet("font: 22pt \"Berlin Sans FB\"; color: rgb(175,238,238);\n"
"background-color: rgb(204, 204, 204, 0);")
        self.create_btn.setObjectName("create_btn")
        self.label_error = QtWidgets.QLabel(Form)
        self.label_error.setGeometry(QtCore.QRect(380, 10, 671, 121))
        self.label_error.setStyleSheet("font: 22pt \"Berlin Sans FB\"; color: rgb(175,238,238);\n"
"background-color: rgb(204, 204, 204, 0);")
        self.label_error.setText("")
        self.label_error.setObjectName("label_error")
        self.back_button = QtWidgets.QPushButton(Form)
        self.back_button.setGeometry(QtCore.QRect(30, 590, 121, 41))
        self.back_button.setStyleSheet("font: 22pt \"Berlin Sans FB\"; color: rgb(175,238,238);\n"
"background-color: rgb(204, 204, 204, 0);")
        self.back_button.setObjectName("back_button")
        self.label_v = QtWidgets.QLabel(Form)
        self.label_v.setGeometry(QtCore.QRect(30, 120, 411, 91))
        self.label_v.setStyleSheet("font: 22pt \"Berlin Sans FB\"; color: rgb(175,238,238);\n"
"background-color: rgb(204, 204, 204, 0);")
        self.label_v.setObjectName("label_v")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        Form.setWindowTitle(_translate("Form", "Новый мир"))
        self.name_text.setText(_translate("Form", "Название:"))
        self.accidentally_name_btn.setText(_translate("Form", "Случайно"))
        self.key_text.setText(_translate("Form", "Ключ генерации:"))
        self.accidentally_key_btn.setText(_translate("Form", "Случайно"))
        self.radioButton_litlle.setText(_translate("Form", "Маленький"))
        self.radioButton_average.setText(_translate("Form", "Средний "))
        self.radioButton_big.setText(_translate("Form", "Большой"))
        self.create_btn.setText(_translate("Form", "Создать"))
        self.back_button.setText(_translate("Form", "Назад"))
        self.label_v.setText(_translate("Form", "Выберите тип мира"))