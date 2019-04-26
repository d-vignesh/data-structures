

# the time complexity of binary search in O( log n )
# it is calculated as how many times n can be divied by 2
#  		n / 2^x = 1
#	=>  n = 2^x
#   =>  log2 n = log2 2^x
#	=>  log2 n = x log2 2
#   =>  log2 n = x 

# use binar search only if there is a requirement for many search operation
# because it requires the array to be sorted and hence sorting for a single search in inefficient

# the worst case scenario can be obtained by search for a element that is not in the list

class BinarySearch :

	def binary_search(self , list , key , start , end ) :

		while ( start <= end ) :

			# print ('index : 0\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14')
			# print ('list  : 1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15')
			# print (' start is : '+ str(start))
			# print (' end is : '+ str(end))

			mid = int( (start + end ) / 2 )
			# print(' mid is : '+ str(mid) )

			if list[mid] == key :
				return str(key) + ' is present in index ' + str(mid)

			if list[mid] > key :
				end = mid-1
			else :
				start = mid+1

		return str(key) + ' is not found '


class BinarySearchAccess :

	def main() :
		b_search = BinarySearch()

		print('binary search : ')
		arr = [1, 12, 3, 14, 10, 6, 7, 8, 15, 5, 11, 2, 13, 4, 9]
		key = input(' enter element to search : ')
		arr.sort()

		print(b_search.binary_search(arr , int(key) , 0 , 13 ))


	if __name__ == '__main__' :
		main()