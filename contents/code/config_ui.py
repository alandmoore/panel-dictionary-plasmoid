# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contents/ui/config.ui'
#
# Created: Mon Aug 24 13:06:28 2009
#      by: PyQt4 UI code generator 4.5.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(259, 245)
        self.backend_config_box = QtGui.QGroupBox(Form)
        self.backend_config_box.setGeometry(QtCore.QRect(1, 0, 261, 121))
        self.backend_config_box.setObjectName("backend_config_box")
        self.verticalLayoutWidget = QtGui.QWidget(self.backend_config_box)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 19, 241, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.python_dictclient_button = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.python_dictclient_button.setEnabled(False)
        self.python_dictclient_button.setObjectName("python_dictclient_button")
        self.verticalLayout_2.addWidget(self.python_dictclient_button)
        self.dict_client_button = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.dict_client_button.setEnabled(False)
        self.dict_client_button.setObjectName("dict_client_button")
        self.verticalLayout_2.addWidget(self.dict_client_button)
        self.dict_dataengine_button = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.dict_dataengine_button.setEnabled(False)
        self.dict_dataengine_button.setObjectName("dict_dataengine_button")
        self.verticalLayout_2.addWidget(self.dict_dataengine_button)
        self.server_config_box = QtGui.QGroupBox(Form)
        self.server_config_box.setGeometry(QtCore.QRect(10, 120, 241, 111))
        self.server_config_box.setObjectName("server_config_box")
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.server_config_box)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(-1, 20, 241, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.localhost_server_button = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.localhost_server_button.setObjectName("localhost_server_button")
        self.verticalLayout.addWidget(self.localhost_server_button)
        self.dict_org_server_button = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.dict_org_server_button.setObjectName("dict_org_server_button")
        self.verticalLayout.addWidget(self.dict_org_server_button)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.custom_server_button = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.custom_server_button.setObjectName("custom_server_button")
        self.horizontalLayout.addWidget(self.custom_server_button)
        self.serverUrlEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.serverUrlEdit.setEnabled(False)
        self.serverUrlEdit.setObjectName("serverUrlEdit")
        self.horizontalLayout.addWidget(self.serverUrlEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.custom_server_button, QtCore.SIGNAL("toggled(bool)"), self.serverUrlEdit.setEnabled)
        QtCore.QObject.connect(self.python_dictclient_button, QtCore.SIGNAL("toggled(bool)"), self.server_config_box.setVisible)
        QtCore.QObject.connect(self.dict_client_button, QtCore.SIGNAL("toggled(bool)"), self.server_config_box.setVisible)
        QtCore.QObject.connect(self.dict_dataengine_button, QtCore.SIGNAL("clicked(bool)"), self.server_config_box.setHidden)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.backend_config_box.setTitle(QtGui.QApplication.translate("Form", "Backend to Use", None, QtGui.QApplication.UnicodeUTF8))
        self.python_dictclient_button.setToolTip(QtGui.QApplication.translate("Form", "Use the Python dictclient library backend.  Requires the python-dictclient library.", None, QtGui.QApplication.UnicodeUTF8))
        self.python_dictclient_button.setText(QtGui.QApplication.translate("Form", "Python dictclient library", None, QtGui.QApplication.UnicodeUTF8))
        self.dict_client_button.setToolTip(QtGui.QApplication.translate("Form", "Use the \"dict\" command.  Requires that \"dict\" be installed.  See dict\'s man page for configuration instructions.", None, QtGui.QApplication.UnicodeUTF8))
        self.dict_client_button.setText(QtGui.QApplication.translate("Form", "Command line dict client", None, QtGui.QApplication.UnicodeUTF8))
        self.dict_dataengine_button.setToolTip(QtGui.QApplication.translate("Form", "Use the dict dataengine that ships with Plasma.  Unfortunately, it is quite limited at this time.  Not recommended.", None, QtGui.QApplication.UnicodeUTF8))
        self.dict_dataengine_button.setText(QtGui.QApplication.translate("Form", "Plasma dict dataengine", None, QtGui.QApplication.UnicodeUTF8))
        self.server_config_box.setTitle(QtGui.QApplication.translate("Form", "Server selection", None, QtGui.QApplication.UnicodeUTF8))
        self.localhost_server_button.setToolTip(QtGui.QApplication.translate("Form", "Consult a local computer (Requires you to run dictd or another DICT server on this computer)", None, QtGui.QApplication.UnicodeUTF8))
        self.localhost_server_button.setText(QtGui.QApplication.translate("Form", "localhost (this computer)", None, QtGui.QApplication.UnicodeUTF8))
        self.dict_org_server_button.setToolTip(QtGui.QApplication.translate("Form", "Use the DICT server at dict.org (requires internet connection)", None, QtGui.QApplication.UnicodeUTF8))
        self.dict_org_server_button.setText(QtGui.QApplication.translate("Form", "dict.org (internet)", None, QtGui.QApplication.UnicodeUTF8))
        self.custom_server_button.setToolTip(QtGui.QApplication.translate("Form", "Type in a custom hostname or IP address for a server running the DICT service.", None, QtGui.QApplication.UnicodeUTF8))
        self.custom_server_button.setText(QtGui.QApplication.translate("Form", "Custom", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

