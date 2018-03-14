'''
Generates frequent item sets and association rules from given datasets using Apriori algorithm.
'''
# pylint: disable=invalid-name
import csv
import itertools

DataFile = open('groceries2.csv', 'r')
minsup = 0.03
f2 = "Rules.txt"
f1 = "FItems.txt"
minconf = 0.39


def L1():
    '''
    Find frequent 1-itemsets
    '''
    #Get all 1-itemsets in the list items and their counts in the dictionary counts
    DataCaptured = csv.reader(DataFile, delimiter=',')
    data = list(DataCaptured)
    for e in data:
        e = sorted(e)
    count = {}
    for items in data:
        for item in items:
            if item not in count:
                count[(item)] = 1
            else:
                count[(item)] = count[(item)] + 1
    #print("C1 Items", count)
    print("C1 Length : ", len(count))
    print()

    #Thresholding
    count2 = {k: v for k, v in count.items() if v >= minsup*9835}
    #print("L1 Items : ", count2)
    print("L1 Length : ", len(count2))
    print()

    return count2, data


def generateCk(Lk_1, flag, data):
    '''
    Generate Ck by joining 2 Lk-1
    '''
    Ck = []

    if flag == 1:
        flag = 0
        for item1 in Lk_1:
            for item2 in Lk_1:
                if item2 > item1:
                    Ck.append((item1, item2))
        print("C2: ", Ck[1:3])
        print("length : ", len(Ck))
        print()

    else:
        for item in Lk_1:
            k = len(item)
        for item1 in Lk_1:
            for item2 in Lk_1:
                if (item1[:-1] == item2[:-1]) and (item1[-1] != item2[-1]):
                    if item1[-1] > item2[-1]:
                        Ck.append(item2 + (item1[-1],))
                    else:
                        Ck.append(item1 + (item2[-1],))
        print("C" + str(k+1) + ": ", Ck[1:3])
        print("Length : ", len(Ck))
        print()
    L = generateLk(set(Ck), data)
    return L, flag


def generateLk(Ck, data):
    '''
    If item in Ck belongs to a transaction,
    it makes it into list Ct
    Then Ct is thresholded to form L
    '''
    count = {}
    for itemset in Ck:
        #print(itemset)
        for transaction in data:
            if all(e in transaction for e in itemset):
                if itemset not in count:
                    count[itemset] = 1
                else:
                    count[itemset] = count[itemset] + 1

    print("Ct Length : ", len(count))
    print()

    count2 = {k: v for k, v in count.items() if v >= minsup*9835}
    print("L Length : ", len(count2))
    print()
    return count2


def rulegenerator(fitems):
    '''
    Generates association rules from the frequent itemsets
    '''
    counter = 0
    for itemset in fitems.keys():
        if isinstance(itemset, str):
            continue
        length = len(itemset)

        union_support = fitems[tuple(itemset)]
        for i in range(1, length):

            lefts = map(list, itertools.combinations(itemset, i))
            for left in lefts:
                if len(left) == 1:
                    if ''.join(left) in fitems:
                        leftcount = fitems[''.join(left)]
                        conf = union_support / leftcount
                else:
                    if tuple(left) in fitems:
                        leftcount = fitems[tuple(left)]
                        conf = union_support / leftcount
                if conf >= minconf:
                    fo = open(f2, "a+")
                    right = list(itemset[:])
                    for e in left:
                        right.remove(e)
                    fo.write(str(left) + ' (' + str(leftcount) + ')' + ' -> ' + str(right) + ' (' + str(fitems[''.join(right)]) + ')' + ' [' + str(conf) + ']' + '\n')
                    print(str(left) + ' -> ' + str(right) + ' (' + str(conf) + ')')
                    counter = counter + 1
                    #Greater than 1???
                    fo.close()
    print(counter, "rules generated")


def apriori():
    '''
    The runner function
    '''
    L, data = L1()
    flag = 1
    FreqItems = dict(L)
    while(len(L) != 0):
        fo = open(f1, "a+")
        for k, v in L.items():
            fo.write(str(k) + ' >>> ' + str(v) + '\n\n')
        fo.close()

        L, flag = generateCk(L, flag, data)
        FreqItems.update(L)
    rulegenerator(FreqItems)


if __name__ == '__main__':
    apriori()
