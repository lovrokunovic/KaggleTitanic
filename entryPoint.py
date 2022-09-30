import csv
import pandas as pd
import re

class Person:
    def __init__(self, id, survived, gender):
        self.id = id
        self.survived = survived
        self.gender = gender

    def __str__(self):
        return f"id:{self.id}, survived: {self.survived}, gender: {self.gender}"

people = []
with open('./data/titanic/train.csv', "r") as file:
    reader = csv.reader(file, delimiter="\t")
    for i, line in enumerate(reader):
        if i == 0 :
            continue


        # list to string conversion
        stripped = line[0]
        stripped = re.split(r',(?=[^\s]+)',stripped)
        # print(stripped)
        person = Person(stripped[0], int(stripped[1]), stripped[4] )
        people.append(person)

print()
# data = pd.read_csv('./data/titanic/train.csv')
# print(data.to_string())
total = 0
survived = 0
males = 0
females = 0
males_survived_count = 0
females_survived_count = 0

for p in people:
    total += 1
    if(p.gender == "male"):
        males += 1
        if(p.survived):
            survived += 1
            males_survived_count += 1
    if(p.gender == "female"):
        females += 1
        if(p.survived):
            survived += 1
            females_survived_count += 1

print("survived:",survived, "out of", total, "total,", round((survived/total)*100, 2), "%")
print("males survived:", males_survived_count, "out of", males, "total,", round((males_survived_count/males)*100, 2), "%")
print("females survived:", females_survived_count, "out of", females, "total,", round((females_survived_count/females)*100, 2), "%") 
print()
