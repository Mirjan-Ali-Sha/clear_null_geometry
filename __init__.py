# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ClearNullGeometry
                                 A QGIS plugin
 Clear Null Geometry is a QGIS Plugin which is use to remove all Null geometries from selected layers.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-04-03
        copyright            : (C) 2022 by Mirjan Ali Sha
        email                : mirrjanalisha@gmail.com
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ClearNullGeometry class from file ClearNullGeometry.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .clear_null_geometry import ClearNullGeometry
    return ClearNullGeometry(iface)