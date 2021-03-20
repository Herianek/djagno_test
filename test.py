i = 0
a = input("napiš slovo: ")
s = len(a)- 1
x = []
y = []

while i != len(a):
    x.append(a[i])
    y.append(a[s])
        

    i += 1
    s -= 1

if x == y:
    print("Čte")
else:
    print("NEČTE")
