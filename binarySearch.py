# binary search example

def bsearch(v, s, e, k):
    if s <= e:
        m = (s + e) // 2
        if k == v[m]:
            return m
        if k < v[m]:
            return bsearch(v, s, m-1, k)
        return bsearch(v, m+1, e, k)
    return -1


ord_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
element = int(input('n: '))
index_find = bsearch(ord_list, 0, len(ord_list) - 1, element)

if index_find != -1:
    print(f'element found in index {index_find}')
else:
    print('dont exist this element')