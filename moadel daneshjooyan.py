#average betweent 10 to 15
x=int(input("how many student you have? ".title()))
list=[]
c=0
for i in range(x,0,-1):
    c=c+1
    print("avrerage student".title(),c,":",end="",sep="")
    a=float(input())
    if(a>=10)and(a<=15):
        list.append(a)
        list.sort()
print(list)
