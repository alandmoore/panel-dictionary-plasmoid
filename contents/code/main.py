# -*- coding: utf-8 -*-
# Panel Dictionary
# Copyright 2009 Alan D Moore
# Released under the terms of the GNU GPL v2 or later

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript
from PyKDE4 import kdeui
from PyQt4 import uic
from configureBackend import Dict_Backend_Config
from appearanceConfig import Appearance_Config
from matchWidget import Match_View_Widget
from definitionWidgetTabbed import Definition_View_Tabbed

import subprocess
import re
import threading

has_python_dictclient = True
try:
    import dictclient
except:
    has_python_dictclient = False



class PythonDictionary(plasmascript.Applet):
    def __init__(self,parent,args=None):
        plasmascript.Applet.__init__(self, parent)
        self.determine_capabilities()
        self.definition = []
        self.word = None
        self.engines = {}
        if self.has_engine:
            self.engines["dict-dataengine"] = self.define_via_dict_dataengine
        if self.has_dict_client:
            self.engines["dict-client"] = self.define_via_dict_client
        if self.has_python_dictclient:
            self.engines["python-dictclient"] = self.define_via_python_dict_client
        self.height = 60
        
    def init(self):
        #configuration
        self.setHasConfigurationInterface(True)
        #open config file
        configuration = self.config()
        #configurations settings
        self.chosen_engine = unicode(configuration.readEntry("engine", self.engines.keys()[-1]).toString())
        self.server = unicode(configuration.readEntry("server", "dict.org").toString())
        self.width = int(configuration.readEntry("width", "200").toString())
        self.text_color = unicode(configuration.readEntry("textColor", "#000000").toString())
        self.force_bw_definition = configuration.readEntry("force_bw_definition", False).toBool()

        #configure non-configurable settings
        self.setAspectRatioMode(Plasma.IgnoreAspectRatio)
        self.theme = Plasma.Svg(self)
        self.theme.setImagePath("widgets/background")
        self.setBackgroundHints(Plasma.Applet.DefaultBackground)

        self.layout = QGraphicsLinearLayout(Qt.Horizontal, self.applet)
        self.combobox = Plasma.ComboBox()
        self.combobox.nativeWidget().setEditable(True)
        self.combobox.setFocusPolicy(Qt.ClickFocus)
        self.combobox.nativeWidget().setContextMenuPolicy(Qt.NoContextMenu)
        self.update_text_color()

        self.lineEdit = self.combobox.nativeWidget().lineEdit()
        
        self.connect(self.combobox.nativeWidget(), SIGNAL("returnPressed()"), self.lookup_word)
        self.connect(self.combobox.nativeWidget(), SIGNAL("activated()"), self.focusWidget)
        self.lineEdit.installEventFilter(self)
        self.lineEdit.setFont(Plasma.Theme.defaultTheme().font(Plasma.Theme.DesktopFont))
        self.layout.addItem(self.combobox)
        self.setLayout(self.layout)
        self.set_combo_width(self.width)

##END INIT METHOD###

###FOCUS FIX###
# These methods fix the problem with getting a focus to the combobox
# when there are active windows open.
    def focusWidget(self):
        #adapted from Run Command Applet.
        # thanks Michal Dutkiewicz aka Emdek <emdeck@gmail.com>
        if self.scene():
            parentView = None
            possibleParentView = None
            for view in self.scene().views():
                if view.sceneRect().intersects(self.sceneBoundingRect()) or view.sceneRect().contains(self.scenePos()):
                    if view.isActiveWindow():
                        parentView = view
                        break
                    else:
                        possibleParentView = view
            if not parentView:
                parentView = possibleParentView
            if parentView:
                kdeui.KWindowSystem.forceActiveWindow(parentView.winId())
        self.raise_()
        self.combobox.nativeWidget().setFocus()
        QTimer.singleShot(250, self.combobox.nativeWidget(), SLOT("setFocus()"))
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.focusWidget()

    def eventFilter(self, myobject, event):
        if (event.type() ==QEvent.MouseButtonPress):
            self.focusWidget()
        return False

