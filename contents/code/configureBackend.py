from PyQt4.QtGui import QWidget
from PyQt4.QtCore import QString
from config_ui import Ui_Form

class Dict_Backend_Config(QWidget, Ui_Form):
    def __init__(self, parent, defaultConfig = None):
        QWidget.__init__(self)
        self.parent = parent
        self.setupUi(self)
        #This mess probably needs to be recoded more elegantly
        if parent.has_engine:
            self.dict_dataengine_button.setEnabled(True)
            if parent.chosen_engine == "dict-dataengine":
                self.dict_dataengine_button.click()
        if parent.has_dict_client:
            self.dict_client_button.setEnabled(True)
            if parent.chosen_engine == "dict-client":
                self.dict_client_button.click()
        if parent.has_python_dictclient:
            #This is the most preferred, so it's last and will therefore
            #end up being selected by default if available
            self.python_dictclient_button.setEnabled(True)
            if parent.chosen_engine == "python-dictclient":
                self.python_dictclient_button.click()

        ## Now, with great inelegance, set the server radio button
        if parent.server == "localhost":
            self.localhost_server_button.click()
        elif parent.server == "dict.org" or parent.server == "":
            self.dict_org_server_button.click()
        else:
            self.custom_server_button.click()
            self.serverUrlEdit.setText(parent.server)        

        
    def get_backend(self):
        if self.python_dictclient_button.isChecked():
            return "python-dictclient"
        if self.dict_client_button.isChecked():
            return "dict-client"
        if self.dict_dataengine_button.isChecked():
            return "dict-dataengine"

    def get_server_url(self):
        if self.localhost_server_button.isChecked():
            return "localhost"
        elif self.dict_org_server_button.isChecked():
            return "dict.org"
        elif self.custom_server_button.isChecked():
            return unicode(self.serverUrlEdit.text())
