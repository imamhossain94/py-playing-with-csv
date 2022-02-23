import csv
import json


def saveJson():
    with open('new-json/prods.json', 'w') as outfile:
        json.dump(myDict1, outfile)
    with open('new-json/stds.json', 'w') as outfile:
        json.dump(myDict2, outfile)


def read_csv(filename):
    with open(filename,  encoding="utf8") as f:
        file_data = csv.reader(f)
        headers = next(file_data)
        return [dict(zip(headers, i)) for i in file_data]


myDict1 = read_csv("new-files/prods.csv")
myDict2 = read_csv("new-files/stds.csv")


saveJson()


