import math

def discriminant(a,b,c):
    return b*b - 4*a*c

def larger_root(p,q):
    d = discriminant(1,p,q)
    if d > 0:
        return (-p + pow(d,0.5))/2

def smaller_root(p,q):
    d = discriminant(1,p,q)
    if d > 0:
        return (-p - pow(d,0.5))/2


def main():
    p1 = float(input())
    q1 = float(input())

    print(discriminant(1,p1,q1))
    print(smaller_root(p1,q1), larger_root(p1,q1))


#if __name__ == '__main__': main()
