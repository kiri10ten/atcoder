# n = int(input())
# a = list(map(int, input().split()))
# if n <= 1:
#   print(0)
# else: 
#     L = max(a)
#     S = a[0]

#     M= max(a[1:])
#     diff = max(0,(M-S)+1)
#     print(diff)
N = int(input())

d = []
for i in range(N):
    C = int(input())
    A = list(map(int, input().split()))
    d.append((C, A))

X = int(input())
winners = []


min_bets = 65
for i in range(N):
    if X in A:
        min_bets = min(min_bets, C)


for i in range(N):
    if X in A and C == min_bets:
        winners.append(i + 1)  


print(len(winners))
for winner in winners:
    print(winner)




       