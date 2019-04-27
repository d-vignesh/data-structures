

def fibanocci(n , list , first , second ) :

	if ( n <= 0 ) :
		return None 

	third = first + second
	first = second
	second = third	
	list.append(third)
	fibanocci( n-1 , list , first , second )
	return None


list = []
fibanocci(10 , list , 0 , 1 )
print(list)