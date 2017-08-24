# a=input("enter the sentance : ")
# if a[::-1]==a:
# 	print (True)
# else:
# 	print (False)

num=int(input("enter the number: "))
temp=num
a=0
while(num!=0):
	a=num%10 + a*10
	num=num//10
if temp==a:
	print ("yes")
else:
	print("no")