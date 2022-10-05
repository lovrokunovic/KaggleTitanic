import csv
import pandas 
import re

train_data = pandas.read_csv('./data/titanic/train.csv')
# print("rows, cols:", train_data.shape) 
# print(train_data.info())

print()
# print(train_data.describe())
train_data = train_data[["Survived", "Pclass", "Sex"]]
result = train_data.groupby(['Survived'])

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

# print(pclass_probs_not_survived)
# print(pclass_probs_survived)
# print(sex_probs_not_survived)
# print(sex_probs_survived)


test_data = pandas.read_csv('./data/titanic/test.csv')
test_data = test_data[["PassengerId", "Pclass", "Sex"]]
# print(test_data)

# TODO overflows management using logarithms
# return 0 if prediction is not_survived and 1 if prediction is survived (return class 0 or 1)
def naive_bayes_predict(row):
    print()
    # p(y0|x) = p(x|y0) * p(y0) = p(x1|y0)*p(x2|y0) * p(y0)
    # p(y0) == apriori_prob_not_survived
    # p(x1|y0) == pclass_probs_not_survived[row.Pclass]
    # p(x2|y0) == sex_probs_not_survived[row.Sex]
    prob_not_survived = pclass_probs_not_survived[row.Pclass]*sex_probs_not_survived[row.Sex]*apriori_prob_not_survived
    # print(prob_not_survived)

    # p(y1|x) = p(x|y1) * p(y1) = p(x1|y1)*p(x2|y1) * p(y1)
    # p(y1) == apriori_prob_survived
    # p(x1|y1) == pclass_probs_survived[row.Pclass]
    # p(x2|y1) == sex_probs_survived[row.Sex]
    prob_survived = pclass_probs_survived[row.Pclass]*sex_probs_survived[row.Sex]*apriori_prob_survived
    # print(prob_survived)

    # print("Probability of survival is:", round(100*prob_survived/float(prob_not_survived+prob_survived), 2), "%")
    
    return 0 if prob_not_survived >= prob_survived else 1

for index, row in test_data.iterrows():
    # print(row)
    passenger_id = row.PassengerId
    result = naive_bayes_predict(row)
    print(result)
    print()
    break

