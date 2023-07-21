#list
lst=[10,20,30]
for i in lst:
    print(i)
print("\n")
#list operartion 1(traversing)
lst=[10,20,30,40]
for i in lst:
    if(i==20):
        continue
    elif(i==40):
       break
    else:
        print(i)
else:
    print("else part print")

print("\n")
#list hw
lst=[10,20,30,40,50]
print((10*2) in lst)
print(lst[1]+lst[-1])
print("\n")

#list operation
lst=[10,20,30,40,50]
print(max(lst))
print(min(lst))
#append
lst.append(70)
print("append:")
print(lst)
#nested list
lst1=[1,2,3]
lst1.append([4,5])
print("nested loop:")
print(lst1)
#insert
lst.insert(5,60)
print("insert:")
print(lst)

#extend
lst.extend([80,90,100])
print("extend:")
print(lst)

#remove
lst.remove(100)
print(lst)
#pop
lst.pop(-1)
print(lst)
#store the removing element in variable
element=lst.pop(-1)
print(lst)
print(element)
#sort
lst1=[100,2,30]
lst1.sort()
print(lst1)
#reverse
lst1.sort(reverse=True)
print(lst1)

#list of function
lst2=list(input("enter the string "))
print(lst2)

#list hw1
lst3=[10,20,30]
lst3.append([40])
lst3.extend([40])
print(lst3)