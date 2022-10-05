import csv
import pandas 
import re

train_data = pandas.read_csv('./data/titanic/train.csv')
train_data = train_data[["Survived", "Pclass", "Sex"]]
result = train_data.groupby(['Survived'])
survived = pandas.DataFrame()
not_survived = pandas.DataFrame()

for survived, group in result:
    if(survived == 0):
        not_survived = group
    elif(survived == 1):
        survived = group

apriori_prob_survived = len(survived)/float(len(train_data))
apriori_prob_not_survived = len(not_survived)/float(len(train_data))

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

test_data = pandas.read_csv('./data/titanic/test.csv')
test_data = test_data[["PassengerId", "Pclass", "Sex"]]

def naive_bayes_predict(row):
    prob_not_survived = pclass_probs_not_survived[row.Pclass]*sex_probs_not_survived[row.Sex]*apriori_prob_not_survived
    prob_survived = pclass_probs_survived[row.Pclass]*sex_probs_survived[row.Sex]*apriori_prob_survived
    return 0 if prob_not_survived >= prob_survived else 1

result_data = pandas.DataFrame(columns=['PassengerId', 'Survived'])
for index, row in test_data.iterrows():
    result = naive_bayes_predict(row)
    result_data.loc[len(result_data)] = {'PassengerId': row.PassengerId, 'Survived': result}
result_data.to_csv('./data/predictions/simple_naive_bayes_predictions.csv', index=False)
