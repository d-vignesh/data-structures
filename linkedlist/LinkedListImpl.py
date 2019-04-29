

class Node :
	def __init__( self , data ):
		self.data = data 
		self.next = None


class LinkedList :
	def __init__( self , head=None ):
		self.head = head


	def add_to_beginning( self , new_data ):
		node = Node(new_data)
		node.next = self.head
		self.head = node

	def add_to_end( self , new_data ):
		node = Node(new_data)
		if self.head == None :
			self.head = node
		else :
			current = self.head
			while current.next :
				current = current.next
			current.next = node 

	def search( self , search_data ):
		if self.head == None :
			return " empty list "
		counter = 1 
		current = self.head
		while current :
			if current.data == search_data :
				return search_data +" is in position "+str(counter)
			counter += 1
			current = current.next 
		return "no such data "

	def delete( self , data_to_delete ):
		if self.head == None :
			return " empty list "
		counter = 0
		current = self.head
		while current.next :
			counter += 1
			if current.next.data ==data_to_delete :
				current.next = current.next.next
				return data_to_delete + " in position " + str(counter) + " is deleted "
			current = current.next
		return " no such element "

	def insert( self , position , new_data ):
		if self.head == None and position > 1 :
			return "empty list "
		counter = 1
		current = self.head
		while counter + 1 < position and current.next :
			counter += 1
			current = current.next
		if current.next :
			node = Node(new_data)
			node.next = current.next
			current.next = node
			return new_data + " is inserted at "+ str(counter+1)
		return " invalid position :" + str(position) +" given position exceed link list size : "+str(counter)



	def display(self):
		current = self.head
		node_list = []
		while current :
			node_list.append(current.data)
			current = current.next
		return node_list



class LinkedListTest :

	def main() :

		list_obj = LinkedList()
		cont = "Y"
		while cont == "Y" or cont == "y" :
			print( " available operation : \n\t 1 . display list \n\t 2 . add node to beginning \n\t 3 . add node to end \n\t 4 . search data \n\t 5 . delete \n\t 6 . insert ")
			choice = input(" enter option : ")
			if choice == "1" :
				node_list = list_obj.display()
				print (node_list)
			elif choice == "2" :
				data = input(" enter node's data : ")
				list_obj.add_to_beginning(data)
			elif choice == "3" :
				data = input(" enter node's data : ")
				list_obj.add_to_end(data)
			elif choice == "4" :
				search_data = input(" enter data to search : ")
				print(list_obj.search( search_data ))
			elif choice == "5" :
				data_to_delete = input(" enter data to delete : ")
				print(list_obj.delete(data_to_delete))
			elif choice == "6" :
				data_to_insert = input(" enter data to insert : ")
				position = input(" enter position to insert : ")
				print(list_obj.insert(int(position) , data_to_insert))
			cont = input(" continue ? (y/n) : ")




	if __name__ == "__main__":
		main()

