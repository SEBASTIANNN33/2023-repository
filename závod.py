def win1(t, s, v = 0):
    while t*v <= s:
        t = t-1
        v = v+1
    return t-v+1

a = win1(40, 233)
b = win1(82, 1011)
c = win1(84, 1110)
d = win1(92, 1487)
e = win1(71530, 940200)
f = win1(40828492, 233101111101487)
#print(a*b*c*d)
#print(e)
print (f)



