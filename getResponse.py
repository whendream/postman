__author__ = 'jun.wen'
import requests
import json

def getReq(url):
    r = requests.get(url)
    return json.dumps(json.loads(r.text), indent=4, sort_keys=False, ensure_ascii=False)
     

if __name__ == "__main__":
    #url = 'http://www.runoob.com/try/angularjs/data/sites.php'
    url = 'https://api.douban.com/v2/book/1220562'

    print(getReq(url))
