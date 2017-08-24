print ("hai")
class FindAmstrongNumbers(object):

	def amstrong():
		for i in range(1,10000):
			pows=[int(a)**len(str(i)) for a in str(i)]
			if sum(pows)==i:
				print (i)
FindAmstrongNumbers.amstrong()