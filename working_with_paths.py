#!/usr/bin/env python
import os
from datetime import datetime
from humanize import filesize
FOLDER = 'DATA'
FILE_NAME = 'alice.txt'

file_path = os.path.join(FOLDER, FILE_NAME)
print("file path:", file_path)
file_size = os.path.getsize(file_path)
print("raw file size:", file_size)
print("file size:", filesize.naturalsize(file_size))
raw_timestamp = os.path.getmtime(file_path)
print("raw timestamp:", raw_timestamp)
file_timestamp = datetime.fromtimestamp(raw_timestamp)
print("timestamp:", file_timestamp)

print('directory:', os.path.dirname(file_path))
print("file name:", os.path.basename(file_path))
print("absolute path:", os.path.abspath(file_path))
for name in 'alice.txt', 'mary.txt', 'wombat.txt':
    print(name, os.path.exists(os.path.join('DATA', name)))




