n = int(input())
a = []
b = [[] for i in range(10)]
for i in range(n):
    a.append(input())
    
print("Initial array:")
print(*a, sep = ", ")

def print_bucket(b, k):
    print("**********", f"Phase {len(a[0]) - k}", sep = "\n")
    for i in range(10):
        print(f"Bucket {i}:", ", ".join(b[i])) if b[i] != [] else print(f"Bucket {i}: empty")

def change_array(d):
    global a
    a = []
    for k in range(10):
        if d[k] != []: a.extend(d[k])
    

for i in range(len(a[0])-1, -1, -1):
    for j in a:
        b[int(j[i])].append(j)
    print_bucket(b, i)
    if i != 0: 
        change_array(b)
        b = [[] for j in range(10)] 
    
change_array(b)
print("**********", "Sorted array:", sep="\n")
print(*a, sep = ", ")
    
    
