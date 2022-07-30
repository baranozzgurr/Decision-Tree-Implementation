import var
import sys
import Entropy
import Calculate
from collections import defaultdict
import csv
import Variance
#for dataset 1
def main():
    directory="dataset 1/"
        
    train_file = directory + sys.argv[1]
    validation_file = directory + sys.argv[2]
    test_file = directory + sys.argv[3]
    to_print = str(sys.argv[4])
    heuristic=str(sys.argv[5])
    if heuristic== "H1":
        decisionTree = Variance.Decision_Tree(train_file)
    elif heuristic== "H2":
        decisionTree = Entropy.Decision_Tree(train_file)
    if to_print == "yes":
        print "Decision Tree:" #printing tree
        print decisionTree

    accuracy = Calculate.Set_accuracy(test_file)
    accuracy.FindAcc(decisionTree.Rnode)
    print "Test Data Accuracy is:"
    accuracy.displayAccuracy()
    
def csplit(self, filename):
    self.d_arr = []
    ##self.arr=[]
    with open(filename,'rb') as csvfile:
        numb=0
        csvreader = csv.reader(csvfile, delimiter = ',')
        
        for row in csvreader:
            if numb==0:
                self.name=row[:-1]
            else:
                self.d_arr.append([int(i) for i in row])
            numb=numb+1

    self.attributes = range(len(self.name))
    self.Class = [row[-1] for row in self.d_arr]
    self.train_values = range(len(self.d_arr))
    
    return self

main()


    

    


