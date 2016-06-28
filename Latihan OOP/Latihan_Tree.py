class Tree:
	def __init__(self,kiri,kanan,data):
		self.kiri = kiri
		self.kanan = kanan
		self.data = data
		
def inOrder(tree): #algoritma InOrder traversing
	if(tree.kiri!=None):
		inOrder(tree.kiri)
	print (tree.data)
	if(tree.kanan!=None):
		inOrder(tree.kanan)

root = Tree(Tree(None,None,3),Tree(None,None,10),5)
inOrder(root)