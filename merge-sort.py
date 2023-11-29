n = int(input())
a = list(map(int, input().split()))

def merge(a, b):
    d = [0] * (len(a) + len(b))
    x, y = 0, 0
    for i in range(len(d)):
        if x == len(a):
            d[i:] = b[y:]
            break
        elif y == len(b) :
            d[i:] = a[x:]
            break
        elif a[x] <= b[y]:
            d[i] = a[x]
            x += 1
        else:
            d[i] = b[y]
            y += 1
    return d
        
def merge_sort(d):
    n = len(d) // 2
    if n != 0: 
        k1 = merge_sort(d[:n])
        k2 = merge_sort(d[n:])
        d = merge(k1, k2)
    return d
        
print(*merge_sort(a))   

    

    

    



