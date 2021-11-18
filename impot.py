def mesImpots(revenu):
    Montant=[10085,25711,73517,158123]
    TauxImpo=[11/100,30/100,41/100,45/100]
    if revenu<Montant[0]:
        impot=0
    elif revenu>=Montant[0] and revenu<Montant[1]:
        impot=(revenu-Montant[0])*TauxImpo[0]
    elif revenu>=Montant[1] and revenu<Montant[2]:
        impot=(revenu-Montant[1])*TauxImpo[1]+(Montant[1]-Montant[0]+1)*TauxImpo[0]
    elif revenu>=Montant[2] and revenu<Montant[3]:
        impot=(revenu-Montant[2])*TauxImpo[2]+(Montant[2]-Montant[1]+1)*TauxImpo[1]+(Montant[1]-Montant[0]+1)*TauxImpo[0]
    else:
        impot=(revenu-Montant[3])*TauxImpo[3]+(Montant[3]-Montant[2]+1)*TauxImpo[2]+(Montant[2]-Montant[1]+1)*TauxImpo[1]+(Montant[1]-Montant[0]+1)*TauxImpo[0]
    return impot                
            

revenu=float(input("donnez votre montant des revenus"))          
print("tes impots sont:",mesImpots(revenu))  