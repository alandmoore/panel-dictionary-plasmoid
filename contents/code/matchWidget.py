from PyQt4.QtGui import *
from PyQt4.QtCore import *
from match_ui import Ui_Definition

class Match_View_Widget(QWidget, Ui_Definition):
    def __init__(self, parent, data):
        QWidget.__init__(self)
        self.parent = parent
        self.setupUi(self)
        self.setWindowTitle(data["title"])
        self.summary_label.setText(data["summary"])
        #for line in data["definition"]:
         #   self.definition_list.addItem(line)
        self.definition_list.addItems(data["definition"])
        self.definition_list.adjustSize()
        self.connect(self.definition_list, SIGNAL("itemDoubleClicked(QListWidgetItem*)"), self.define_match)

    def define_match(self, list_widget_item):
        self.parent.combobox.nativeWidget().lineEdit().setText(list_widget_item.text())
        self.parent.def_dialog.close()
        QTimer.singleShot(200, self.parent.lookup_word)
        
