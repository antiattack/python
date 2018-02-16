list=[]
f=0

while(True):
    name=str(input("enter string: "))
    if(name!="finish"):
        a=len(name)
        for i in range(0,a,+1):
            b=name[f]
            if(b.isdigit()==True):
                list.append(name)
            f=f+1
    print(list)
