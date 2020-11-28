""" Q1: Given two matrices please print the product of those two matrices 

Ex 1: A   = [[1 3 4]
             [2 5 7]
             [5 9 6]]
      B   = [[1 0 0]
             [0 1 0]
             [0 0 1]]
      A*B = [[1 3 4]
             [2 5 7]
             [5 9 6]]

     
Ex 2: A   = [[1 2]
             [3 4]]
      B   = [[1 2 3 4 5]
             [5 6 7 8 9]]
      A*B = [[11 14 17 20 23]
             [23 30 37 44 51]]
             
Ex 3: A   = [[1 2]
             [3 4]]
      B   = [[1 4]
             [5 6]
             [7 8]
             [9 6]]
      A*B =Not possible
"""



# here A and B are list of lists
def matrix_mul(A, B):
    # write your code
    m1 = len(A)
    n1 = len(A[0])
    m2 = len(B)
    n2 = len(B[0])
    if(n1!=m2):
        print("Not Possible")
    else:
        c = [[0]*n2 for _ in range(m1)]
        for i in range(m1):
            for j in range(n2):
                total = 0
                for k in range(n1):
                    total += A[i][k] * B[k][j]
                c[i][j]=total
        return c

    
A = [[1,3,4],[2,5,7],[5,9,6]]
B = [[1,0,0],[0,1,0],[0,0,1]]    

print("Matrix A\n",A)
print("Matrix B\n",B)
print("AxB\n",matrix_mul(A, B))

A = [[1,2],[3,4]]
B = [[1,2,3,4,5],[5,6,7,8,9]]
print("Matrix A\n",A)
print("Matrix B\n",B)
print(len(A),len(A[0]))
print(len(B),len(B[0]))
print("AxB\n",matrix_mul(A, B))

A = [[1,2],[3,4]]
B = [[1,4],[5,6],[7,8],[9,6]]
print("Matrix A\n",A)
print("Matrix B\n",B)
print(len(A),len(A[0]))
print(len(B),len(B[0]))
print("AxB\n",matrix_mul(A, B))