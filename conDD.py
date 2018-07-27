def dm(x):
    degrees = int(x) // 100
    minutes = x - 100*degrees
    print(degrees)
    print(minutes)
    return degrees, minutes

def decimal_degrees(degrees, minutes):
    	# print(degrees)
    	# print(minutes)
	t =  degrees + minutes/60
	print(t) 
#	return degrees + minutes/60
#print (decimal_degrees(*dm(0412.74943)))
