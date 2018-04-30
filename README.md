# Apriori-Implementation-in-Python
This Python program generates frequent item sets and association rules from given datasets using Apriori algorithm.

## Different support and confidence values - outputs:
  
``` Support, confidence - #rules generated
0.02, 0.35 - 26
0.02, 0.42 - 10
0.03, 0.39 - 6
0.04, 0.35 - 5
0.04, 0.42 - 2
0.05, 0.35 - 0
```

The output is stored in 2 files:

### File1:
<pre>Format: Freq Itemset >>> count
Global variable f1
Default value of f1 : FItems.txt
</pre>

### File2:
<pre>Format: LHS itemset (count) -> RHS itemset (count) [confidence] 
Global variable f2
Default value of f2 : Rules.txt

The outputs are appended to the files
So if you want to run the program multiple times, remember that the data will be written multiple times
</pre>
### Dataset used:
groceries.csv

### Rules for using other datasets:
Change the global variable DataFile to the filename

## Pre-processing of data
### Sorter.py - to sort the transactions data in lexicographical order Stripped off whitespaces and newlines.
<pre>And converted the data into a more comfortable format for running the program,
with each line representing a single transaction, with the items being comma separated.
Got each transaction as a list from the csv and sorted each list and wrote the sorted transactions into a new csv.
</pre>
## Formulae used and pseudo code of algorithm:

## Apriori:-
<pre>Generate frequent 1-itemsets - L1()
Generate Ck from Lk-1 - generateCk()
Generate Lk from Ck - generateLk()
Generate rules from frequent itemsets - rulegenerator()

Each of these are written in detail below.
</pre>
### L1():	Find frequent 1-itemsets
<pre>Read data from the csv file and store it into a list.
Sort the data if necessary.
Go through all the elements in each transaction and store their counts in a dictionary.
Threshold them i.e create a new dictionary with old dictionary values that had a support greater than the support threshold.
The final list is made into a set, to avoid repetition.
</pre>
### generateCk(Lk_1, flag, data): Generate Ck by joining 2 Lk-1 
<pre>Traverse through all the itemsets of Lk_1 and on finding 2 itemsets that are identical,
except for the last element, merge them (i.e their union)in a sorted manner and insert into Ck.
The final list Ck is made into a set, to avoid repetition.
</pre>
### generateLk(Ck, data):	Ck -> Ct -> L
<pre>If itemset in Ck belongs to a transaction, it makes it into list Ct, and its support is updated by 1,
each time a transaction contains the itemset. Then Ct is thresholded to form L,
using the support calculated during creation of Ct. L is stored in a new dicitonary,
by choosing itemsets above threshold from the old dictionary.
</pre>
### rulegenerator(fitems): Generates association rules from the frequent itemsets
<pre>For each itemset in the frequent items list, compute its total support.
Then get a list of all possible combinations of splitting the itemset into LHS and RHS, with min of 1 element.
Calculare support for each of these combinations from the dictionary, 
and if total_support/combination_support is greater than the min confidence value,
it is added as a rule, and written to f2.
</pre>

A lot of conversion of lists to tuples would be required, since lists cannot be hashed into dictionaries as keys.

And lists should be converted into sets, to avoid repetition, which could affect the count values significantly, otherwise.
