from PyQt4.QtGui import *
from PyQt4.QtCore import *
from appearanceConfig_ui import Ui_Form

class Appearance_Config(QWidget, Ui_Form):
    def __init__(self, parent, defaultConfig = None):
        QWidget.__init__(self)
        self.parent = parent
        self.setupUi(self)
        self.width_slider.setValue(parent.combobox.nativeWidget().width())
        self.text_colorcombo.setColor(QColor(parent.text_color))
        self.force_bw_definition_box.setChecked(parent.force_bw_definition)
        self.connect(self.width_slider, SIGNAL("valueChanged(int)"), parent.set_combo_width)

    def get_width(self):
        return self.width_slider.value()

    def get_text_color(self):
        return self.text_colorcombo.color().name()
    def get_force_bw_defs(self):
        return self.force_bw_definition_box.isChecked()
