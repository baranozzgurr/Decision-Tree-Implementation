import main
#import csv


class Node: #constracting nodes
     def __init__(self,node_value,left=None,right=None):
       self.left=left
       self.right=right
       self.label=-1
       self.node_value=node_value

class Set_accuracy:
	def __init__(self,filename):
		csplit =main.csplit(self,filename)
		self.d_arr=csplit.d_arr
		self.Class=csplit.Class
    
		#self.accsave=accsave

	def FindAcc(self,Rnode):

		if Rnode==None or len(self.d_arr)==0:
			return 0
		num = 0
		for i in range(0,len(self.d_arr)):
			if self.construct(Rnode,self.d_arr[i])==self.Class[i]:
				num=num+1

		self.accuracy=1.0*num/len(self.d_arr)        
		return self.accuracy

	def construct(self,Rnode,dr):  
        
		if Rnode!=None:
			if Rnode.node_value==-1:
				return Rnode.label
			if dr[Rnode.node_value]==0:
				return self.construct(Rnode.left,dr)
			else:
				return self.construct(Rnode.right,dr)

	def displayAccuracy(self):
		print str((self.accuracy)*100)+"%"

