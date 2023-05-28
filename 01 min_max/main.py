lst = [-2, -1, -5, -4, -1, 22,  -99, -89, -78, -98]
greater = lst[0]
lesser = lst[0]
for i in lst:
    if i > greater:
        greater = i
    elif i < lesser:
        lesser = i
print(greater)
print(lesser)
