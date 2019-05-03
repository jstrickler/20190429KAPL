#!/usr/bin/env python
import requests
import bs4
import os
import sys

URL = "https://navalnuclearlab.energy.gov/"
response = requests.get(URL)

if response.status_code == requests.codes.OK:
    content = response.content
    print(content.decode())

URL = "https://navalnuclearlab.energy.gov/ckfinder/userfiles/files/October%202018%20Update%20to%20the%20Kesselring%20Site%20Refueling%20and%20Overhaul%20of%20the%20S8G%20Prototype.pdf"

response = requests.get(
    URL,
    auth=('bob', 'l0l'),
    headings={'x-nnl-secret': 'apple pie'},
    proxy={'https': "myproxy.nnl.energy.gov:1234"},
)

raw_pdf = response.content

FILE_NAME = 'nnl.pdf'

with open(FILE_NAME, 'wb') as nnl_out:
    nnl_out.write(raw_pdf)

if sys.platform == 'win32':
    cmd = FILE_NAME
elif sys.platform == 'darwin':
    cmd = 'open {}'.format(FILE_NAME)
else:  # linux....
    cmd = 'acroread {}'.format(FILE_NAME)

os.system(cmd)


