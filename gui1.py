# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(607, 790)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.file_list_widget = QtWidgets.QListWidget(self.centralwidget)
        self.file_list_widget.setGeometry(QtCore.QRect(40, 60, 531, 181))
        self.file_list_widget.setObjectName("file_list_widget")
        self.select_dir_btn = QtWidgets.QPushButton(self.centralwidget)
        self.select_dir_btn.setGeometry(QtCore.QRect(40, 20, 101, 31))
        self.select_dir_btn.setObjectName("select_dir_btn")
        self.old_word_lbl = QtWidgets.QLabel(self.centralwidget)
        self.old_word_lbl.setGeometry(QtCore.QRect(10, 300, 201, 31))
        self.old_word_lbl.setObjectName("old_word_lbl")
        self.new_word_ldl = QtWidgets.QLabel(self.centralwidget)
        self.new_word_ldl.setGeometry(QtCore.QRect(10, 340, 191, 31))
        self.new_word_ldl.setObjectName("new_word_ldl")
        self.old_word_Qtext = QtWidgets.QTextEdit(self.centralwidget)
        self.old_word_Qtext.setGeometry(QtCore.QRect(210, 300, 361, 31))
        self.old_word_Qtext.setObjectName("old_word_Qtext")
        self.new_word_Qtext = QtWidgets.QTextEdit(self.centralwidget)
        self.new_word_Qtext.setGeometry(QtCore.QRect(210, 340, 361, 31))
        self.new_word_Qtext.setObjectName("new_word_Qtext")
        self.run_btn = QtWidgets.QPushButton(self.centralwidget)
        self.run_btn.setGeometry(QtCore.QRect(210, 390, 361, 31))
        self.run_btn.setObjectName("run_btn")
        self.changes_Qlist = QtWidgets.QListWidget(self.centralwidget)
        self.changes_Qlist.setGeometry(QtCore.QRect(20, 460, 561, 271))
        self.changes_Qlist.setObjectName("changes_Qlist")
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setGeometry(QtCore.QRect(30, 390, 141, 31))
        self.clear_btn.setObjectName("clear_btn")
        self.check_if_file_exist_btn = QtWidgets.QPushButton(self.centralwidget)
        self.check_if_file_exist_btn.setGeometry(QtCore.QRect(40, 250, 161, 31))
        self.check_if_file_exist_btn.setObjectName("check_if_file_exist_btn")
        self.select_files_btn = QtWidgets.QPushButton(self.centralwidget)
        self.select_files_btn.setGeometry(QtCore.QRect(150, 20, 81, 31))
        self.select_files_btn.setObjectName("select_files_btn")
        self.file_type_Qtext = QtWidgets.QTextEdit(self.centralwidget)
        self.file_type_Qtext.setGeometry(QtCore.QRect(440, 20, 131, 31))
        self.file_type_Qtext.setObjectName("file_type_Qtext")
        self.file_type_lbl = QtWidgets.QLabel(self.centralwidget)
        self.file_type_lbl.setGeometry(QtCore.QRect(320, 20, 111, 31))
        self.file_type_lbl.setObjectName("file_type_lbl")
        self.prfix_Qtext = QtWidgets.QTextEdit(self.centralwidget)
        self.prfix_Qtext.setGeometry(QtCore.QRect(220, 250, 351, 31))
        self.prfix_Qtext.setObjectName("prfix_Qtext")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 607, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.select_dir_btn.setText(_translate("MainWindow", "select directory"))
        self.old_word_lbl.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff0000;\">old word (word to replace)</span></p><p align=\"center\"><span style=\" font-size:12pt; color:#ff0000;\"><br/></span></p></body></html>"))
        self.new_word_ldl.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#005500;\">new word (word to insert)</span></p></body></html>"))
        self.run_btn.setText(_translate("MainWindow", "run"))
        self.clear_btn.setText(_translate("MainWindow", "clear"))
        self.check_if_file_exist_btn.setText(_translate("MainWindow", "check if files exist in prefix"))
        self.select_files_btn.setText(_translate("MainWindow", "select files"))
        self.file_type_lbl.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">chose file type:</span></p></body></html>"))
        self.prfix_Qtext.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">prefix here</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
