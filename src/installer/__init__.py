# -*- coding=utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from ._pip import (
    WheelInstaller, EditableInstaller, uninstall, RequirementUninstaller
)
from .operations import sync, clean
from .synchronizer import Cleaner, Synchronizer

__version__ = '0.1.1'

__all__ = [
    "Cleaner", "clean", "EditableInstaller", "RequirementUninstaller",
    "sync", "Synchronizer", "uninstall", "WheelInstaller"
]
