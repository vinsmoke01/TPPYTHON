def Syracuse(n):
    L=[n]
    while len(L)<15:
        if n%2==0:
            n=n/2
            L.append(n)
        else:
            n=n*3+1
            L.append(n)
    return L       



    

