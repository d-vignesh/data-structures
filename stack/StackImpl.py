

# class to represent a node with data and a address attributes
class Node :
	def __init__( self , data ) :
		self.data = data 
		self.next = None


class StackOperation :

	# constructor of the StackOperation class . it initializes the top of the stack to none initially as there will be no elements 
	def __init__( self , top=None ) :
		self.top = top # ptr to keep track of the recently added element
		self.size = 0 # variable to keep track of the size of the stack

	# used to insert an element into the stack
	# creates a node with the given element 
	# insert the node at beginning and makes it as top of stack
	def push(self , data) :
		node = Node(data)

		node.next = self.top
		self.top = node
		self.size += 1 
		return str(data) + " inserted at top "

	# used to remove the top element of the stack
	# it does it by just referencing the top ptr to the second top element of the stack and thus dereferencing the current top element
	def pop(self) :
		if self.top :
			data = self.top.data
			self.top = self.top.next
			self.size -= 1
			return str(data) + " is removed from the stack "
		else :
			return " the stack is empty "


	# used to display the state of the stack
	# iterates through all elements in the stack and returns a list of the data's 
	def display(self) :
		if self.top :
			current = self.top 
			data_list = []
			while current :
				data_list.append(current.data)
				current = current.next
			return data_list
		else :
			return ' the stack is empty '

	# returns the current size of the stack
	def stack_size(self) :
		return self.size


# utility class that gets the input from user and calls the respective stack operations.
class StackImpl :
		

	def main() :
		stack = StackOperation()
		cont = 'y'
		while cont == 'y' or cont =='Y' :
			print ( ' enter your choice \n\t 1.push \n\t 2.pop \n\t 3.display \n\t 4.view size ')
			choice = input(' enter your choice : ')
			if choice == '1' :
				data = input(' enter data to push : ')
				status = stack.push(data)
				print (status)
			elif choice == '2' :
				status = stack.pop()
				print(status)
			elif choice == '3' :
				status = stack.display()
				print(status)
			elif choice == '4' :
				status = stack.stack_size()
				print(status)

			cont = input(' continue ? (y/n) : ')

	if __name__ == '__main__' :
		main()