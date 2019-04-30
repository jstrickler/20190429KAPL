#!/usr/bin/env python
import requests
import bs4

URL = "https://navalnuclearlab.energy.gov/"
response = requests.get(URL)

if response.status_code == requests.codes.OK:
    content = response.content

    soup = bs4.BeautifulSoup(content, ='lxml')

    print(soup)
    for link in soup.findall("a"):
        print(link)



