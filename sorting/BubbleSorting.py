

def bubble_sort(list) :

	for i in range(len(list) -1 ) :
		for j in range(( len(list) -1 ) - i  ):
	
			if list[j] > list[j+1] :
				temp = list[j] 
				list[j] = list[j+1] 
				list[j+1] = temp


list = [5,4,3,2,1]
bubble_sort(list)
print(list)