p = [x for x in raw_input()]
res = ''
i=0
count = 1
def s_string(k):
    i = 0   
    while True:
        if i >= len(k) - 1:
            return k
        if k[i] == k[i+1]:
            k[i:i+2] = []
            continue
        else: i = i+1

while True:
    pp = len(p)
    p = s_string(p)
    if pp == len(p):
        if p == []: 
            print "Empty String"
            break
        print ''.join(x for x in p)
        break
