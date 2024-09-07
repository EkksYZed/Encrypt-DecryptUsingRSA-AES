import random
import sys
import os

def generate_keys(Name):
    p = getprime(1024)
    q = getprime(1024)
    n = p * q
    f = (p - 1) * (q - 1)

    while True:
        d = random.randrange(2, f)
        if findGCD(d, f)[0] == 1:
            break

    e = minverse(d, f)
    if e == None:
        print("d and f are not coprime and hence, no inverse exists")
        sys.exit()

    with open(f"{Name}.pub", "w") as file:
        file.write(f"{n},{e}")

    with open(f"{Name}.prv", "w") as file:
        file.write(f"{n},{d}")


def primecheck(n, repeat):
    #The easy cases
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    r = 0
    s = n-1
    while s % 2 == 0:
        r = r + 1
        s = s // 2

    for i in range(repeat):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for j in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def getprime(size):
    while True:
        random_bytes = os.urandom(size // 8)
        p = int.from_bytes(random_bytes, byteorder='big')
        if primecheck(p, repeat):
            return p

def findGCD(a, b):
    x = 0
    y = 1
    u = 1
    v = 0
    while a != 0:
        q= b // a
        r = b % a
        m = x - u * q
        n = y - v * q 
        b = a
        a = r
        x = u
        y = v
        u = m
        v = n
    return b, x

def minverse(n1, n2):
    gcd, x = findGCD(n1, n2)
    if gcd != 1:
        print("No MOD inverse")
        return None
    else:
        return x % n2

Name = sys.argv[1]
repeat=5
generate_keys(Name)