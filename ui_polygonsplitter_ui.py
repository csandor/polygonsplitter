# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/data/dev/viamap/polygonsplitter/ui_polygonsplitter.ui'
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

class Ui_polygonsplitter(object):
    def setupUi(self, polygonsplitter):
        polygonsplitter.setObjectName(_fromUtf8("polygonsplitter"))
        polygonsplitter.setWindowModality(QtCore.Qt.ApplicationModal)
        polygonsplitter.resize(304, 338)
        self.buttonBox = QtGui.QDialogButtonBox(polygonsplitter)
        self.buttonBox.setGeometry(QtCore.QRect(130, 300, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(polygonsplitter)
        self.label.setGeometry(QtCore.QRect(140, 20, 151, 21))
        self.label.setToolTip(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(polygonsplitter)
        self.label_2.setGeometry(QtCore.QRect(140, 50, 141, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.groupBox = QtGui.QGroupBox(polygonsplitter)
        self.groupBox.setGeometry(QtCore.QRect(30, 90, 271, 81))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.layoutWidget = QtGui.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 241, 61))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.targetAreaParts = QtGui.QRadioButton(self.layoutWidget)
        self.targetAreaParts.setChecked(True)
        self.targetAreaParts.setObjectName(_fromUtf8("targetAreaParts"))
        self.verticalLayout_2.addWidget(self.targetAreaParts)
        self.equalParts = QtGui.QRadioButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equalParts.sizePolicy().hasHeightForWidth())
        self.equalParts.setSizePolicy(sizePolicy)
        self.equalParts.setObjectName(_fromUtf8("equalParts"))
        self.verticalLayout_2.addWidget(self.equalParts)
        self.granulFactor = QtGui.QSpinBox(polygonsplitter)
        self.granulFactor.setGeometry(QtCore.QRect(30, 50, 91, 22))
        self.granulFactor.setMinimum(5)
        self.granulFactor.setMaximum(10)
        self.granulFactor.setObjectName(_fromUtf8("granulFactor"))
        self.targetArea = QtGui.QDoubleSpinBox(polygonsplitter)
        self.targetArea.setGeometry(QtCore.QRect(30, 20, 91, 22))
        self.targetArea.setDecimals(3)
        self.targetArea.setMinimum(0.001)
        self.targetArea.setMaximum(1e+15)
        self.targetArea.setProperty("value", 2.0)
        self.targetArea.setObjectName(_fromUtf8("targetArea"))
        self.groupBox_2 = QtGui.QGroupBox(polygonsplitter)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 180, 271, 111))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.layoutWidget1 = QtGui.QWidget(self.groupBox_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 20, 241, 74))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalCut = QtGui.QRadioButton(self.layoutWidget1)
        self.verticalCut.setObjectName(_fromUtf8("verticalCut"))
        self.verticalLayout.addWidget(self.verticalCut)
        self.horizontalCut = QtGui.QRadioButton(self.layoutWidget1)
        self.horizontalCut.setObjectName(_fromUtf8("horizontalCut"))
        self.verticalLayout.addWidget(self.horizontalCut)
        self.alternatingCut = QtGui.QRadioButton(self.layoutWidget1)
        self.alternatingCut.setChecked(True)
        self.alternatingCut.setObjectName(_fromUtf8("alternatingCut"))
        self.verticalLayout.addWidget(self.alternatingCut)
        self.groupBox_2.raise_()
        self.buttonBox.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.groupBox.raise_()
        self.granulFactor.raise_()
        self.targetArea.raise_()

        self.retranslateUi(polygonsplitter)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), polygonsplitter.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), polygonsplitter.reject)
        QtCore.QMetaObject.connectSlotsByName(polygonsplitter)

    def retranslateUi(self, polygonsplitter):
        polygonsplitter.setWindowTitle(_translate("polygonsplitter", "Split polygons into equal area parts", None))
        self.label.setText(_translate("polygonsplitter", "Target area in layer units", None))
        self.label_2.setText(_translate("polygonsplitter", "Granularity factor (5-10)", None))
        self.groupBox.setTitle(_translate("polygonsplitter", "Recalculate target area?", None))
        self.targetAreaParts.setToolTip(_translate("polygonsplitter", "The target area will be kept exactly as entered", None))
        self.targetAreaParts.setText(_translate("polygonsplitter", "Target area exactly as entered", None))
        self.equalParts.setToolTip(_translate("polygonsplitter", "Target area is recalculated by rounding the polygon area / target area and dividing the polygon area by this ratio to produce more even parts.", None))
        self.equalParts.setText(_translate("polygonsplitter", "Try to make more equal parts", None))
        self.granulFactor.setToolTip(_translate("polygonsplitter", "Multiplier of original polygon area / target area to get iteration steps (recommended value is between 5 and 10)", None))
        self.targetArea.setToolTip(_translate("polygonsplitter", "Target area of polygon parts", None))
        self.groupBox_2.setTitle(_translate("polygonsplitter", "Direction of cut", None))
        self.verticalCut.setText(_translate("polygonsplitter", "Vertical cutting", None))
        self.horizontalCut.setText(_translate("polygonsplitter", "Horizontal cutting", None))
        self.alternatingCut.setText(_translate("polygonsplitter", "Alternating vertical/horizontal", None))

