in1 = raw_input()
in2 = raw_input()

len2 = len(in2)
count = 0

for i in range(len(in1)-len2+1):
    if in2 == in1[i:i+len2]: count += 1
   
print count
