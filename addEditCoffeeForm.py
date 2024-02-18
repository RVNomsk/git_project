# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(572, 340)
        MainWindow.setMinimumSize(QtCore.QSize(572, 340))
        MainWindow.setMaximumSize(QtCore.QSize(572, 340))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 321, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.id = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.id.setObjectName("id")
        self.verticalLayout.addWidget(self.id)
        self.variety_name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.variety_name.setObjectName("variety_name")
        self.verticalLayout.addWidget(self.variety_name)
        self.degree_of_roasting = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.degree_of_roasting.setObjectName("degree_of_roasting")
        self.verticalLayout.addWidget(self.degree_of_roasting)
        self.ground_or_beans = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.ground_or_beans.setObjectName("ground_or_beans")
        self.verticalLayout.addWidget(self.ground_or_beans)
        self.description_of_taste = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.description_of_taste.setObjectName("description_of_taste")
        self.verticalLayout.addWidget(self.description_of_taste)
        self.price = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.price.setObjectName("price")
        self.verticalLayout.addWidget(self.price)
        self.packaging_volume_gram = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.packaging_volume_gram.sizePolicy().hasHeightForWidth())
        self.packaging_volume_gram.setSizePolicy(sizePolicy)
        self.packaging_volume_gram.setObjectName("packaging_volume_gram")
        self.verticalLayout.addWidget(self.packaging_volume_gram)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(350, 20, 201, 251))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 4, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.id_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.id_2.setObjectName("id_2")
        self.verticalLayout_2.addWidget(self.id_2)
        self.variety_name_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.variety_name_2.setObjectName("variety_name_2")
        self.verticalLayout_2.addWidget(self.variety_name_2)
        self.degree_of_roasting_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.degree_of_roasting_2.setObjectName("degree_of_roasting_2")
        self.verticalLayout_2.addWidget(self.degree_of_roasting_2)
        self.ground_or_beans_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.ground_or_beans_2.setObjectName("ground_or_beans_2")
        self.verticalLayout_2.addWidget(self.ground_or_beans_2)
        self.description_of_taste_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.description_of_taste_2.setObjectName("description_of_taste_2")
        self.verticalLayout_2.addWidget(self.description_of_taste_2)
        self.price_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.price_2.setObjectName("price_2")
        self.verticalLayout_2.addWidget(self.price_2)
        self.packaging_volume_gram_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.packaging_volume_gram_2.setObjectName("packaging_volume_gram_2")
        self.verticalLayout_2.addWidget(self.packaging_volume_gram_2)
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(20, 290, 121, 23))
        self.add_btn.setObjectName("add_btn")
        self.edit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.edit_btn.setGeometry(QtCore.QRect(220, 290, 121, 23))
        self.edit_btn.setObjectName("edit_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Добавить / изменить запись"))
        self.id_2.setText(_translate("MainWindow", "ID"))
        self.variety_name_2.setText(_translate("MainWindow", "Название сорта"))
        self.degree_of_roasting_2.setText(_translate("MainWindow", "Степень обжарки"))
        self.ground_or_beans_2.setText(_translate("MainWindow", "Молотый/в зернах"))
        self.description_of_taste_2.setText(_translate("MainWindow", "Описание вкуса"))
        self.price_2.setText(_translate("MainWindow", "Цена"))
        self.packaging_volume_gram_2.setText(_translate("MainWindow", "Объем упаковки"))
        self.add_btn.setText(_translate("MainWindow", "Добавить запись"))
        self.edit_btn.setText(_translate("MainWindow", "Изменить запись"))