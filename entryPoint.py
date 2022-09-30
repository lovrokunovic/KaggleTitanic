import csv
import pandas as pd
import re

class Person:
    def __init__(self, id, survived, sex):
        self.id = id
        self.survived = survived
        self.sex = sex

    def __str__(self):
        return f"{self.id},{self.survived},{self.sex}"

people = []
with open('./data/titanic/train.csv', "r") as file:
    reader = csv.reader(file, delimiter="\t")
    for i, line in enumerate(reader):
        if i == 0 :
            continue


        # list to string conversion
        stripped = line[0]
        stripped = re.split(r',(?=[^\s]+)',stripped)
        print(stripped)
        person = Person(stripped[0], stripped[1], stripped[4])
       
        people.append(person)


# data = pd.read_csv('./data/titanic/train.csv')
# print(data.to_string())
