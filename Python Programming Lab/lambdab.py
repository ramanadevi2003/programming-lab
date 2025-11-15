def check(n):
    if n% 2==0:
        return "Even"
    else:
        return "Odd"
num=int(input("Enter the number:"))
print("the given number",num,"is",check(num))