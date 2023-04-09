import requests
import os
from parse import *
from dataclasses import dataclass
BASE_DIR = os.path.dirname(__file__) + "//"

@dataclass
class Downloader:
    url: str 
    params: dict
    method: str = "GET"
    html_text: str = None

    def __init__(self, url: str, params: dict, method: str = "GET"):
        self.url = url
        self.params = params

    def get_html(self, pages_count : int = 50):
        result = ""
        for page_id in range(pages_count):
            if page_id != 1: 
                # https://anilibria.life/page/23/
                self.url =  f"https://anilibria.life/serials/page/{page_id}/"
            result += requests.request(url = self.url, params=self.params, method=self.method).text
            result += "\n"
        self.html_text = result

    def save(self, filename: str):
        with open(BASE_DIR + filename, "w") as file:
            file.write(self.html_text)

if __name__ == "__main__" :
    URL = "https://anilibria.life/serials/"
    PARAMS = {}
    FILE_PATH = "anilibria.html"
    downloader = Downloader(url = URL, params=PARAMS, method="GET") # Download our page and save to '.html' file
    downloader.get_html()
    downloader.save(FILE_PATH)