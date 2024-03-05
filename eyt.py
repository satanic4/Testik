A = [2, 4, 1, 7, 3, 5, 11]
s = 1
for i in range(3):
    if A[i] < A[i+1]:
        A[i+1], A[i] = A[i], A[i+1]
        s += A[i]
print(s)