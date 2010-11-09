from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyKDE4.kdeui import KTextEdit
from definition_tabbed_ui import Ui_Definition

class Definition_View_Tabbed(QWidget, Ui_Definition):
    def __init__(self, parent, data):
        QWidget.__init__(self)
        self.parent = parent
        self.setupUi(self)
        self.setWindowTitle(data["title"])
        self.summary_label.setText(data["summary"])
        for line in data["definition"]:
            index = data["definition"].index(line) + 1
            self.add_definition(line, index)
        
        self.definition_tabs.adjustSize()

    def add_definition(self, text, number):
        dictionary = text.split("\n")[0]
        definitions = text.split("\n")[1:]
        page = KTextEdit("<br>".join(definitions), self)
        page.setReadOnly(True)
        page.setAutoFormatting(QTextEdit.AutoBulletList)
        page.setFontWeight(QFont.Normal)
        if self.parent.force_bw_definition:
            page.setStyleSheet(QString("background-color: white; color:black;"))
        self.definition_tabs.addTab(page, "%s: %s" %(number, dictionary))
