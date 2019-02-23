# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bid.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_autoBid(object):
    def setupUi(self, autoBid):
        autoBid.setObjectName(_fromUtf8("autoBid"))
        autoBid.setEnabled(True)
        # autoBid.resize(265, 500)
        autoBid.resize(295, 530)
        autoBid.setMinimumSize(QtCore.QSize(295, 530))
        autoBid.setMaximumSize(QtCore.QSize(295, 530))
        self.verticalLayout_2 = QtGui.QVBoxLayout(autoBid)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, 10, 10, 30)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.timeLabel = QtGui.QLabel(autoBid)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.timeLabel.setFont(font)
        self.timeLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLabel.setObjectName(_fromUtf8("timeLabel"))
        self.verticalLayout.addWidget(self.timeLabel)
        self.winStatLabel = QtGui.QLabel(autoBid)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.winStatLabel.setFont(font)
        self.winStatLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.winStatLabel.setWordWrap(True)
        self.winStatLabel.setObjectName(_fromUtf8("winStatLabel"))
        self.verticalLayout.addWidget(self.winStatLabel)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.splitter_3 = QtGui.QSplitter(autoBid)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.getWindowBtn = QtGui.QPushButton(self.splitter_3)
        self.getWindowBtn.setObjectName(_fromUtf8("getWindowBtn"))
        self.getCapBtn = QtGui.QPushButton(self.splitter_3)
        self.getCapBtn.setObjectName(_fromUtf8("getCapBtn"))
        self.aboutBtn = QtGui.QPushButton(self.splitter_3)
        self.aboutBtn.setObjectName(_fromUtf8("aboutBtn"))
        self.verticalLayout_2.addWidget(self.splitter_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setMargin(10)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.splitter = QtGui.QSplitter(autoBid)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.btn500 = QtGui.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn500.setFont(font)
        self.btn500.setCheckable(False)
        self.btn500.setObjectName(_fromUtf8("btn500"))
        self.btn700 = QtGui.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn700.setFont(font)
        self.btn700.setObjectName(_fromUtf8("btn700"))
        self.btn900 = QtGui.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn900.setFont(font)
        self.btn900.setObjectName(_fromUtf8("btn900"))
        self.horizontalLayout.addWidget(self.splitter)
        self.splitter_2 = QtGui.QSplitter(autoBid)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.btn600 = QtGui.QPushButton(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn600.setFont(font)
        self.btn600.setObjectName(_fromUtf8("btn600"))
        self.btn800 = QtGui.QPushButton(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn800.setFont(font)
        self.btn800.setObjectName(_fromUtf8("btn800"))
        self.btn1000 = QtGui.QPushButton(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn1000.setFont(font)
        self.btn1000.setObjectName(_fromUtf8("btn1000"))
        self.horizontalLayout.addWidget(self.splitter_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.btnAid = QtGui.QPushButton(autoBid)
        self.btnAid.setObjectName(_fromUtf8("btnAid"))
        self.verticalLayout_2.addWidget(self.btnAid)

        self.retranslateUi(autoBid)
        QtCore.QMetaObject.connectSlotsByName(autoBid)
        autoBid.setTabOrder(self.btnAid, self.btn600)
        autoBid.setTabOrder(self.btn600, self.btn700)
        autoBid.setTabOrder(self.btn700, self.getWindowBtn)
        autoBid.setTabOrder(self.getWindowBtn, self.getCapBtn)
        autoBid.setTabOrder(self.getCapBtn, self.btn900)
        autoBid.setTabOrder(self.btn900, self.aboutBtn)
        autoBid.setTabOrder(self.aboutBtn, self.btn800)
        autoBid.setTabOrder(self.btn800, self.btn500)
        autoBid.setTabOrder(self.btn500, self.btn1000)

    def retranslateUi(self, autoBid):
        autoBid.setWindowTitle(_translate("autoBid", "AutoBid for 201701 -- By Luke", None))
        self.timeLabel.setText(_translate("autoBid", "10:00:01", None))
        self.winStatLabel.setText(_translate("autoBid", "未识别", None))
        self.getWindowBtn.setText(_translate("autoBid", "获取窗口", None))
        self.getCapBtn.setText(_translate("autoBid", "自动截图", None))
        self.aboutBtn.setText(_translate("autoBid", "关于", None))
        self.btn500.setText(_translate("autoBid", "+500", None))
        self.btn700.setText(_translate("autoBid", "+700", None))
        self.btn900.setText(_translate("autoBid", "+900", None))
        self.btn600.setText(_translate("autoBid", "+600", None))
        self.btn800.setText(_translate("autoBid", "+800", None))
        self.btn1000.setText(_translate("autoBid", "+1000", None))
        self.btnAid.setText(_translate("autoBid", "自动加400提交(最后补救用)", None))

