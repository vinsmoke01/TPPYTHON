def bissextile(annee):
    if (annee%100!=0 and annee%4==0) or annee%400==0:
        return True
    return False    
    


def nbrjours(mois,annee):
    if mois<=0 or mois>12:
        return "mois non valide"
    if annee<0:
        return "année non valide"
    elif mois==4 or mois==6 or mois==9 or mois==11:
        return "30 jours"
    elif mois==2:
        if bissextile(annee):
            return "29 jours"
        else:
            return "28 jours"
    else:
        return "31 jours" 


def valide(jour,mois,annee):
    if jour<=nbrjours(mois,annee) and jour>0:
        return True
    return False            

jour=int(input("entrez un jour"))
mois=int(input("entrez le mois"))
annee=int(input("entrez l'annee"))
if valide(jour,mois,annee):
    print("date valide")
else:
    print("date non valide")    


            
