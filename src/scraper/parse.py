from bs4 import BeautifulSoup as bs
import os
 
BASE_DIR = os.path.dirname(os.path.realpath(__file__)) + "//"


class Parser:
    def __init__(self, source) -> None:
        self.source: str = source
        self.json_dict: dict = {}
 
    @staticmethod
    def __read_html(filename: str):
        with open(BASE_DIR + filename, "r") as file:
            text = file.read()
        return text
 
    def parse(self):
        info = bs(Parser.__read_html(self.source), "html.parser")

        for anime in info.find_all("div", class_ = "kino-item ignore-select"):
            main_name = anime.find("h2").text.split(" [")[0]

            rating = anime.find("li", class_ = 'current-rating').text
            some_info = anime.find("ul", class_ = "kino-lines")
            tmp_dct: dict = {"rating": rating}
            for info in some_info.find_all("li"):
                name, value = info.text.split(": ")
                tmp_dct[name] = value
            self.json_dict[main_name] = tmp_dct
            


    def save(self, filename:str):
        import json
        with open(BASE_DIR + filename, "w") as file:
            file.write(json.dumps(self.json_dict, ensure_ascii = False, indent = 2))
 

if __name__ == "__main__" :  
    FILE_PATH = "anilibria.html"
    parser = Parser(FILE_PATH)
    parser.parse()
    parser.save("anilibria_data.json")

