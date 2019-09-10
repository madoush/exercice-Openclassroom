#Ceci est un fichier python
def list_bidimensionnelle(A):
    B=[]
    w=[sum(x) for x in A]
    B.append(w)
    return(B)
    
A=[[1,2,3],[0,7,5],[10,4,12]]
print(list_bidimensionnelle(A))

def remplirDict():
    i=1
    d=dict()
    n=int(input("donner le nbre de matiére"))
    while i<=n:
        m=(input("le nom de la matiére: "))
        x=int(input("la note obtenue: "))
        d[m]=x
        i += 1
    return d