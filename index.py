import requests
import json
import urllib.request
from appscript import app, mactypes


def main():
    response = requests.get(
        "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-IN"
    )
    todos = json.loads(response.text)
    baseurl = "https://www.bing.com"
    url = baseurl + todos["images"][0]["url"]
    urllib.request.urlretrieve(url, "latest" + ".jpg")
    app('Finder').desktop_picture.set(mactypes.File("latest.jpg"))


if __name__ == "__main__":
    main()
