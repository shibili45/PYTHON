li=input("enter the numbers separated with commas=")
li1=li.split(",")
s=0
print("list elements are...")
print(li1)
for x in li1:
    s=s+int(x)
print("sum of all items in a list=",s)
