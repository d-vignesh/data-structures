
'''
	python class to find the longest common subsequence between two given strings.

'''

class LCS:

	def compute_lcs(self, str1, str2):
		# construct the memoziation matrix
		memo_mat = [['' for col in range(len(str2)+1)] for row in range(len(str1)+1)]

		max_len_lcs = ''

		# loop throught the strings and update the memo_mat
		for i in range(1, len(str1)+1):
			for j in range(1, len(str2)+1):

				# case 1 : if both the character of the strings are equal.
				# the lcs will be the lcs formed without this character(i,e. memo[i-1][j-1]) + current_char
				if str1[i-1] == str2[j-1]:
					memo_mat[i][j] = memo_mat[i-1][j-1] + str1[i-1]
					if len(memo_mat[i][j]) > len(max_len_lcs):
						max_len_lcs = memo_mat[i][j] 

				# case 2 : if both the characters are not equal.
				# then lcs would be the max ( lcs formed by omitting str1 char and taking str2 char i.e., memo[i-1][j] , 
				#    						  lcs formed by omitting str2 char and taking str1 char i.e., memo[i][j-1] )

				else:
					memo_mat[i][j] = memo_mat[i-1][j] if len(memo_mat[i-1][j]) > len(memo_mat[i][j-1]) else memo_mat[i][j-1]


		for row in memo_mat :
			print(row)

		print(f'\n\n\t lcs is : {memo_mat[len(str1)][len(str2)]}')

		

class LCSAccess :
	def main():
		lcs = LCS()
		#str1 = 'breakfast i had tooday was awsome'
		#str2 = 'the breakfast i had today was awesome'
		str1 = 'abcdef'
		str2 = 'cdefghi'
		lcs.compute_lcs(str1, str2)

	if __name__ == '__main__':
		main()