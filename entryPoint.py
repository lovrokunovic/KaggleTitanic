import csv

list = []
dict = {}
with open('./data/titanic/train.csv', "r") as file:
    reader = csv.reader(file, delimiter="\t")
    for i, line in enumerate(reader):
        if i == 0 :
            continue
        # print 'line[{}] = {}'.format(i, line)
        list.append(line)
        print line
        stripped = line
        print stripped

        print ''
        dict[i] = line


# print dict