class KeyIndex:
	k = []
	pos = 0
	def __init__(self,a):
		min = self.Min_finder(a)
		if min<0:
			self.pos = - min
			for x in range(len(a)):
				self.k.append(a[x]+self.pos)
		else:
			for x in a:self.k.append(x)
		max = self.Max_finder(self.k)
		aux = [0]* (max + 1)
		for l in self.k:
			aux[l] += 1
		self.k = aux

	def search(self,value):
		check = False
		if value<len(self.k) and self.k[value]>0:
			check = True
		return check

	def sort(self):
		for x in range(len(self.k)):
			if self.k[x] != 0:
				for y in range(self.k[x]):
					print((x-self.pos),end = " ")

	def Max_finder(self,a):
		max = a[0]
		for x in a:
			if(x > max):
				max = x
		return max
	def Max_finder(self,a):
		max = a[0]
		for x in a:
			if(x > max):
				max = x
		return max

	def Min_finder(self,a):
		min = a[0]
		for x in a:
			if(x < min):
				min = x
		return min

class HashTable:
	def hash_func(self,data):
		vowel = ["A","E","I","O","U"]
		digit = ['0','1','2','3','4','5','6','7','8','9']
		aux = [None]*len(data)
		for item in data:
			total = 0
			con_count = 0
			for letters in item:
				if letters in digit:
					total += int(letters)
				elif  letters not in vowel:
					con_count +=1
			value = ((con_count*24 ) + total) % 9
			if aux[value] is None:
				aux[value] = item
			else:
				x = (value+ 1) % len(aux)
				while(True):
					if aux[x] is None:
						aux[x] = item
						break;
					x = (x+1)%len(aux)
		print(aux)
					
#------Tester
a = [4,-2,3,-4,7,4]
b = ["ST1E89B8A32","ABC123","DFJDK342","DFGE23","DJBCN1234","DNCNJDNCJ4","CNCIFN78","DNCJDC45","JDNCJ475"]
print("====Task 1=====")
ob = KeyIndex(a)
ob.sort()
print()
print("====Task 2=====")
ob1 = HashTable()
ob1.hash_func(b)