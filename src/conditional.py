marks=100
if marks>=90:
    print("grade A")
if marks>=100:
    print("grade A+")
elif marks<50:
    print("grade c")
elif marks in [70,80]:
    print("grade B")
else:
    print("none")
