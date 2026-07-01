a=[10,20,30,40,50]
for i in range (-1,-6,-1):
    print(a[i])

#Print numbers from 1 to 10 using a for loop.
for i in range(1,10+1):
    print(i)
#Print numbers from 10 to 1 in reverse order
for i in range(10,0,-1):
    print(i)
#Print all even numbers between 1 and 20.
for i in range(1,20+1):
    if i%2==0:
        print(i)
#(or)
for i in range(2, 21, 2):
    print(i)
#Find the product (factorial) of numbers from 1 to 5.
fact=1
for i in range(1,6):
    fact=fact*i
    print(fact)
#Count the number of the string "programming".
a="programming"
count=0
for i in a:
    count=count+1
print(count)
#or
a="programming"
print(len(a))
#count vowels in programming
a="programming"
count=0
for i in a:
    if i in "aeiou":
        count+=1
print(count)
#or
a="programming"
count=0
for i in range(len(a)):
    if a[i] in "aeiou":
        count+=1
print(count)
##
a=["apple","banana","cat"]
for i in a:
    if i=="banana":
        print(i)
    else:
        continue
#nested loop
a=["apple","banana","cat"]
b=["red","blue","green"]
for i in a:
    for j in b:
        print(i,j)
    
     

