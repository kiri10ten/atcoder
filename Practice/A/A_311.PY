n=int(input())
s=input()
uniquecharacters=set()
count=0
for i in s:
    uniquecharacters.add(i)

    if len(uniquecharacters)==3:
        break
    
    count+=1

print(count+1)