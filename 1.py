print("hi")
x=int(input("inter a number: "))
for i in range(x,0,-1):
    a=x%i
    if(a==0):
        #print(a)
        print(i)
