# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Evaluator.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication,
                            QMetaObject,
                            QSize, Qt)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QLineEdit,
                               QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
                               QTextBrowser, QToolButton, QVBoxLayout)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(492, 391)
        MainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.verticalLayout_6 = QVBoxLayout(MainWindow)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(MainWindow)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Consolas"])
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.file_name = QLineEdit(MainWindow)
        self.file_name.setObjectName(u"file_name")
        self.file_name.setFont(font)
        self.file_name.setReadOnly(True)

        self.horizontalLayout.addWidget(self.file_name)

        self.choose_file = QToolButton(MainWindow)
        self.choose_file.setObjectName(u"choose_file")

        self.horizontalLayout.addWidget(self.choose_file)

        self.label_6 = QLabel(MainWindow)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.method_name = QLineEdit(MainWindow)
        self.method_name.setObjectName(u"method_name")
        self.method_name.setFont(font)

        self.horizontalLayout.addWidget(self.method_name)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 4)
        self.horizontalLayout.setStretch(5, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(MainWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.tle_time = QLineEdit(MainWindow)
        self.tle_time.setObjectName(u"tle_time")
        self.tle_time.setFont(font)

        self.horizontalLayout_2.addWidget(self.tle_time)

        self.label_5 = QLabel(MainWindow)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_2.setStretch(3, 3)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(MainWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.args = QPlainTextEdit(MainWindow)
        self.args.setObjectName(u"args")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.args.sizePolicy().hasHeightForWidth())
        self.args.setSizePolicy(sizePolicy)
        self.args.setMinimumSize(QSize(100, 80))
        self.args.setMaximumSize(QSize(16777215, 80))
        self.args.setFont(font)

        self.verticalLayout_3.addWidget(self.args)

        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_7 = QLabel(MainWindow)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setBold(False)
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_7)

        self.jars = QPlainTextEdit(MainWindow)
        self.jars.setObjectName(u"jars")
        sizePolicy.setHeightForWidth(self.jars.sizePolicy().hasHeightForWidth())
        self.jars.setSizePolicy(sizePolicy)
        self.jars.setMinimumSize(QSize(100, 80))
        self.jars.setMaximumSize(QSize(16777215, 80))
        self.jars.setFont(font)

        self.verticalLayout_4.addWidget(self.jars)

        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.path = QLineEdit(MainWindow)
        self.path.setObjectName(u"path")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.path.sizePolicy().hasHeightForWidth())
        self.path.setSizePolicy(sizePolicy1)
        self.path.setMinimumSize(QSize(0, 20))
        self.path.setMaximumSize(QSize(16777215, 20))
        self.path.setFont(font)
        self.path.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.path)

        self.choose_path = QToolButton(MainWindow)
        self.choose_path.setObjectName(u"choose_path")

        self.horizontalLayout_6.addWidget(self.choose_path)

        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.verticalLayout_6.addLayout(self.verticalLayout_7)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(MainWindow)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)

        self.outputs = QTextBrowser(MainWindow)
        self.outputs.setObjectName(u"outputs")
        font2 = QFont()
        font2.setFamilies([u"Consolas"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.outputs.setFont(font2)
        self.outputs.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.outputs)

        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.start_button = QPushButton(MainWindow)
        self.start_button.setObjectName(u"start_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.start_button.sizePolicy().hasHeightForWidth())
        self.start_button.setSizePolicy(sizePolicy2)
        self.start_button.setFont(font)
        self.start_button.setLayoutDirection(Qt.LeftToRight)
        self.start_button.setAutoFillBackground(False)

        self.horizontalLayout_5.addWidget(self.start_button)

        self.end_button = QPushButton(MainWindow)
        self.end_button.setObjectName(u"end_button")
        sizePolicy2.setHeightForWidth(self.end_button.sizePolicy().hasHeightForWidth())
        self.end_button.setSizePolicy(sizePolicy2)
        self.end_button.setFont(font)

        self.horizontalLayout_5.addWidget(self.end_button)

        self.clear_button = QPushButton(MainWindow)
        self.clear_button.setObjectName(u"clear_button")
        sizePolicy2.setHeightForWidth(self.clear_button.sizePolicy().hasHeightForWidth())
        self.clear_button.setSizePolicy(sizePolicy2)
        self.clear_button.setFont(font)

        self.horizontalLayout_5.addWidget(self.clear_button)

        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.verticalLayout_6.setStretch(3, 4)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Evaluator", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u6570\u636e\u751f\u6210\u5668\uff08\u8bf7\u8fd4\u56delist\uff09",
                                                        None))
        self.file_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u540d", None))
        self.choose_file.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u".py", None))
        self.method_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u65b9\u6cd5\u540d", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u8bbe\u7f6eTLE\u65f6\u95f4\uff08\u9ed8\u8ba4\u65e0\u65f6\u9650\uff09",
                                                        None))
        self.tle_time.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TLE\u65f6\u95f4", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u79d2", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u6570\u636e\u751f\u6210\u6240\u9700\u53c2\u6570\uff08\u9ed8\u8ba4\u65e0\u53c2\u6570\uff09",
                                                        None))
        self.args.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u53c2\u6570", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u60f3\u6d4b\u8bd5\u7684jar\u5305", None))
        self.jars.setPlaceholderText(QCoreApplication.translate("MainWindow", u"jar\u5305", None))
        self.path.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"jar\u5305\u6240\u5728\u7684\u76ee\u5f55", None))
        self.choose_path.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u7a97\u53e3", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.end_button.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
    # retranslateUi
