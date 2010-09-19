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

from reportlab.lib import colors

RGB_REGEX = re.compile('\(([0-9\.]*),([0-9\.]*),([0-9\.]*)\)')
HEX_REGEX = re.compile('#([0-9a-zA-Z][0-9a-zA-Z])([0-9a-zA-Z]' \
                     '[0-9a-zA-Z])([0-9a-zA-Z][0-9a-zA-Z])')


def get(col_str):
    """
    parse a string and return a tuple
    """
    all_colors = colors.getAllNamedColors()

    if col_str in all_colors.keys():
        return all_colors[col_str]

    res = RGB_REGEX.search(col_str, 0)

    if res:
        return (float(res.group(1)),
                float(res.group(2)),
                float(res.group(3)))

    res = HEX_REGEX.search(col_str, 0)

    if res:
        return tuple([float(int(res.group(i), 16)) / 255 for i in range(1, 4)])
    return colors.red
