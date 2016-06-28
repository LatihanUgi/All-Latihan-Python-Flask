class Node:
	def __init__(self,node,data):
		self.node = node
		self.data = data

def jelajahNode(node):
	print(node.data)
	if(node.node!=None):
		jelajahNode(node.node)
		
node = Node(Node(Node(Node(None,8),7),6),5)
jelajahNode(node)