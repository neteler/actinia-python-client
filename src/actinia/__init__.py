#!/usr/bin/env python

"""Initialize the actinia-python-client package.

actinia-python-client is a python client for actinia - an open source REST
API for scalable, distributed, high performance processing of geographical
data that uses GRASS GIS for computational tasks.

Copyright (c) 2022-2025 mundialis GmbH & Co. KG

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

__license__ = "GPLv3"
__author__ = "Anika Weinmann"
__copyright__ = "Copyright 2022-2025, mundialis GmbH & Co. KG"
__maintainer__ = "Anika Weinmann"

from importlib.metadata import PackageNotFoundError, version

from actinia.actinia import Actinia as Actinia

try:
    # Change here if project is renamed and does not equal the package name
    __version__ = version(__name__).version
except PackageNotFoundError:
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError
