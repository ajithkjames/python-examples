for i in range(1,1000):
	sumof=sum([a for a in range(1,i+1) if i%a==0 ])
	if i==sumof/2:
		print (i)
