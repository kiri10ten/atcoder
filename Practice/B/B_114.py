a=input()
r={

}

for i in range(len(a)):
    if i<len(a)-2:
        if int(a[i:i+3])>753:
         r[a[i:i+3]]=int(a[i:i+3])-753
        else:
           r[a[i:i+3]]=753-int(a[i:i+3])


minimum = min(r.values())
print(minimum)