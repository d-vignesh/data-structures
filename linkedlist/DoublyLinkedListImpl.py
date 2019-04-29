

class Node :
	def __init__(self , data , prev=None , next=None ) :
		self.data = data 
		self.prev = prev
		self.next = next


class DoublyLinkedListImpl :
	def __init__( self , head= None) :
		self.head = head 

	def add_to_end(self , data) :
		node = Node(data)

		if not self.head :
			self.head = node 
			return str(data) + " is inserted as head "
		else :
			current = self.head
			counter = 1

			while current.next :
				current = current.next
				counter += 1

			current.next = node
			node.prev = current
			return str(data) + " is inserted at end at " + str(counter+1)

	def add_to_beginning(self , data) :
		node = Node(data)

		if not self.head :
			self.head = node
			return str(data) + " is inserted as head "
		else :
			node.next = self.head
			self.head.prev = node
			self.head = node
			return str(data) + " is inserted at beginning "

	def display(self):
		current = self.head
		data_list = []

		while current :
			data_list.append(current.data)
			current = current.next

		print(data_list)

	def search(self , search_data) :
		if not self.head :
			return ' list is empty '
		current = self.head
		counter = 1

		while current and current.data != search_data :
			current = current.next
			counter += 1

		if current :
			return str(search_data) + " is found in position "+ str(counter)
		else :
			return str(search_data) + ' is not found '

	def delete(self , delete_data ):
		if not self.head :
			return ' list is empty '

		current = self.head
		counter = 1 
		while current.next and current.data != delete_data :
			current = current.next
			counter += 1

		if current :
			current.prev.next = current.next
			current.next.prev = current.prev
			return str(delete_data) + ' is deleted at position ' + str(counter)
		else :
			return str(delete_data) + ' not found '



class DoublyLinkedListTest :

	def main() :

		cont = 'y'
		doublyll = DoublyLinkedListImpl()
		while ( cont == 'y' or cont == 'Y') :
			print( ' available operations \n\t 1.display \n\t 2.add_to_beginning \n\t 3.add_to_end \n\t 4.search \n\t 5.delete')
			choice = input( ' enter choice : ')
			if choice == '1' :
				doublyll.display()
			elif choice == '2' :
				data = input(' enter node data : ')
				status = doublyll.add_to_beginning(data)
				print(status)
			elif choice == '3' :
				data = input(' enter node data : ')
				status = doublyll.add_to_end(data)
				print(status)
			elif choice == '4' :
				search_data = input(' enter data to search : ')
				status = doublyll.search(search_data)
				print(status)
			elif choice == '5' :
				delete_data = input(' enter data to delete : ')
				status = doublyll.delete(delete_data)
				print(status)

			cont = input(' want to continue ? (y/n) : ')


	if __name__ == '__main__' :
		main()