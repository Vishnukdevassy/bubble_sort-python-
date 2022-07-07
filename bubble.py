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

for i in range(n-1,0,-1):
	print("****i****:");
	print(a[i])
	for j in range(i):
		print("****j****:");
		print(a[j])
		print("****j+1****:");
		print(a[j+1])
		if(a[j]>a[j+1]):
			temp=a[j];
			a[j]=a[j+1];
			a[j+1]=temp;

for i in range(n):
	print(a[i])