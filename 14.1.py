print("HI")
b=0
list=[]

for i in range(0,5,+1):
    x=int(input("Enter Number: "))
    if (x<0):
        list.append(x)
        f=list
        b=b+1
        f.sort()
print("Number of negative numbers: ",b)
print("negative numbers are: ",f)

