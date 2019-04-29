

class MergeSort :



	def sort_and_merge( self , list , start , mid , end ) :
		# print( '						merging the portion with start - %s mid - %s end - %s ' % ( start , mid , end ))
		left_sub_list = list[start:mid+1]
		right_sub_list = list[mid+1:end+1]

		left_len = ( mid+1 ) - start 
		right_len = end - mid 

		# print( ' 						left sub list is ' + str(left_sub_list ) )
		# print( ' 						right sub list is ' + str(right_sub_list ) )

		i = j = 0 
		k = start 

		while i < left_len and j < right_len :
			if ( left_sub_list[i] < right_sub_list[j]) :
				list[k] = left_sub_list[i] 
				i += 1
			else :
				list[k] = right_sub_list[j]
				j += 1 
			k += 1 

		if i < left_len :
			while i < left_len :
				list[k] = left_sub_list[i]
				i += 1
				k += 1


		if j < right_len :
			while j < right_len :
				list[k] = rigth_sub_list[j]
				j += 1
				k += 1

		# print(list)
		# print('*' * 10 )


	def divide ( self , list , start , end ) :
		if ( start < end ) :
			mid = ( start + end ) 
			# print( 'left divide start - %s mid - %s ' % (start , mid ))
			self.divide(list , start , mid) 
			# print( 'right divide mid - %s end - %s ' % ( mid+1 , end ))
			self.divide(list , mid+1 , end) 
			self.sort_and_merge( list , start , mid , end)



	def sort(self , list ):
		self.divide( list , 0 , len(list) - 1 )
		return list




class MergeSortAccess :
	
	def main() :
		mergeSort = MergeSort()
		list = [ 6, 5, 4, 3, 2, 1 ]
		mergeSort.sort(list)


	if __name__ == '__main__' : 
		main()