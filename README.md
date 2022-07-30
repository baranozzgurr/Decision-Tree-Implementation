# Decision-Tree-Implementation
Implementing a Decision Tree in Python, using heuristics such as Variance Impurity and Information Gain.
Each data set is divided into three sets:  the training set, the validation set and the test set.  Data sets are in CSV format.The first line in the file gives the attribute names.  Each line after that is a training (or test) example that contains a list of attribute values separated by a comma. The last attribute is the class-variable.  Assume that all attributes take valuesfrom the domain{0,1}.
The main step in decision tree learning is choosing the next attribute to split on. We are going to implement the following two heuristics for selecting the next attribute.

1.  Information gain heuristic
2.  Variance impurity heuristic.

We are going to Implement reduced error post pruning algorithm on the tree .The steps in the algorithm are given below.


1.Consider each node for pruning.

2.Pruning = removing the subtree at that node, make it a leaf and assign the most common class at that node.

3.A node is removed if the resulting tree performs no worse then the original on the validation set.

4.Nodes are removed iteratively choosing the node whose removeal most increases the decision tree accuracy on the graph.

5.Pruning continues until further pruning is harmful.

We will use the following format for the output:

wesley = 0 :

| honor = 0 :

| | barclay = 0 : 1

| | barclay = 1 : 0

| honor = 1 :

| | tea = 0 : 0

| | tea = 1 : 1

wesley = 1 : 0

According to this tree, if wesley = 0 and honor = 0 and barclay = 0,then the class value of the corresponding instance should be 1.  In otherwords, the value appearing before a colon is an attribute value, and thevalue appearing after a colon is a class value.

Compile Insruction is below.

For Dataset 1:
python main.py training_set.csv validation_set.csv test_set.csv no H2
yes/no=to print
H1=Variance
H2=Entropy

For Dataset 2:
python main2.py training_set.csv validation_set.csv test_set.csv no H2


