#!/usr/bin/env python
import os
from datetime import datetime, timedelta

now = datetime.now()

TARGET_FOLDER = '.'


for curr_dir, subs, files in os.walk(TARGET_FOLDER):
    if '.git' in curr_dir:
        continue
    print(curr_dir)
    for file_name in files:
        if file_name.endswith('.py'):
            file_path = os.path.join(curr_dir, file_name)
            file_size  = os.path.getsize(file_path)
            raw_file_modtime = os.path.getmtime(file_path)
            file_modtime = datetime.fromtimestamp(raw_file_modtime)
            # print(file_modtime, now.date())
            if file_modtime < (now - timedelta(30)):
                print("    {:5d} {} {}".format(file_size, file_modtime.date(), file_name))
