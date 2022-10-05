import csv
import pandas 
import re

class Person:
    def __init__(self, id, survived, gender):
        self.id = id
        self.survived = survived
        self.gender = gender

    def __str__(self):
        return f"id:{self.id}, survived: {self.survived}, gender: {self.gender}"


people = []
survived = []
not_survived = []

with open('./data/titanic/train.csv', "r") as file:
    reader = csv.reader(file, delimiter="\t")
    for i, line in enumerate(reader):
        if i == 0 :
            continue
        # list to string conversion
        stripped = line[0]
        stripped = re.split(r',(?=[^\s]+)', stripped)
        person = Person(stripped[0], int(stripped[1]), stripped[4])
       
        people.append(person)
        if(person.survived):
            survived.append(person)
        else:
            not_survived.append(person)
        

print()
total = len(survived) + len(not_survived) # = i

print("survived:",len(survived), "out of", total, "total,", round((len(survived)/total)*100, 2), "%")
   
       
print()
print()
print()
print()


data_frame = pandas.read_csv('./data/titanic/train.csv')
# print("rows, cols:", data_frame.shape) 
# print(data_frame.info())
data_frame = data_frame[["Survived", "Pclass", "Sex"]]
result = data_frame.groupby(['Survived'])

survived = pandas.DataFrame()
not_survived = pandas.DataFrame()
for survived, group in result:
    if(survived == 0):
        not_survived = group
    elif(survived == 1):
        survived = group

print(survived)
print()
print(not_survived)

apriori_prob_survived = len(survived)/float(len(data_frame))
apriori_prob_not_survived = len(not_survived)/float(len(data_frame))

pclass_counts_not_survived = not_survived['Pclass'].value_counts()
pclass_counts_survived = survived['Pclass'].value_counts()

sex_counts_not_survived = not_survived['Sex'].value_counts()
sex_counts_survived = survived['Sex'].value_counts()

print()
print("Not survived:")
print(pclass_counts_not_survived)
print(sex_counts_not_survived)

print()
print("Survived:")
print(pclass_counts_survived)
print(sex_counts_survived)
print()

print(dict(sex_counts_survived))
