n = int(input())
a = list(map(int, input().split()))

l = max(a)
s = min(a)
count = 0
diff = l - s
if diff <= 1:
    print(0)
else:
    for i in range(n):
        for j in range(n):
            if i != j:
                a1 = a[:]
                a1[i] -= 1
                a1[j] += 1
                new_l = max(a1)
                new_s = min(a1)
                if new_l - new_s <= 1:
                    count += 1


print(count)
