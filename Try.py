import numpy as np

a = [[5, 6, 7], [1, 2, 3], [4, 8, "B"]]



inversion = 0


for i in range (len(a)):
    for j in range (len(a)-1):

        if a[i][j] == "0":
            continue
        elif a[i][j] < a[i][j+1]:
            print("yes")