n,d,q=map(int, input().split())
dishes=list(map(int, input().split()))

if d<q + min(dishes):
     print(d)
elif d >= q + min(dishes):
     print(q+min(dishes))

