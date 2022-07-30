import sys
import main
import Calculate
import random
import copy
from collections import deque
import math



#we will use this class for H1

class Decision_Tree:

	def __init__(self, filename):

		csplit=main.csplit(self,filename)

		self.d_arr=csplit.d_arr
		self.name=csplit.name
		self.attributes=csplit.attributes
		self.train_values=csplit.train_values
		self.Class=csplit.Class

		self.Rnode=self.Heuristic(self.train_values, self.Class, self.attributes)

	def Heuristic(self, train_values,Class,Attributes):

		if len(train_values) == 0:
			return None

		Rnode=Calculate.Node(-1)
		Entropy=self.EntropyCalc(train_values,Class)
		variance=self.FindVariance(train_values,Class)
		Rnode.label=self.Counter(Class)
		if Entropy==0 or len(Attributes)==0:
			return Rnode

		else:
			

			Attr=self.VarianceImp(train_values,Class,Attributes,variance)

			if Attr==-1:
				return Rnode
			Rnode.node_value=Attr
			temp_atrr=[]
			for attribute in Attributes:
      
				if attribute !=Attr:
					temp_atrr.append(attribute)
			Attributes=temp_atrr
			temp_tree=self.Divide(train_values,Class,Attr)
			Rnode.left=self.Heuristic(temp_tree[0][0],temp_tree[0][1],Attributes)
			Rnode.right=self.Heuristic(temp_tree[1][0],temp_tree[1][1],Attributes)

			return Rnode

	
	def VarianceImp(self,train_values,Class,Attributes,variance):


		Attr,Maxgain=-1,-1

		for attribute in Attributes:
				V_Gain = self.VarianceGain(train_values, Class, variance, attribute)

				if V_Gain > Maxgain:
					Maxgain = V_Gain
					Attr = attribute
		return Attr

	def Counter(self, Class):

		if len(Class)==1:
			return Class[0]

		tc=0
		for i in range(len(Class)):
			if Class[i]==1:
				tc=tc+1

		if tc>=len(Class)/2:
			return 1
		else:
			return 0

	def Divide(self, train_values, Class, attribute):

		temp1,temp2,temp3,temp4=[],[],[],[]
		

		for i in range(len(train_values)):
			if self.d_arr[train_values[i]][attribute] == 0:
				temp1.append(train_values[i])
				temp3.append(Class[i])
				
			else:
				temp2.append(train_values[i])
				temp4.append(Class[i])

		return [(temp1,temp3),(temp2,temp4)]



	def EntropyCalc(self, train_values, Class):
		temp1,temp2=0,0


		
		tr=len(train_values)
		for i in range(len(train_values)):
			if Class[i] == 1:
				temp1=temp1+1 #increment temp1
			else:
				temp2=temp2+1
		if tr == 0 or temp1==0 or temp2==0:
			return 0

		


		plus= 1.0 *temp1/tr
		eksi=1-plus


		return -(plus*math.log(plus,2)+eksi*math.log(eksi,2))

	

	def FindVariance(self,train_values,Class):

		tr= len(train_values)
		temp1=0
		temp2=0
		temp3=0
		for i in range(len(train_values)):
		  if Class[i] == 1:
		      temp1=temp1+1
		  elif Class[i] == 0:
			  temp2=temp2+1
		
		
		if temp1 == 0 or temp2== 0:
			return 0
		ar=1.0*temp1/tr
		eksi= 1.0*temp2/tr
		
		return 	ar*eksi
	def VarianceGain(self,train_values,Class,variance,attribute):

		trRow= len(train_values)

		temp_tree=self.Divide(train_values,Class,attribute)
		variance1=self.FindVariance(temp_tree[0][0],temp_tree[0][1])
		variance2=self.FindVariance(temp_tree[1][0],temp_tree[1][1])


		num=1.0*len(temp_tree[0][0])/trRow
		temp=1-num

		V_Gain=variance -num* variance1 -temp*variance2
		return V_Gain


	

	

	def __str__(self):
            return self.PrintDecisionTree(self.Rnode,0,self.name)

	def PrintDecisionTree(self,Rnode,level,name):

		tree = ''
		if Rnode==None:
			return ''
		if Rnode.left==None and Rnode.right==None:
			tree=tree+ str(Rnode.label) + '\n'
			return tree
		currentNode=name[Rnode.node_value]

		depth=''
		for i in range(0,level):
			depth=depth+ '| '
		tree=tree+depth


		if Rnode.left!=None:
			if Rnode.left.left == None and Rnode.left.right == None:
				tree=tree+currentNode+ "= 0 :"
			else:
				tree=tree+currentNode+ "= 0 :\n"
		tree=tree+self.PrintDecisionTree(Rnode.left,level+1,name)


		tree=tree+depth
		if Rnode.right!=None:
			if Rnode.right.left ==None and Rnode.right.right==None:
				tree=tree+currentNode + "= 1 :"
			else:
				tree=tree+currentNode + "= 1 :\n"
		tree=tree+self.PrintDecisionTree(Rnode.right,level+1,name)

		return tree
