n = int(input("Enter the limit "))
a=0
b=1
print("the fibonacci series is")
print(a)
print(b)
for i in range(1,n):
    sum=a+b
    print(sum)
    a=b
    b=sum
