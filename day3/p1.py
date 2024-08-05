array_3d = []

# array[2][3][2] = {{{1, 2}, {2, 3}, {3, 4}}, {{4, 5}, {5, 6}, {6, 7}}};
for i in range(2): # the 3D array has 2 matrices
    t_2 = []
    for j in range(3): # each Matric will have 3 rows
        t_1 = []
        for k in range(2): # each 1d array will have 2 elements
            t_1.append(int(input()))
        t_2.append(t_1)
    array_3d.append(t_2)

print(array_3d)
