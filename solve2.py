val = input()
s_list = []

for number in range(10000):
    s = [0] * (4 - len(str(number))) + [*map(int, str(number))]
    s_list.append(s)


count = 0

for c in s_list:
    valid = True
    for i in range(10):
        if val[i] == 'o' and i not in c:
            valid = False
            break
        if val[i] == 'x' and i in c:
            valid = False
            break
    if valid:
        count += 1

print(count)