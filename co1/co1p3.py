#a)
num1=[-4,-3,-2,-1,1,2,3,4,-5,-6,-7,8,9]
num2=[x for x in num1 if x>0]
print(num2)

#b)
n=int(input("Enter the limit="))
print([x*x for x in range(n+1)])

#c)
word=input("Enter a word=")
vowel=["A","E","I","O","U","a","e","i","o","u"]
listv=[x for x in word if x in vowel ]
print(listv)

#d
word=input("Enter a word=")
listo=[ord(x) for x in word]
print(listo)
