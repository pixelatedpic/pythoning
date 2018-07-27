def dm(x):
    degrees = int(x) // 100
    minutes = x - 100*degrees
    #print(degrees)
    #print(minutes)
    conval =  degrees + minutes/60
    return conval
#r = dm(07332.48362)
#print(r)
#def decimal_degrees(degrees, minutes):
#    print(degrees)
#    print(minutes)
#    t =  degrees + minutes/60
#    print(t) 
#	return degrees + minutes/60
#print (decimal_degrees(*dm(0412.74943)))
#dm(07332.48362)
#decimal_degrees(73,32.483619)
