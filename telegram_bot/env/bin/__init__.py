from download import Downloader
from parse import Parser
from data import Data

# region = "base params"
PARAMS = {}
URL = "https://anilibria.life/serials/"
FILE_PATH = "anilibria.html"
PARSED_FILE_PATH = "anilibria_data.json"
# endregion


class TgBot_logic:
    

    
    def procees (self, url, web_page_path = None, data_path = None) :
        
        # region = "download block"
        downloader = Downloader(url = url, params = PARAMS, method = "GET") # Download our page and save to '.html' file
        downloader.get_html(pages_count = 10)
        downloader.save(web_page_path)
        # endregion

        # region = "Parse block"
        parser = Parser(web_page_path) # Parse our page into a json file
        parser.parse()
        parser.save(data_path)
        # endregion

        
        data = Data(data_path) # Object to import and start our logic
        

        return data.anime_data_analisys()

    #print(procees(URL, FILE_PATH, PARSED_FILE_PATH))