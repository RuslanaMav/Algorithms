import random
n = int(input())
a = list(map(int, input().split()))


def partition(l, r, x):
    e, g = -1, -1
    for i in range(l, r):
        if e == -1 and g == -1:
            if a[i] == x: e = i
            elif a[i] > x: g = i
        
        elif e == -1 and g != -1:
            if a[i] < x:
                z = a[i]
                a[i], a[g] = a[g], z
                g += 1
            elif a[i] == x:
                a[i], a[g] = a[g], x
                e = g
                g += 1
   
        elif e != -1 and g == -1:
            if a[i] < x:
                a[e], a[i] = a[i], x
                e += 1
            elif a[i] > x: g = i
        else:
            if a[i] < x:
                z = a[i] 
                a[i], a[g], a[e] = a[g], a[e], z
                e += 1
                g += 1
            elif a[i] == x:
                a[i], a[g] = a[g], x
                g += 1
      
    if g == -1: g = r
    if e == -1: e = 0
    return e, g

def quick_sort(l, r):
    if r <=1: return a
    x = a[random.randrange(l, r)]
    p_l, p_r = partition(l, r, x)
    if p_l - l > 1: quick_sort(l, p_l)
    if r - p_r > 1: quick_sort(p_r, r)
    return a
    

print(*quick_sort(0, n))
