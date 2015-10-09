# -*- coding: utf-8 -*-
"""
/***************************************************************************
 polygonsplitter
                                 Polygon Splitter plugin
 Split polygons into equal area parts
                              -------------------
        begin                : 2013-03-07
        copyright            : (C) 2013 by ViaMap Ltd.
        email                : info@viamap.hu
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from polygonsplitterdialog import polygonsplitterDialog
from split_poly import EqSplitPolygon

# Use pdb for debugging
import pdb

class polygonsplitter:

    def __init__(self, iface):
        self.iface = iface

        # Create the dialog (after translation) and keep reference
        self.dlg = polygonsplitterDialog()

    def initGui(self):
        # Create action that will start plugin configuration
        # These lines allow you to set a breakpoint in the app
        myQrcPath = ":polygonsplitter.png"
        myIcon=QIcon(myQrcPath)
        self.action = QAction(
            myIcon,
            u"Polygon Splitter", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Polygon Splitter", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Polygon Splitter", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code)
            if self.dlg.ui.horizontalCut.isChecked():
                method="v"
            elif self.dlg.ui.verticalCut.isChecked():
                method="h"
            else:
                method="a"
            eqsplit_inst = EqSplitPolygon()
            eqsplit_inst.splitSelected(self.dlg.ui.targetArea.value(),self.dlg.ui.granulFactor.value(),method,self.dlg.ui.equalParts.isChecked())
