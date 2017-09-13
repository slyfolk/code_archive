
a = 23,35,46,21
total = 0
e=[]
b=''
for i in a:
	x= str(i)
	e.append(x)
	for j in x:
		total += int(j)
		b+=j
print(total)
print(b)
c = "+".join(b)
d = "+".join(e)
print(c)
print(d)

print(str(a))
print(type(a))
print(type(a[0]))

x = [1,2,3,4,3,5,2]
y = [1,2,2,2,4,4,3,5,3]


x = [str(i) for i in x]
y = [str(j) for j in y]
g="".join(x)
h="".join(y)
print(x)
print(y)
print(g)
print(h) 

def numero(x,y):
	print(x)
	print(y)
	a = list(set(x))
	b = list(set(y))
	print(a)
	print(b)
	x_compare = []
	y_compare = []
	x_count = [x.count(i) for i in a] 
	y_count = [y.count(i) for i in b]
	for j,k in zip(a,x_count):
		result = j,k
		x_compare.append(result)
	print (x_compare)
	print()
	for j,k in zip(b,y_count):
		result = j,k
		y_compare.append(result)
	print (y_compare)
	print()
	z = []
	for i,j in zip(x_compare,y_compare):
		if i != j:
			z.append(i[0])
	print(z)
	print()
	print ([int(i) for i in z])

def numero_optimized(a,b):
	a.sort()
	b.sort()
	z = [i for i in set(a) if a.count(i)!=b.count(i)]
	print(z)
print("making changes on work directory")
	
		









