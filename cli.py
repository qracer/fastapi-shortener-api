import argparse
import requests

help_shorten = "Creates a shortened link\n" \
    "For example: py cli.py -s https://google.com/"

help_find = "Finds a shortened URI by original URL\n" \
    "For example: py cli.py -f https://cnn.com/"
    
help_unpack = "Finds an original URL by shortened version\n" \
    "For example: py cli.py -u 9JH4G"

help_create = "Creates a custom version of shortened URL provided by a user\n" \
    "For example: py cli.py -c https://dw.com/ DWCOM"

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-s', "--shorten", nargs=1, help=help_shorten)
parser.add_argument('-f', "--find", nargs=1, help=help_find)
parser.add_argument('-u', "--unpack", nargs=1, help=help_unpack)
parser.add_argument('-c', "--create", nargs=2, help=help_create)
args = parser.parse_args()

linkToFind = args.find
if linkToFind != None:
    linkToFind = linkToFind[0]
    r = requests.get("http://localhost:8000/find_shortened/",
                     params={"url": linkToFind})
    print(r.json())

linkToFind = args.unpack
if linkToFind != None:
    linkToFind = linkToFind[0]
    r = requests.get("http://localhost:8000/find_original/",
                     params={"url": linkToFind})
    print(r.json())

linkToShorten = args.shorten
if linkToShorten != None:
    linkToShorten = linkToShorten[0]
    r = requests.post("http://localhost:8000/shorten/", json={
        "url": linkToShorten
    })
    print(r.json())

custom_link = args.create
if custom_link != None:
    url = custom_link[0]
    shortUrl = custom_link[1]
    r = requests.post("http://localhost:8000/create/", json={
        "url": url,
        "shortened_url": shortUrl
    })
    print(r.json())
