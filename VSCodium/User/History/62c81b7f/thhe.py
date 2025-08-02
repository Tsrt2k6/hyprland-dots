a = [1,2,3,4,[6,9]]
b = a.deepcopy()
b[4][0] = 8
print(a)