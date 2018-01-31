list=[]
g=0
for i in range(0,5,+1):
    x=int(input("enter a number: "))
    if (x>=10):
        g=g+1
        list.append(x)
sum=sum(list)
ave=sum/g
print("average grater than 10: ",ave)
