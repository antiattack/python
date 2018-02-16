listali=[]
ali=0
k=[]
count=[]
for i in range(0,4,+1):
    x=str(input("enter your name: "))
    if(x=="Ali" or x=="ali" or x=="ALi" or x=="ALI"):
        ali=ali+1
        listali.append(x)
    if(x[0]=="k"):
        k.append(x)
    if (len(x)>=6):
        count.append(x)



print("listali: ", listali)
print("k liat: ",k)
print(count)
