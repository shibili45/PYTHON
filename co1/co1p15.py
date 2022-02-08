li1=["violet","yellow","blue","white","black"]
li2=["violet","black","orange","green","yellow"]
print(li1)
print(li2)
print("all colors from color-list1 not contained in color-list2")
print([x for x in li1 if x not in li2])
