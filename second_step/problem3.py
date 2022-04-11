a=17391
b=546
c=934
if a%17 < b%17 and a%17 < c%17:
    print("a")
elif b%17 < a%17 and b%17 < c%17:
    print("b") 
elif c%17 < a%17 and c%17 < b%17:
    print("c")
