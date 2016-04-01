# ##### BEGIN GPL LICENSE BLOCK #####
#
# Part of the Cycles sub-package of Blib.
# Cycles Blib utilities: Common Cycles Blib functions.
# Copyright (C) 2016  Luca Rood
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####

"""Utility functions for the Cycles Blib package."""

import bpy

import xml.etree.cElementTree as ET
import zipfile as zf
from ..exceptions import InvalidObject
from ..utils import get_file_type

def check_asset(asset, do_raise=False):
    """
    Check if asset is a Cycles material or node group,
    and thus is exportable by the 'cycles' package.
    
    Args:
        asset (any type): Asset to be checked for validity.
        do_raise (bool): If True, an exception is raised for invalid assets,
            instead of returning False.
    
    Returns:
        bool: True if check is passed, otherwise returns False.
        Note that False is only ever returned if 'do_raise' is False,
        otherwise an exception is raised instead.
    
    Raises:
        blib.exeptions.InvalidObject: If the check fails and 'do_raise' is True.
    """
    
    if asset:
        if isinstance(asset, bpy.types.Material):
            if asset.use_nodes:
                tree = asset.node_tree
            else:
                if do_raise:
                    raise InvalidObject("Material can't be exported, contains no node tree.")
                else:
                    return False
        elif isinstance(asset, bpy.types.ShaderNodeTree):
            if asset.type == 'SHADER':
                tree = asset
            else:
                if do_raise:
                    raise InvalidObject("Node tree is not of SHADER type.")
                else:
                    return False
        else:
            if do_raise:
                raise InvalidObject("Object passed is not a material or node group.")
            else:
                return False
        
        groups = [tree]
        while groups:
            for node in groups.pop(0).nodes:
                if 'NEW_SHADING' not in node.shading_compatibility:
                    if do_raise:
                        raise InvalidObject("Node tree contains non Cycles nodes.")
                    else:
                        return False
                
                if node.bl_static_type == 'GROUP':
                    groups.append(node.node_tree)
    return True

def get_sub_type(f_path):
    """
    Get the subtype of a 'cycles' type Blib file.
    
    Args:
        f_path (str): Path to the file to be checked.
    
    Returns:
        str or None
        A string containing the Blib sub-type is returned,
        if no valid sub-type is found, None is returned.
    """
    
    try:
        archive = zf.ZipFile(f_path, 'r')
    except zf.BadZipFile:
        return None
    
    try:
        xml_file = archive.open("structure.xml", 'r')
    except KeyError:
        return None
    
    tree = ET.ElementTree(file=xml_file)
    xml_file.close()
    xroot = tree.getroot()
    if xroot.tag != "blib":
        return None
    if xroot.attrib["type"] != "cycles":
        return None
    if xroot.find("main") is not None:
        return "mat"
    if xroot.find("resources") is not None:
        return "grp"
    return None

def check_file(f_path, sub=None):
    """
    Check if file is a 'cycles' type blib file.
    Optionally check if file is of a specific subtype.
    
    Args:
        f_path (str): Path to the file to be checked.
        sub (str or None): If a str is provided, it should be the subtype to check against,
            if None is given, no subtype check is performed.
    
    Returns:
        bool: True if the file is of type 'cycles', and if it matches the optional subtype.
    """
    
    if get_file_type(f_path) == "cycles":
        if sub is not None:
            return get_sub_type(f_path) == sub
        else:
            return True
    else:
        return False
