import os
import json
 
BASE_DIR = os.path.dirname(os.path.realpath(__file__)) + "/"

class Data:
    def __init__(self, filename : str = "anilibria_data.json"):
        self.json_data: dict = {}
        self.txt_analysis: str = ""
        self.filename: str = filename
        
        try :
            with open(BASE_DIR + filename) as file:
                self.json_data = json.load(file)
                print(BASE_DIR + filename)
        except :
            pass


    def avg_rating(self):
        lst:list = []
        for _, data in self.json_data.items():
            lst.append(int(data["rating"]))

        return sum(lst)/ len(lst)

    # Подсчет среднего рейтинга по жанрам
    def anime_data_analisys(self) :
        tmp_dict = {}
        # region Средний рейтинг по жанрам
        txt_result = "Средний рейтинг по жанрам:\n"
        for _, data in self.json_data.items():
            if data["Жанр"] in tmp_dict:
                tmp_dict[data["Жанр"]].append(int(data["rating"]))
            else:
                tmp_dict[data["Жанр"]] = [int(data["rating"])]
                
        for key, value in tmp_dict.items():
            tmp_dict[key] = str(int(sum(value)/ len(value)))
        # endregion

        # region Кол-во аниме по жанру
        tmp_dict_counter = {}
        for _,data in self.json_data.items():
            genre = data["Жанр"]
            if tmp_dict_counter.get(genre):
                tmp_dict_counter[genre] += 1
            else:
                tmp_dict_counter[genre] = 1
        tmp_dict_counter = {k:v for k, v in sorted(tmp_dict_counter.items(), key= lambda x: x[1], reverse=True)}

        for key_genre, _ in tmp_dict.items():
            for key_count, _ in tmp_dict_counter.items():
                if key_genre == key_count :
                    tmp_dict[key_genre] += "\t\t|\t Кол-во выпущенных аниме: {0}".format(tmp_dict_counter[key_count]).ljust(40)
        # endregion

        for key, value in tmp_dict.items():
            txt_result += f"{key}: {value}\n"
        
        return txt_result

    # Кол-во аниме по жанру
    def __count_genre(self):
        tmp_dict: dict = {}
        txt_result = ""
        for _,data in self.json_data.items():
            genre = data["Жанр"]
            if tmp_dict.get(genre):
                tmp_dict[genre] += 1
            else:
                tmp_dict[genre] = 1
        tmp_dict = {k:v for k, v in sorted(tmp_dict.items(), key= lambda x: x[1], reverse=True)}
        
        for key, value in tmp_dict.items():
            txt_result += f"{key}: {value}\n"

        return txt_result
        

#data = Data("anilibria_data.json")
#print(data.count_genre())

    

#data = Data("anilibria_data.json")
#print(data.anime_data_analisys())

