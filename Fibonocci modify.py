k = map(int,raw_input().split(" "))
def fibby(k1,k2,n):
    count = 2
    while True:
        k1,k2 = k2,k1+k2**2
        count += 1
        if count == n: return k2
        

print fibby(*k)
