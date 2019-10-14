# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 National Institute of Informatics.
#
# Invenio-ResourceSync is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio module that adds ResourceSync function to the platform."""

from __future__ import absolute_import, print_function

from .ext import InvenioResourceSync
from .version import __version__

__all__ = ('__version__', 'InvenioResourceSync')
