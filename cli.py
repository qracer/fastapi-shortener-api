import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument('-s', "--shorten", nargs=1)    
parser.add_argument('-f', "--find", nargs=1)
parser.add_argument('-u', "--unpack", nargs=1)
args = parser.parse_args()

linkToFind = args.find
if linkToFind != None:
    linkToFind = linkToFind[0]
    r = requests.get("http://localhost:8000/find_shortened/", params={"url": linkToFind})
    print(r.json())
    exit()
    
linkToFind = args.unpack
if linkToFind != None:
    linkToFind = linkToFind[0]
    r = requests.get("http://localhost:8000/find_original/", params={"url": linkToFind})
    print(r.json())
    exit()

linkToShorten = args.shorten
if linkToShorten != None:
    linkToShorten = linkToShorten[0]
    dic = {"url": linkToShorten}
    r = requests.post("http://localhost:8000/shorten/", json = {
        "url": linkToShorten
    })
    print(r.json())
    exit()