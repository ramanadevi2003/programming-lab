def fibo(n):
    if n<=1:
        return n
    else:
     return fibo(n-1)+fibo(n-2)
terms=int (input("enter the number of terms:"))
if terms<=0:
    print("please enter a positive number:")
else:
   print("fibonacci series:")
for i in range(terms):
   print(fibo(i))
