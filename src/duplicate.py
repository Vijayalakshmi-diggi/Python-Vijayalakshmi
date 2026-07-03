a=[1,2,2,3]
b=[]
for i in a:
    if i in b:
        print("duplicate found",i)
        break
    else:
        b.append(i)
#


