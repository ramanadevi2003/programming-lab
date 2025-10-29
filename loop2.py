n=int(input("enter the limit:"))
a=0
b=1
print("Fibnocci series upto",n,"term")
for i in range(n):
    print(a,end=" ")
    temp=a
    a=b
    b=temp+b