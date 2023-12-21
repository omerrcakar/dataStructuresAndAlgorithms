def bigon(n):
    for i in range(0,n):
        print(i)

#bigon(5)


def bigon2(m):
    for i in range(0,m):
        for j in range(0,m):
            print(i,j)


#bigon2(4)
            


import math
x = math.floor(5/2)  # yuvarlama

#print(x)

def logn(n):
    while n > 1:
        n = math.floor(n/2)

        print(n)

#logn(64)


def nlogn(n):
    lim = n
    while n > 1:
        n = math.floor(n/2)
        for i in range(1,lim):
            print(i)

#nlogn(64)


# faktöryel bulma
def fakt(n):
    fak = 1
    if n == 0 or n == 1:
        print(f"Sonuc: {1}")
    
    for i in range(n,0,-1):
        fak *= i
    
    print(f"sonuc: {fak}")
        
#fakt(5)


#recursive faktöriel bulma
def fakt2(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return (n * fakt2(n-1))
    
x = fakt2(4)
print(x)