def search(v, n, k):
    ans = 0
    for i in range(n):
        if (v[i] == k):
            ans = i
    return ans


lista = [3, 5, 2, 7, 8, 9]
valueK = int(input('numb: '))
index = search(lista, len(lista), valueK)

if index != 0:
    print(f'found in id {index}')
else:
    print('not found')