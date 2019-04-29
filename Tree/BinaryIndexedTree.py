
# reference : 
# https://www.topcoder.com/community/competitive-programming/tutorials/binary-indexed-trees/
# https://www.youtube.com/watch?v=v_wj_mOAlig

# binary indexed tree is used for storing the prefix sum information of a array.
# this tree is suitable for the following problem
# 	- we have a array of elements and we have multiple query which is either to get sum of a range of index or update a
# 		element in any index, that has to be performed on the array.
#  - it can be solved using for loop or a prefix sum array , but these methods would take O(n) to compute sum and update respectively
# binary indexed tree approach will take O(log n) for both compute sum and update operations.

# BASIC IDEA :

#  basic idea behind BIT is that all numbers can be represented as a power of 2. also a cumulative frequency can be represented
#   as a sum of sets of subfrequencies.
#  an index idx is responsible for the cumulative sum of indices from (idx - 2 ^ r + 1) to idx, where r is the position of
#  	last set bit in binary representation of idx (e.g.,) idx = 4 (0100) => 4 - 2 ^ 2 + 1 = 0, which mean index 4 is 
#  	responsible for the sum of indices from [0-4]
#  so here we need the last set bit. this can be obtained by doing idx & (-idx)
#  i.e., idx -= idx & (-idx) will move idx to the previous index whose sum is not included in the cumulative sum in idx
#  similarly idx += idx & (-idx) will move idx to next index whose sum is not included in the cumulative sum in idx


class BinaryIndexedTree(object):

	def __init__(self, n):

		self.bi_tree = [0] * (n + 1)
		self.size = n

	def construct_BIT(self, arr):

		for ind, val in enumerate(arr):
			self.update_BIT(ind, val)

	def update_BIT(self, ind, val):

		# the indexing in BIT starts from 1. so increment the index.
		ind = ind + 1

		while(ind <= self.size):

			self.bi_tree[ind] += val

			# logic to get the next index which contains the updated index in its subfrequency
			# eg., if we start with index 1 then adding the last set bit will move to index 2
			# then adding the last set bit to 2 will give the index 4. 
			ind += ind & (-ind)

	def get_sum(self, ind):

		sum = 0
		ind = ind + 1

		while(ind > 0 ):

			sum += self.bi_tree[ind]

			# logic to get the last set bit and subtract it to the current index to get the previous index
			# eg., index 4 is reponsible for sum from [1-4]
			# so if we apply this logic to index 4, we get ( 4 -= 4 & 4) => 0 .
			ind -= ind & (-ind)

		return sum


	def read_single(self, ind):
		'''
			returns the actual frequency of at given index.
		'''

		# we will only have the cumulative frequency at the index
		# so in order to get the actual frequency at the index, we reduce the cumulative sum with all the 
		# overlapping index's frequencies until they reach any equal index.
		# e.g., consider we need the frequency at index 12, index 12 will hold the cumulative sum of 
		# index 9, 10, 11 and 12. so we subtract the sum with value at 11, 10 to get the actual freqency at 12

		ind += 1
		sum = bi_tree[ind]

		overlapping_ind = ind - ( ind & -ind)
		ind -= 1

		while(ind != overlapping_ind):
			sum -= bi_tree[ind]
			ind -= ind & -ind

		return sum

class Driver(object):

	def main():

		arr = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
		tree = BinaryIndexedTree(len(arr))

		tree.construct_BIT(arr)
		print(f'sum of first 5 elements : {tree.get_sum(4)}')

		tree.update_BIT(3, 6)
		print(f'sum of first 5 elements : {tree.get_sum(4)}')

	if __name__ == '__main__':
		main()