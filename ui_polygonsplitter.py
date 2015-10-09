# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_polygonsplitter.ui'
#
# Created: Fri Mar 08 09:13:41 2013
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_polygonsplitter(object):
    def setupUi(self, polygonsplitter):
        polygonsplitter.setObjectName(_fromUtf8("polygonsplitter"))
        polygonsplitter.setWindowModality(QtCore.Qt.ApplicationModal)
        polygonsplitter.resize(276, 360)
        self.buttonBox = QtGui.QDialogButtonBox(polygonsplitter)
        self.buttonBox.setGeometry(QtCore.QRect(50, 310, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(polygonsplitter)
        self.label.setGeometry(QtCore.QRect(140, 20, 131, 21))
        self.label.setToolTip(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(polygonsplitter)
        self.label_2.setGeometry(QtCore.QRect(140, 50, 131, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.groupBox = QtGui.QGroupBox(polygonsplitter)
        self.groupBox.setGeometry(QtCore.QRect(30, 90, 191, 81))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.equalParts = QtGui.QRadioButton(self.groupBox)
        self.equalParts.setGeometry(QtCore.QRect(20, 30, 171, 17))
        self.equalParts.setObjectName(_fromUtf8("equalParts"))
        self.targetAreaParts = QtGui.QRadioButton(self.groupBox)
        self.targetAreaParts.setGeometry(QtCore.QRect(20, 50, 171, 17))
        self.targetAreaParts.setChecked(True)
        self.targetAreaParts.setObjectName(_fromUtf8("targetAreaParts"))
        self.granulFactor = QtGui.QSpinBox(polygonsplitter)
        self.granulFactor.setGeometry(QtCore.QRect(30, 50, 91, 22))
        self.granulFactor.setMinimum(5)
        self.granulFactor.setMaximum(20)
        self.granulFactor.setObjectName(_fromUtf8("granulFactor"))
        self.targetArea = QtGui.QDoubleSpinBox(polygonsplitter)
        self.targetArea.setGeometry(QtCore.QRect(30, 20, 91, 22))
        self.targetArea.setDecimals(3)
        self.targetArea.setMinimum(0.001)
        self.targetArea.setMaximum(1e+15)
        self.targetArea.setProperty(_fromUtf8("value"), 2.0)
        self.targetArea.setObjectName(_fromUtf8("targetArea"))
        self.groupBox_2 = QtGui.QGroupBox(polygonsplitter)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 180, 191, 111))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalCut = QtGui.QRadioButton(self.groupBox_2)
        self.verticalCut.setGeometry(QtCore.QRect(20, 20, 121, 17))
        self.verticalCut.setObjectName(_fromUtf8("verticalCut"))
        self.horizontalCut = QtGui.QRadioButton(self.groupBox_2)
        self.horizontalCut.setGeometry(QtCore.QRect(20, 50, 131, 17))
        self.horizontalCut.setObjectName(_fromUtf8("horizontalCut"))
        self.alternatingCut = QtGui.QRadioButton(self.groupBox_2)
        self.alternatingCut.setGeometry(QtCore.QRect(20, 80, 161, 17))
        self.alternatingCut.setChecked(True)
        self.alternatingCut.setObjectName(_fromUtf8("alternatingCut"))

        self.retranslateUi(polygonsplitter)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), polygonsplitter.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), polygonsplitter.reject)
        QtCore.QMetaObject.connectSlotsByName(polygonsplitter)

    def retranslateUi(self, polygonsplitter):
        polygonsplitter.setWindowTitle(QtGui.QApplication.translate("polygonsplitter", "Split polygons into equal area parts", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("polygonsplitter", "Target area in layer units", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("polygonsplitter", "Granularity factor 5-10", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("polygonsplitter", "Recalculate target area?", None, QtGui.QApplication.UnicodeUTF8))
        self.equalParts.setToolTip(QtGui.QApplication.translate("polygonsplitter", "Target area is recalculated by rounding the polygon area / target area and dividing the polygon area by this ratio to produce more even parts.", None, QtGui.QApplication.UnicodeUTF8))
        self.equalParts.setText(QtGui.QApplication.translate("polygonsplitter", "Try to make more equal parts", None, QtGui.QApplication.UnicodeUTF8))
        self.targetAreaParts.setToolTip(QtGui.QApplication.translate("polygonsplitter", "The target area will be kept exactly as entered", None, QtGui.QApplication.UnicodeUTF8))
        self.targetAreaParts.setText(QtGui.QApplication.translate("polygonsplitter", "Target area exactly as entered", None, QtGui.QApplication.UnicodeUTF8))
        self.granulFactor.setToolTip(QtGui.QApplication.translate("polygonsplitter", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Multiplier of original polygon area / target area to get iteration steps<br />(recommended value is between 5 and10)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.targetArea.setToolTip(QtGui.QApplication.translate("polygonsplitter", "Target area of polygon parts", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("polygonsplitter", "Direction of cut", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalCut.setText(QtGui.QApplication.translate("polygonsplitter", "Vertical cutting", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalCut.setText(QtGui.QApplication.translate("polygonsplitter", "Horizontal cutting", None, QtGui.QApplication.UnicodeUTF8))
        self.alternatingCut.setText(QtGui.QApplication.translate("polygonsplitter", "Alternating vert/horiz", None, QtGui.QApplication.UnicodeUTF8))

