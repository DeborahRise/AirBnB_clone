#!/usr/bin/python3
""" data handling
This module instantiates an object
of class FileStorage
"""

from models.engine.file_storage import FileStorage
""" successfully imported """

storage = FileStorage()
storage.reload()
