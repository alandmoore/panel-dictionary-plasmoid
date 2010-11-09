zip -r ../panel-dictionary.plasmoid .
plasmapkg -r panel-dictionary
plasmapkg -i ../panel-dictionary.plasmoid

sleep 4 
plasmoidviewer panel-dictionary
