def multiplication(A,B):
    n=len(A)
    m=len(B)
    if m==len(A[0]):
        C=[[0 for i in range(0,len(B[0]))] for j in range(0,n)]
        for i in range(0,n):
            for j in range(0,len(B[0])):
                for k in range(0,m):
                    C[i][j]+=A[i][k]*B[k][j]
        return C 
    else:
        return "condition de multiplication des matrices n'est pas vérifiée"                  

