

# time complexity of linear search is O(n)
# it has to iterate through the entire list in worst case


class LinearSearch :

	def linear_search(self , list , key ) :
		for index in range(0,len(list)) :
			if key == list[index]:
				return str(key) + ' is present at index ' + str(index) 

		return str(key) + ' is not found '


class LinearSearchAccess :

	def main():
		lin_sch = LinearSearch()

		print(' binary search : ')
		list = [1, 2, 3, 4, 5, 6, 7]
		print('list is : ')
		print(list)
		key = int(input('enter key to search'))
		print(lin_sch.linear_search(list , key))

	if __name__ == '__main__' :
		main()
