'''
	python script to implement and understand the components and functionalities of a binarh search tree data structure

'''

class Node(object) :
	def __init__( self, value ) :
		
		self.value = value
		self.right = None 
		self.left = None


class Tree(object) :

	def __init__(self) :
		
		self.root = None


	def add( self, value) :
		
		if self.root == None :
			self.root = Node(value)
		else :
			node = self.root
			self._add( node, value)


	def _add( self, node, value) :
		
		if value < node.value :
			if node.left == None :
				node.left = Node(value)
			else :
				self._add( node.left, value)
		else :
			if node.right == None :
				node.right = Node(value)
			else :
				self._add( node.right, value)


	def find( self, value) :
		
		if self.root == None :
			return ' tree is empty '
		else :
			node = self.root
			return self._find( node, value)

    
    
	def _find( self, node, value) :
		
		if node != None :
			if value == node.value :
				return ' the value exists '
			elif value < node.value :
				return self._find( node.left, value)
			else :
				return self._find( node.right, value)
		return ' element does not exists '

    
	def height( self) :
		
		if self.root == None :
			return 0 
		else :
			node = self.root 
			return self._height( node, 0)

	
	def _height( self, node, h):
		
		if node == None :
			return h
		left_height = self._height( node.left, h+1 )
		right_height = self._height( node.right, h+1)
		return max( left_height, right_height)


	
	def min_element( self ):
		
		if self.root == None :
			return ' tree is empty '
		else :
			node = self.root
			return self._min_element( node )

	
	def _min_element( self, node):
		
		if node.left == None :
			return node.value
		return self._min_element( node.left)

	
	def max_element( self ):
		
		if self.root == None :
			return ' tree is empty '
		else :
			node = self.root
			return self._max_element( node )

	
	def _max_element( self, node):
		
		if node.right == None :
			return node.value
		return self._max_element( node.right )

	
	def delete(self, value ) :
		
		if self.root == None :
			return ' tree is empty'
		else :
			node = self.root
			self.root = self._delete(node, value)

	
	def _delete( self, node, value) :
		
		if node == None :
			return None
		elif value < node.value :
			node.left = self._delete(node.left, value)
		elif value > node.value :
			node.right = self._delete(node.right, value)
		else :
			if node.left == None and node.right == None :
				print(' deleting the element ')
				return None
			elif node.left != None and node.right != None :
				node.value = self._min_element(node.right)
				node.right = self._delete(node.right , node.value)
			else :
				print(' deleting the element ')
				if node.left != None :
					return node.left 
				else :
					return node.right
		return node


	def print_tree(self):
		
		if self.root == None :
			print(' tree is empty ')
		else :
			node = self.root 
			self._print_tree( node)
			print()


	def _print_tree( self, node):
		
		if node != None :
			self._print_tree( node.left)
			print(node.value , end=' , ')
			self._print_tree( node.right)


	def top_view(self):
		
		if self.root == None :
			print('tree is empty')
		else :
			node = self.root
			# a dictionary to store the first appearing element in each level
			levels_viewed = {}
			self._top_view(node, levels_viewed, level=0)

		return levels_viewed

	def _top_view(self, node, levels_viewed, level):
		
		if node == None :
			return 
		if level not in levels_viewed:
			levels_viewed[level] = node.value

		# consider the left sub tree as '-'ve levels and right sub tree as '+'ve levels. hence level-1 for
		# next level left and level+1 for next level right
		self._top_view(node.left, levels_viewed, level-1)
		self._top_view(node.right, levels_viewed, level+1)


	def right_view(self):
		
		if self.root == None:
			print('tree is empty')
		else:
			levels_viewed = {}
			node = self.root
			self._right_view(node, levels_viewed, level=0)

		return levels_viewed


	def _right_view(self, node, levels_viewed, level):

		if node == None:
			return
		if level not in levels_viewed:
			levels_viewed[level] = node.value
		self._right_view(node.right, levels_viewed, level+1)
		self._right_view(node.left, levels_viewed, level+1)

		return


	def left_view(self):
		
		if self.root == None:
			print('tree is empty')
		else:
			levels_viewed = {}
			node = self.root
			self._left_view(node, levels_viewed, level=0)

		return levels_viewed


	def _left_view(self, node, levels_viewed, level):

		if node == None:
			return
		if level not in levels_viewed:
			levels_viewed[level] = node.value
		self._left_view(node.left, levels_viewed, level+1)
		self._left_view(node.right, levels_viewed, level+1)

		return
		

class TreeAccess(object) :
	
	def main() :
		
		tree = Tree()
		cont = 'y'

		while cont == 'y' :
			print( ''' avaialbe operations : \n\t 1.add \n\t 2.find \n\t 3.height \n\t 4.min_element  
					                         \n\t 5.max_element \n\t 6.print \n\t 7.delete \n\t 8.top_view 
					                         \n\t 9.right_view \n\t 10.left_view''')
			choice = input(' enter you choice : ')
			if choice == '1' :
				value = input(' enter value for node : ')
				tree.add(value)
			
			elif choice =='2' :
				value = input(' enter value to find : ')
				print(tree.find(value))
			
			elif choice =='3' :
				print(tree.height())
			
			elif choice =='4' :
				print(' min element is ' + tree.min_element())
			
			elif choice =='5':
				print(' max element is ' + tree.max_element())
			
			elif choice =='6':
				tree.print_tree()
			
			elif choice =='7':
				value = input(' element to delete : ')
				tree.delete(value)
			
			elif choice =='8':
				top_view = tree.top_view()
				print('top view : ')
				for level in top_view:
					print(top_view[level], end=' ')
				print()
			
			elif choice =='9':
				right_view = tree.right_view()
				print('right view : ')
				for level in right_view:
					print(right_view[level], end=' ')
				print()

			elif choice =='10':
				left_view = tree.left_view()
				print('left view :')
				for level in left_view:
					print(left_view[level], end=' ')
				print()

			cont = input(' continue ? (y/n) : ')

	if __name__ == '__main__' :
		main()



