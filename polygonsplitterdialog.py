# -*- coding: utf-8 -*-
"""
/***************************************************************************
 polygonsplitterDialog
                                 A QGIS plugin
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

from PyQt4 import QtCore, QtGui
from ui_polygonsplitter import Ui_polygonsplitter
# create the dialog for zoom to point


class polygonsplitterDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_polygonsplitter()
        self.ui.setupUi(self)
