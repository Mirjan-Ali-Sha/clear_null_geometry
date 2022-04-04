# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ClearNullGeometry
                                 A QGIS plugin
 Clear Null Geometry is a QGIS Plugin which is use to remove all Null geometries from selected layers.
                              -------------------
        begin                : 2022-04-03
        git sha              : $Format:%H$
        copyright            : (C) 2022 by Mirjan Ali Sha
        email                : mirrjanalisha@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the BSD 3-Clause License, or                    *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction
from qgis.core import *

# Initialize Qt resources from file resources.py
from .resources import *
import os.path


class ClearNullGeometry:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        
    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        self.action = QAction(QIcon(":/plugins/clear_null_geometry/icon.png"),u"Clear Null Geometry", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToVectorMenu(u"&Clear Null Geometry", self.action)


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""

        self.iface.removePluginMenu(u"&Clear Null Geometry", self.action)
        self.iface.removeToolBarIcon(self.action)


    def run(self):
        """Run method that performs all the real work"""

        layers = self.iface.layerTreeView().selectedLayers()
        for lyr in range(0,len(layers),1):
                features = layers[lyr].getFeatures()
                geometryType = int(layers[lyr].geometryType())
                layer_provider = layers[lyr].dataProvider()
                layers[lyr].startEditing()
                requestnull = "$geometry is NULL"
                requestempty =  "$geometry is EMPTY"
                nullitem = layers[lyr].getFeatures(QgsFeatureRequest().setFilterExpression(requestnull))
                emptyitem = layers[lyr].getFeatures(QgsFeatureRequest().setFilterExpression(requestempty))
                layer_provider.deleteFeatures([i.id() for i in nullitem]) # Delete the selected features
                layer_provider.deleteFeatures([i.id() for i in emptyitem])
                layers[lyr].commitChanges()
        self.iface.messageBar().pushMessage("Done", "All NULL geometries successfully cleared.", level=Qgis.Info)
