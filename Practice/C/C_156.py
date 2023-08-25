a=int(input())
b = list(map(int, input().strip().split()))
t={}

for i in range(min(b),max(b)+1):
     t[i] = 0 
     for j in b:
       t[i]+=(i-j)**2

print(min(t.values()))