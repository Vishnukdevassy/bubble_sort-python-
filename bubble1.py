n=int(input("enter the limit of an array"));
a=[]


for i in range(n):
	p=int(input("enter the array elements are"));
	a.append(p)


print("****Before Swapping****:");
print("-------------------------------------:");
for i in range(n):
	print(a[i])


print("****After Swapping****:");
print("-------------------------------------:");

for i in range(0,n):
	
	for j in range(i+1,n):
		
		
		if(a[i]>a[j]):
			temp=a[i]
			a[i]=a[j]
			a[j]=temp

for i in range(n):
	print(a[i])