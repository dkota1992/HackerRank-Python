# Enter your code here. Read input from STDIN. Print output to STDOUT
def fibby():
    a,b = 0,1
    yield a
    yield b
    while True:
        a,b = b,a+b
        yield b
    
N = input()
kk = fibby()
print(map(lambda x:x**3,[kk.next() for x in range(N)]))
 
