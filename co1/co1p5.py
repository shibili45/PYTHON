lst = []
lst = [int(item) for item in input("Enter the list items : ").split()]
print("INPUT IS", lst)
x = ["over" if x > 100 else x for x in lst]
lst = list(x)
print(lst)
