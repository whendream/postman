__author__ = 'jun.wen'
import requests
import json

def getReq(url):
    r = requests.get(url)

    return r.text

if __name__ == "__main__":
    url = 'http://www.runoob.com/try/angularjs/data/sites.php'

    print(getReq(url))
