def star(func):
	def inner():
		print ("**********")
		func()
		print ("**********")
	return inner

def per(func):
	def inner():
		print ("%%%%%%%%%%%%%%%%")
		func()
		print ("%%%%%%%%%%%%%%%%")
	return inner


@per
@star
def hai():
	print ("hai")

hai()