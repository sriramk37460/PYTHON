#conditional operator
if 10>5:
    print("True")
    a=10
    if a==10:
        print("Equal")
    else :
        print("Not Equal")

#looping statement
for i in range(5):
    print(i)
    i=0

while i<10:
    print(i)
    i+=1
#continue and break
for i in range(0,10):
    if i==3:
        continue
    if i==5:
        break
    print(i)
#loop else
for i in range(5):
    print(i)
else:
    print("else")