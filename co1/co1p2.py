x=int(input("future year :"))
y=int(input("current year:"))

while (y<=x):
    if y%100==0:
        if y%400==0:
            print(y)
    elif y%4==0:
        print(y)
    y=y+1
