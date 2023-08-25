b1 = 10000
b2 = 5000
b3 = 1000
u = -1
a, b = map(int, input().split())

r = True
for i in range(a + 1):
    for j in range(a + 1):
        for c in range(a + 1):
            if ((i * b1) + (j * b2) + (c * b3)) == b:
                r = False
                print(f"{i} {j} {c}")
                break  

        if not r:
            break  
    if not r:
        break  
if r:
    print(f"{u} {u} {u}")
