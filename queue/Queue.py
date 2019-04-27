
# class representing a node in the queue
class Node :

	def __init__(self , data) :
		self.data = data 
		self.next = None
		self.prev = None

# class containing the queue operations.
class Queue :

	def __init__(self , head=None , tail=None) :
		self.head = head
		self.tail = tail
		self.size = 0 

	# adds the data to the beginning of the queue
	def add_first(self , data ) :
		node = Node(data)
		
		if not self.head :
			self.head = node
			self.tail = node 
			self.size += 1 
		else :
			node.next = self.head
			self.head.prev = node
			self.head = node
			self.size += 1 
		return str(data)+' is inserted at beginning '

	# adds the data to the end of the queue 
	# if the queue is empty then it adds the data at the beginning
	def add_last(self , data ) :
		node = Node(data)
		
		if not self.tail :
			self.head = node
			self.tail = node 
			self.size += 1
			
		else :
			self.tail.next = node
			node.prev = self.tail
			self.tail = node
			self.size += 1

		return str(data) + ' is inserted at position ' + str(self.size)

	# removes the first elements of the queue
	def remove_first(self) :
		if self.head :
			temp = self.head 
			self.head = self.head.next
			if self.tail == temp :
				self.tail = None # if there was only one element in the queue
			else :
				self.head.prev = None
			self.size -= 1 
			return str(temp.data)+' at first is removed '
		else :
			return 'queue empty : no elements to remove '

	# removes the last element in the queueu
	def remove_last(self) :
		if self.tail :
			temp = self.tail 
			self.tail = self.tail.prev
			if self.head == temp :
				self.head = None # if there was only one element in the queue
			else :
				self.tail.next = None
			self.size -= 1	
			return str(temp.data)+' at the end is removed '
		else :
			return ' queue empty : no elements to remove '


	def queue_size(self) :
		return self.size

	# to display the queue state
	def display(self) :
		current = self.head
		queue_elements = []

		while current :
			queue_elements.append(current.data)
			current = current.next

		return queue_elements


class QueueAccess :

	def main() :
		queue = Queue()

		cont = 'y'

		while cont == 'y' :
			print(" Availabe operations are : \n\t 1.display \n\t 2.add_first \n\t 3.add_last \n\t 4.remove_first \n\t 5.remove_last \n\t 6.viewsize ")
			choice = input(' enter choice : ')
			if choice == '1' :
				print(queue.display())
			elif choice == '2' :
				data = input(' enter data : ') 	
				print(queue.add_first(data))
			elif choice == '3' :
				data = input(' enter data : ') 
				print(queue.add_last(data))
			elif choice == '4' :
				print(queue.remove_first())
			elif choice == '5' :
				print(queue.remove_last())
			elif choice == '6' :
				print(queue.queue_size())


			cont = input(' continue ? (y/n) : ')

	if __name__ == '__main__' :
		main()




