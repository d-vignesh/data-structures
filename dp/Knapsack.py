
'''
	python program to implement the knapsack problem.
	a knapsack problem is : given a knapsack with weight capacity W and a set of objects with value v and weigth w , 
							find a subset of the object set the combined values of which has max possible value and combined weight 
							is less than or equal to W ( uses dynamic programming tech memoziation)

'''

class Knapsack(object):


	def compute_max_value(self, value_list, weight_list, weight_capacity):

		list_len = len(weight_list)
		
		# construct the matric to store the sub results and fill in the known cases.
		look_up = [[0 for col in range(weight_capacity+1)] for row in range(list_len)]
		for row in look_up:
			print(row)

		# the possible weight when only 0 weight allowed is 0
		for i in range(list_len):
			look_up[i][0] = 0 

		# the possible weight when only one object is present
		for i in range(weight_capacity):
			if weight_list[0] <= i:
				look_up[0][i] = value_list[0]
			else:
				look_up[0][i] = 0 


		for i in range(1, list_len):
			for j in range(1, weight_capacity+1):
				if weight_list[i] <= j:
					look_up[i][j] = max( value_list[i] + look_up[i-1][j-weight_list[i]] , look_up[i-1][j])
				else :
					look_up[i][j] = look_up[i-1][j]

		for row in look_up:
			print(row)



		print(look_up[list_len-1][weight_capacity])


class KnapsackAccess(object):

	def main():
		knapsack = Knapsack()
		value_list = [1, 4, 5, 7]
		weight_list = [1, 3, 4, 5]
		weight_capacity = 7

		knapsack.compute_max_value(value_list, weight_list, weight_capacity)

	if __name__ == '__main__':
		main()
