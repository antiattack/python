x=input("enter your name: ")
a=len(x)
digit=[0,1,2,3,4,5,6,7,8,9]
print("x= ",x,end="" "\t")
print("len: ",a)
print("Alphabet: ",x.isalpha())
b={}
f=0
if(x.isalpha()):
    print("alhpaet: ",x)
else:
    for i in range (0,a,+1):
        b=x[f]
print(x)
