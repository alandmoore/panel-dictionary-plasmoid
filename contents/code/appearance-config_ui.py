# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contents/ui/appearance-config.ui'
#
# Created: Mon Aug 24 22:00:16 2009
#      by: PyQt4 UI code generator 4.5.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 361, 88))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.width_slider = QtGui.QSlider(self.verticalLayoutWidget)
        self.width_slider.setMaximum(200)
        self.width_slider.setOrientation(QtCore.Qt.Horizontal)
        self.width_slider.setObjectName("width_slider")
        self.horizontalLayout.addWidget(self.width_slider)
        self.width_spinbox = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.width_spinbox.setMaximum(200)
        self.width_spinbox.setObjectName("width_spinbox")
        self.horizontalLayout.addWidget(self.width_spinbox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.text_colorcombo = KColorCombo(self.verticalLayoutWidget)
        self.text_colorcombo.setObjectName("text_colorcombo")
        self.horizontalLayout_2.addWidget(self.text_colorcombo)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label.setBuddy(self.width_spinbox)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.width_slider, QtCore.SIGNAL("valueChanged(int)"), self.width_spinbox.setValue)
        QtCore.QObject.connect(self.width_spinbox, QtCore.SIGNAL("valueChanged(int)"), self.width_slider.setValue)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Text Color", None, QtGui.QApplication.UnicodeUTF8))

from PyKDE4.kdeui import KColorCombo

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

