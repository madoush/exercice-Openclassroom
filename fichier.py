#Ceci est un fichier python
def list_bidimensionnelle(A):
    B=[]
    w=[sum(x) for x in A]
    B.append(w)
    return(B)

A=[[1,2,3],[0,7,5],[10,4,12]]
print(list_bidimensionnelle(A))