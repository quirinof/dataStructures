# bubble sort example

def sort(v, n):
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]


listt = [5, 2, 8, 1, 3, 9, 7, 6, 4]
print("original list:", listt)
sort(listt, len(listt))
print("ordered list:", listt)