###END FOCUS FIX ###     
    def determine_capabilities(self):
    ## Check to see if python-dictclient is an option:
        self.has_python_dictclient = has_python_dictclient
    ## Check to see if there is a local instance of dict client:
        self.has_dict_client = (subprocess.call(["which", "dict"]) == 0)
    ## Use the engine as a last resort (no offense...)
        self.has_engine =  True
        
    def de_markup(self, text):
        regex = re.compile('<[^>]*>')
        return regex.sub('', text).strip().replace("\r", "\n")

    def ping(self):
        KMessageBox.information(None, "ping", "ping")
###WORD LOOKUP METHODS###

    def lookup_word(self, word=None):
        if word is None:
            self.word = unicode(self.combobox.text())
        else:
            self.word = word
        self.combobox.nativeWidget().setCurrentItem("")
        #TODO: timeout this next call
        self.engines[self.chosen_engine]()
               

        
    ###show the messagebox
    def show_definitions(self, match=False):
        dialog_data = {}
        if len(self.definition) > 0:
            dialog_data["is_match"] = match
            dialog_data["summary"] = self.definition[0]
            dialog_data["definition"] = self.definition[1:]
            dialog_data["title"] = "Definition of %s" % self.word
            self.definition_dialog(dialog_data)
            self.definition = []
        else:
            kdeui.KMessageBox.information(self.combobox.nativeWidget(), "There was some kind of weird problem, you shouldn't be seeing this.  Please report to the author.", "Definition of %s" % self.word)

    def definition_dialog(self, data):
        self.def_dialog = kdeui.KDialog()
        self.def_dialog.force_bw_definition = self.force_bw_definition
        self.def_dialog.setWindowTitle(data["title"])
        if not data["is_match"]:
            self.def_widget = Definition_View_Tabbed(self.def_dialog, data)
        else:
            self.def_widget = Match_View_Widget(self, data)
        self.def_dialog.setButtons(kdeui.KDialog.ButtonCode(kdeui.KDialog.Close))
        self.def_dialog.setMainWidget(self.def_widget)
        self.def_dialog.show()

    def define_via_dict_client(self):
        #code for using the CLI dict command
        is_match = False
        if self.word.isalnum():
            command = "dict -f"
            if self.server is not None:
                command += " -h %s" % self.server
            command += " %s" % self.word
        
            defs = subprocess.Popen([command], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            defs = list(defs.stdout) + list(defs.stderr)
            #Reformat that rather ungainly dict output into distinct definitions
            #Unicode fix here and a few lines down from kozakmamay; thanks!
            self.definition = [unicode(defs.pop(0), "utf-8")] #the first line is the summary
            is_match = re.search('perhaps you mean', self.definition[0]) is not None
            if not is_match:
                a_def = ""
                while defs:
                    line = unicode(defs.pop(0), "utf-8")
                    if not re.match("  ", line):
                        if a_def: #if it's not empty, add the current defintion to the list
                            self.definition.append(a_def)
                        a_def = line.split("\t")[-1]
                    else: #two leading spaces indicate a definition line
                        a_def += line
                self.definition.append(a_def) #get the last line.  Yeah, this is ugly.

            else: #if it's a match
                while defs:
                    self.definition.append(defs.pop(0).split("\t")[-1].strip()) 
        else:
            self.definition = ["Invalid Word."]


        self.show_definitions(is_match)

    def define_via_python_dict_client(self):
        #code for using the python-dictclient library
        conn = dictclient.Connection(self.server)
        defs = conn.define("*", self.word)
        num_defs = len(defs)
        is_match = False
        if (num_defs==0):
            #no defs, matching
            defs = conn.match("*","soundex", self.word)
            defs = ["%s\n" % x.getword()  for x in defs]
            perhaps = ", perhaps you mean:"
            is_match =True
        else:
            defs = ["%s:\n\n%s\n" % (x.getdb().getdescription() ,x.getdefstr()) for x in defs]
            perhaps = "."
            #Prepare the output
        s = (num_defs !=1) and "s" or ""
        self.definition.append("%d definition%s found%s\n"%(num_defs, s, perhaps))

        self.definition += defs
        self.show_definitions(is_match)
        
    def define_via_dict_dataengine(self):
        #code for using the plasma dataengine (currently broken)
        self.dict_engine = self.dataEngine("dict")
        mydef = self.dict_engine.connectSource(QString(self.word), self)
        #Once connectSource is called, dataUpdated() will do the rest...

    @pyqtSignature("dataUpdated(const QString &, const Plasma::DataEngine::Data &)")
    def dataUpdated(self, sourceName, data):
        """
        This implementation bears some explanation.  When we call connectSource() in define_via_dict_dataengine(),
        the dataengine will immediately call dataUpdated() with bad data: our word as a source, and an empty set for results.
        Once it actually hears back from the server, we'll get back a single definition with markup, OR and empty set of markup tags if
        no definition was found.  Ugh.

        So, first we filter for no definitions, and do nothing if there are none.  Then, if we get one, we remove the tags and see if there's
        anything left.  If not, we tell the user there was no definition found.  Otherwise, we print the tag-stripped definition (since I don't
        know how to get the KMessageBox.informationList to use the tags).

        If there's a better way to implement this, I'm open to suggestion...
        """
        if sourceName == self.word:
            num_defs = len(data)
            s = (num_defs != 1) and "s" or ""
            self.definition = ["%d definition%s found.\n" % (num_defs, s)]
            if num_defs > 0:
                text = self.de_markup(unicode(data[QString("text")].toString()))
                if text != "":
                    self.definition += ["WordNet"]
                    self.definition += [text]
                else:
                    self.definition = ["No definitions found."]
                self.show_definitions()


### CONFIGURATION RELATED CODE ########
    def createConfigurationInterface(self, parent):
        ##The dictionary backend configuration
        self.backend_config = Dict_Backend_Config(self)
        p = parent.addPage(self.backend_config, "Backend")
        p.setIcon(kdeui.KIcon("accessories-dictionary"))
        ##The appearance configuration part
        self.appearance_config = Appearance_Config(self)
        p2 = parent.addPage(self.appearance_config, "Appearance")
        p2.setIcon(kdeui.KIcon("preferences-desktop-color"))
        ##Final bits
        self.connect(parent, SIGNAL("okClicked()"), self.configAccepted)
        self.connect(parent, SIGNAL("cancelClicked()"), self.configDenied)
        
    def showConfigurationInterface(self):
        self.dialog = kdeui.KPageDialog()
        self.dialog.setFaceType(kdeui.KPageDialog.List)
        self.dialog.setButtons(kdeui.KDialog.ButtonCode(kdeui.KDialog.Ok | kdeui.KDialog.Cancel))
        self.createConfigurationInterface(self.dialog)
        self.dialog.resize(640,480)
        self.dialog.show()

    def configDenied(self):
        configuration = self.config()
        self.width = int(configuration.readEntry("width", "200").toString())
        self.set_combo_width(self.width)

    def configAccepted(self):
        self.chosen_engine = self.backend_config.get_backend()
        self.server = self.backend_config.get_server_url()
        self.text_color = self.appearance_config.get_text_color()
        self.update_text_color()
        self.width = self.appearance_config.get_width()
        self.set_combo_width(self.width)
        self.force_bw_definition = self.appearance_config.get_force_bw_defs()

        configuration = self.config()
        configuration.writeEntry("engine", QVariant(self.chosen_engine))
        configuration.writeEntry("server", QVariant(self.server))
        configuration.writeEntry("width", QVariant(self.width))
        configuration.writeEntry("textColor", QVariant(self.text_color))
        configuration.writeEntry("force_bw_definition", QVariant(self.force_bw_definition))

        ##appearance related
    def set_combo_width(self, width):
        if self.containment().containmentType() == Plasma.Containment.PanelContainment:
            self.combobox.nativeWidget().setMinimumWidth(width)
            self.boundingRect().setWidth(width)
        else:
            self.resize(width, self.height)
            self.combobox.nativeWidget().setMinimumWidth(width-40)

    def update_text_color(self):
        self.combobox.setStyleSheet("color: %s;"% self.text_color)


###END CLASS DEFINITION###        

def CreateApplet(parent):
        return PythonDictionary(parent)
