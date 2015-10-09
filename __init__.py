# -*- coding: utf-8 -*-
"""
/***************************************************************************
 polygonsplitter
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
 This script initializes the plugin, making it known to QGIS.
"""


def name():
    return "Polygon Splitter"


def description():
    return "Split polygons into equal area parts "


def version():
    return "Version 0.1"


def icon():
    return "polygonsplitter.png"


def qgisMinimumVersion():
    return "1.8"

def author():
    return "ViaMap Ltd."

def email():
    return "info@viamap.hu"

def classFactory(iface):
    # load polygonsplitter class from file polygonsplitter
    from polygonsplitter import polygonsplitter
    return polygonsplitter(iface)
