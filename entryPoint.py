import csv
import pandas 
import re

data_frame = pandas.read_csv('./data/titanic/train.csv')
# print("rows, cols:", data_frame.shape) 
# print(data_frame.info())

print()
# print(data_frame.describe())
data_frame = data_frame[["Survived", "Pclass", "Sex"]]
result = data_frame.groupby(['Survived'])

survived = pandas.DataFrame()
not_survived = pandas.DataFrame()
for survived, group in result:
    if(survived == 0):
        not_survived = group
    elif(survived == 1):
        survived = group

# print(survived)
# print()
# print(not_survived)

apriori_prob_survived = len(survived)/float(len(data_frame))
apriori_prob_not_survived = len(not_survived)/float(len(data_frame))

pclass_counts_not_survived = not_survived['Pclass'].value_counts()
pclass_counts_survived = survived['Pclass'].value_counts()

sex_counts_not_survived = not_survived['Sex'].value_counts()
sex_counts_survived = survived['Sex'].value_counts()

pclass_counts_not_survived = dict(pclass_counts_not_survived)
pclass_counts_survived = dict(pclass_counts_survived)

sex_counts_not_survived = dict(sex_counts_not_survived)
sex_counts_survived = dict(sex_counts_survived)

pclass_probs_not_survived = {key: value/float(len(not_survived)) for key, value in pclass_counts_not_survived.items()}
pclass_probs_survived =  {key: value/float(len(survived)) for key, value in pclass_counts_survived.items()}
sex_probs_not_survived = {key: value/float(len(not_survived)) for key, value in sex_counts_not_survived.items()}
sex_probs_survived = {key: value/float(len(survived)) for key, value in sex_counts_survived.items()}

print(pclass_probs_not_survived)
print(pclass_probs_survived)
print(sex_probs_not_survived)
print(sex_probs_survived)