
'''
	python class to find longest common subsequence of two string using recursion and memoziation.
'''

class LCSReMemo (object):

	def compute_lcs(self, str1, str2):
		memo = [[None for col in range(len(str2))] for row in range(len(str2))]

		print(self._compute_lcs(str1, str2, 0, 0, memo))

	def _compute_lcs(self, str1, str2, i, j, memo):

		# base case : end of any string
		if (i == len(str1) or j == len(str2)):
			return ''

		# case 1 : if both chars are equal
		if (str1[i] == str2[j]):
			if memo[i][j] == None :
				memo[i][j] = str1[i] + self._compute_lcs(str1, str2, i+1, j+1, memo)
			return memo[i][j]

		else :
			result = ''

			resultA = self._compute_lcs(str1, str2, i+1, j , memo)
			resultB = self._compute_lcs(str1, str2, i , j+1, memo)

			if len(resultA) > len(resultB):
				result = resultA
			else :
				result = resultB

			memo[i][j] = result
			return result


class LCSRecurseAccess :
	def main():
		lcs = LCSReMemo()
		str1 = 'breakfast i had tooday was awsome'
		str2 = 'the breakfast i had today was awesome'
		#str1 = 'abcd'
		#str2 = 'afkd'
		lcs.compute_lcs(str1, str2)

	if __name__ == '__main__':
		main()