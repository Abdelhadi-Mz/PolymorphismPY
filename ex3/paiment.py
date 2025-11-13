from abc import ABC, abstractmethod

class Paiment(ABC):
    def __init__(self,montant: float):
        self._montant=montant
    @abstractmethod
    def payer(self):
        pass
class CarteBancaire(Paiment):
    def __init__(self, montant,numero,cvv):
        super().__init__(montant)
        self._numero=numero
        self._cvv=cvv
    def payer(self):
        return f"montatn : {self._montant}  avec la carte Bancaire"
class PayPal(Paiment):
    def __init__(self, montant,email,token_api):
        super().__init__(montant)
        self._email=email
        self._token_api=token_api
    def payer(self):
        return f"montatn : {self._montant}  avec PayPal"
class Crypto(Paiment):
    def __init__(self, montant,id,reseau):
        super().__init__(montant)
        self._id=id
        self._reseau=reseau
    def payer(self):
        return f"montatn : {self._montant}  avec Crypto"
def traiter_paiments(paiments: list):
    for a in paiments:
        print(a.payer())
if __name__== "__main__":
    paiments=[CarteBancaire(1000,498735642453,423),Crypto(1000,48939485,"BTC"),PayPal(2009,"test@uca.ac","45495hhfo0409")]
    traiter_paiments(paiments)


    
