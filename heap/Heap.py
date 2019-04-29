
# python implementation of min heap data structure.

class Heap :

	def __init__(self, capacity) :

		self.heap = [None] * capacity
		self.heap_size = 0 
		self.capacity = capacity


	def insert(self, value):

		if self.heap_size >= self.capacity :
			return ' the heap is filled '
		else :
			return self._insert(value)


	def _insert(self, value):
		'''
			ADDS THE VALUE TO THE HEAP AND CALLS THE restore_heap_prop()
			TO CHECK WETHER THE ADDITION OF ELEMENT VIOLATES THE HEAP PROPERTY
		'''
		self.heap[self.heap_size] = value
		self.restore_heap_prop(self.heap_size)
		self.heap_size += 1
		return ' element is inserted '


	def parent(self, index):
		return int(( (index+1) /2) - 1 )


	def right_child(self, index):
		return (index * 2) + 2


	def left_child(self, index):
		return (index * 2) + 1


	def swap(self, index1, index2):
		temp = self.heap[index1]
		self.heap[index1] = self.heap[index2]
		self.heap[index2] = temp



	#  CHECKS WETHER THE HEAP PROPERTY IN VIOLATED AND FIX IT IF VIOLATED
	def restore_heap_prop(self, index):
		while( index != 0 and self.heap[self.parent(index)] > self.heap[index]) :
			print(f' swapping {self.heap[self.parent(index)]} by {self.heap[index]}')
			self.swap( self.parent(index) , index )
			index = self.parent(index)


	def decrease_key(self, index, value):
		'''
			INPUT : THE INDEX OF THE ELEMENT , THE VALUE TO WHICH THE ELEMENT TO BE DECREATED
			RETURNS : STRING VALUE ACKNOWLEDGING THE STATUS OF INSERTION OF ELEMENT
			OPERATION : DECREASES THE VALUE OF A GIVEN NODE TO THE VALUE PASSED AS THE PARAMETER
		'''

		if index >= self.heap_size or index < 0 :
			return f' invalid index , the heap size is 0 to { self.heap_size-1 }'
		else :
			return self._decrease_key(index, value)

	def _decrease_key(self, index, value):
		

		self.heap[index] = value 
		self.restore_heap_prop(index)
		return ' the value is decreased '

	def get_min_element(self):
		'''
			INPUT : NONE
			OUTPUT : MIN ELEMENT ( ROOT ) ELEMENT OF THE HEAP
			OPERATION : RETURNS THE MIN ELEMENT OF THE HEAP IF EXISTS
		'''

		if self.heap_size == 0 :
			return ' heap empty '
		else :
			return self.heap[0]

	def delete_min_element(self):
		'''
			INPUT : NONE 
			OUTPUT : THE MINIMUN ELEMENT OF THE HEAP
			OPERATION : RETURNS THE MIN ELEMENT OF THE HEAP IF EXISTS
						UNLIKE get_min_element() THIS METHOD REMOVE THE 
						MIN_ELEMENT FROM THE HEAP BEFORE RETURNING
		'''

		if self.heap_size == 0 :
			return ' heap empty '
		elif self.heap_size == 1 :
			self.heap_size -= 1
			return self.heap[self.heap_size]
		else :
			return self._delete_min_element()

	def _delete_min_element(self):

		temp = self.heap[0]
		self.heap_size -= 1
		self.heap[0] = self.heap[self.heap_size]
		self.min_heapify(0)
		return f' min element removed is {temp} '

	def min_heapify(self, index):
		'''
			INPUT : AN INDEX FROM WHICH MIN HEAPIFY SHOULD HAPPEN , USUALLY THE ROOT OF THE SUBTREE 
			RETURNS : NONE
			OPERATION : RESTORES THE HEAP PROPERTY FOR THE SUBTREE 
		'''

		left_child = index * 2 + 1
		right_child = index * 2 + 2 

		smallest = index 

		if left_child < self.heap_size and self.heap[left_child] < self.heap[smallest]:
			smallest = left_child
		if right_child < self.heap_size and self.heap[right_child] < self.heap[smallest]:
			smallest = right_child

		if smallest != index :
			self.swap(smallest, index)
			self.min_heapify(smallest)



	def print_heap(self):
		if self.heap_size <= 0 :
			print(' heap is empty ')
		else :
			self._print_heap()

	def _print_heap(self):
		print(self.heap)



class HeapAccess :

	def main():

		cap = int(input( ' enter the size of heap : '))
		heap_obj = Heap(cap)

		cont = 'y'
		print(' implementation of heap data structure  ')

		while( cont == 'y' ):
			print(' available operations : \n\t 1.insert \n\t 2.deleteMin \n\t 3.getMinele  \n\t 4.decreasekey \n\t 5.print_heap')
			choice = input(' enter your choice : ')
			if choice == '1' :
				value = input(' enter the value to insert : ')
				print(heap_obj.insert(value))
			elif choice == '2':
				print(heap_obj.delete_min_element())
			elif choice == '3':
				print( heap_obj.get_min_element())
			elif choice == '4':
				index, value = input( ' enter the index and the decreased value of the element ').split()
				print(heap_obj.decrease_key( int(index), value) )
			elif choice == '5' :
				heap_obj.print_heap()

			cont = input( ' do you want to continue ? (y/n) : ')


	if __name__ == '__main__':
		main()

