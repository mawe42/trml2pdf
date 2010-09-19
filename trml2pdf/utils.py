# trml2pdf - An RML to PDF converter
# Copyright (C) 2003, Fabien Pinckaers, UCL, FSA
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

import re
import reportlab


UNITS = [
    (re.compile('^(-?[0-9\.]+)\s*in$'), reportlab.lib.units.inch),
    (re.compile('^(-?[0-9\.]+)\s*cm$'), reportlab.lib.units.cm),
    (re.compile('^(-?[0-9\.]+)\s*mm$'), reportlab.lib.units.mm),
    (re.compile('^(-?[0-9\.]+)\s*$'), 1)]


def text_get(node):
    """
    get a text value of a node
    """
    text = ''
    for node in node.childNodes:
        if node.nodeType == node.TEXT_NODE:
            text = text + node.data
    return text


def unit_get(size):
    """
    parse a size unit
    """
    for unit in UNITS:
        res = unit[0].search(size, 0)
        if res:
            return unit[1] * float(res.group(1))
    return False


def tuple_int_get(node, attr_name, default=None):
    """
    return a tuple of integers from a node
    """
    if not node.hasAttribute(attr_name):
        return default
    res = [int(x) for x in node.getAttribute(attr_name).split(',')]
    return tuple(res)


def bool_get(value):
    """
    return a boolean from a string value
    """
    return (str(value) == "1") or (value.lower() == 'yes')


def attr_get(node, attrs, types=None):
    """
    parse a node and its attributes
    returning the data type specified in types
    otherwise returns a string
    """
    res = {}
    for name in attrs:
        if node.hasAttribute(name):
            res[name] = unit_get(node.getAttribute(name))
    if types:
        for key in types:
            if node.hasAttribute(key):
                if types[key] == 'str':
                    res[key] = str(node.getAttribute(key))
                elif types[key] == 'bool':
                    res[key] = bool_get(node.getAttribute(key))
                elif types[key] == 'int':
                    res[key] = int(node.getAttribute(key))
    return res
