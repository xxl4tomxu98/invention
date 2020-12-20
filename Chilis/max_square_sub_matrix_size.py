"""Given a binary matrix, find out the maximum size square sub-matrix
with all 1s.
For example, consider the below binary matrix.
maximum-size-square-sub-matrix-with-all-1s
   0  1  1  0  1
   1  1  0  1  0
   0  1  1  1  0
   1  1  1  1  0
   1  1  1  1  1
   0  0  0  0  0
Algorithm:
Let the given binary matrix be M[R][C]. The idea of the algorithm is to
construct an auxiliary size matrix S[][] in which each entry S[i][j]
represents size of the square sub-matrix with all 1s including M[i][j]
where M[i][j] is the rightmost and bottommost entry in sub-matrix.

1) Construct a sum matrix S[R][C] for the given M[R][C].
     a)    Copy first row and first columns as it is from M[][] to S[][]
     b)    For other entries, use following expressions to construct S[][]
         If M[i][j] is 1 then
            S[i][j] = min(S[i][j-1], S[i-1][j], S[i-1][j-1]) + 1
         Else /*If M[i][j] is 0*/
            S[i][j] = 0
2) Find the maximum entry in S[R][C]
3) Using the value and coordinates of maximum entry in S[i], print
   sub-matrix of M[][]
For the given M[R][C] in above example, constructed S[R][C] would be:

   0  1  1  0  1
   1  1  0  1  0
   0  1  1  1  0
   1  1  2  2  0
   1  2  2  3  1
   0  0  0  0  0
The value of maximum entry in above matrix is 3 and coordinates of the entry
is (4, 3). Using the maximum value and its coordinates,
we can find out the required sub-matrix."""


def MaxSubSquare(M):
    R = len(M)  # no. of rows in M[][]
    C = len(M[0])   # no. of columns in M[][]

    S = [[0 for k in range(C)] for l in range(R)]
    # here we have set the first row and column of S[][]
    for j in range(C):
        S[0][j] = M[0][j]
    for i in range(R):
        S[i][0] = M[i][0]
    # Construct other entries
    for i in range(1, R):
        for j in range(1, C):
            if (M[i][j] == 1):
                S[i][j] = min(S[i][j-1], S[i-1][j],
                              S[i-1][j-1]) + 1
            else:
                S[i][j] = 0

    # Find the maximum entry and
    # indices of maximum entry in S[][]
    max_of_s = S[0][0]
    max_i = 0
    max_j = 0
    for i in range(R):
        for j in range(C):
            if (max_of_s < S[i][j]):
                max_of_s = S[i][j]
                max_i = i
                max_j = j

    print("Maximum size sub-matrix is: ")
    for i in range(max_i, max_i - max_of_s, -1):
        for j in range(max_j, max_j - max_of_s, -1):
            print(M[i][j])
        print("")


M = [[0, 1, 1, 0, 1],
     [1, 1, 0, 1, 0],
     [0, 1, 1, 1, 0],
     [1, 1, 1, 1, 0],
     [1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0]]
print(MaxSubSquare(M))
