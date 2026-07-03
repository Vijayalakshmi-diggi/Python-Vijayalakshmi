a=[500,200,300]
b=["apple","babana"]
print(a,b)
#ordered
print(a[1])
#mutable
a[1]=100
print(a)
#allows duplicates and mixed data type
c=['apple','banana',100,'apple',100]
print(c)
#append()
d=[10,20,30]
d.append(40)
print(d)
#insert()
d.insert(1,15)
print(d)
#remove()
d.remove(30)
print(d)
#pop() removes by index
d.pop(0)
print(d)
#sort
d.sort()
print(d)

