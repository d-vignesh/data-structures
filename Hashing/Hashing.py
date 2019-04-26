


# Hashing.py creates a hash table and store string based on the hash function ( ascii(first_char) * 100 + ascii(second_char) )


class HashTable (object) :
	def __init__(self) :
		self.table = [None] * 10000 # creating a list of size 10000 with values as None

	# stores the passed text in its corresponding bucket by calculating the hash value of the text
	# the text is inserted as a list so further strings with same hashvalue  can be appended in the bucket
	def store(self , text ) :
		hash_value = self.calculate_hash_value(text[:2])
		print(hash_value)
		if self.table[hash_value] == None :
			self.table[hash_value] = []
		self.table[hash_value].append(text)
		return text + ' is stored in bucket '+ str(hash_value) 

	# retrieves the text by calculating the hash value and searching in the corresponding hash value bucket 
	# returns 'no found' when the text couldn't be found in the bucket
	def lookup(self , text ) :
		hash_value = self.calculate_hash_value(text[:2])
		if(self.table[hash_value] != None) :
			for val in self.table[hash_value] :
				if val == text :
					return val + ' is present in bucket '+ str(hash_value)
		return ' no found '

	# calculates the hash value of the text using the hash function
	# converts the char to ascii using the ord() method and returns the hash value
	def calculate_hash_value(self , text ) :
		return ord( text[0]) * 100 + ord( text[1])

# class to create object for the HashTable class and access its methods based on the users choice
class HashTableAccess (object) :
	
	def main() :
		hash_table = HashTable()

		cont = 'y'

		while cont == 'y' :
			print( ' availabe operation : \n\t1.store \n\t2.lookup')
			choice = input(' enter your choice : ')
			if choice == '1' :
				text = input(' enter the text to be hashed : ')
				print(hash_table.store(text))

			else :
				text = input(' enter the text to be lookedup : ')
				print(hash_table.lookup(text))

			cont = input( ' continue ? (y/n) : ')

	if __name__ == '__main__' : 
		main()
