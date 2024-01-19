#!/usr/bin/python3
from models.engine.file_storage import FileStorage

try:
    print(type(FileStorage.FileStorage_file_path))
except:
    fs = FileStorage()
    print(type(fs.FileStorage_file_path))

