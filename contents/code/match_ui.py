# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contents/ui/definition.ui'
#
# Created: Fri Aug 21 23:41:13 2009
#      by: PyQt4 UI code generator 4.5.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Definition(object):
    def setupUi(self, Definition):
        Definition.setObjectName("Definition")
        Definition.resize(640, 480)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Definition.sizePolicy().hasHeightForWidth())
        Definition.setSizePolicy(sizePolicy)
        Definition.setMinimumSize(QtCore.QSize(640, 480))
        self.verticalLayoutWidget = QtGui.QWidget(Definition)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 9, 621, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.summary_label = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.summary_label.sizePolicy().hasHeightForWidth())
        self.summary_label.setSizePolicy(sizePolicy)
        self.summary_label.setObjectName("summary_label")
        self.verticalLayout.addWidget(self.summary_label)
        self.definition_list = QtGui.QListWidget(self.verticalLayoutWidget)
        self.definition_list.setObjectName("definition_list")
        self.verticalLayout.addWidget(self.definition_list)

        self.retranslateUi(Definition)
        QtCore.QMetaObject.connectSlotsByName(Definition)

    def retranslateUi(self, Definition):
        Definition.setWindowTitle(QtGui.QApplication.translate("Definition", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.summary_label.setText(QtGui.QApplication.translate("Definition", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Definition = QtGui.QWidget()
    ui = Ui_Definition()
    ui.setupUi(Definition)
    Definition.show()
    sys.exit(app.exec_())

