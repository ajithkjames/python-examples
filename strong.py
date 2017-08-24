
def factorial(num):
	fact=1
	for i in range(1,num+1):
		fact=fact*i
	return fact
	
for i in range(99999):
	digit=str(i)
	facts=[factorial(int(i)) for i in digit]
	if sum(facts)==i:
		print (i)

