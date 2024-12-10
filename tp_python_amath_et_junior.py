class CompteBancaire:    
    def __init__(self, prenom, nom, numero, solde):
        self.prenom = prenom
        self.nom = nom
        self.numero = numero
        self.__solde = solde
        print("Pour créer un compte, entrez les informations suivantes: ")
        prenom = input("Entrez votre prenom: ")
        nom = input("Entrez votre nom: ")
        print("Parfait " + prenom + " " + nom + ", votre compte a été créé avec succès.")
        print("Que souhaitez-vous faire ?")
        print("1. Afficher les informations du compte")
        print("2. Déposer de l'argent")
        print("3. Retirer de l'argent")
        print("4. Afficher le solde du compte")

    def action(self, montant):
        choix = int(input())
        if choix == 1:
          print(f"Nom du titulaire: {self.prenom} {self.nom}, Numero du compte: {self.numero}, Solde du compte: {self.__solde}€")

        elif choix == 2:
            int(input("Entrez le montant: "))
            self.__solde += montant
            print(f"Votre nouveau solde est de {self.__solde}€")
            
        elif choix == 3:
            int(input("Entrez le montant: "))
            self.__solde -= montant
            if self.__solde >= montant:
                print(f"Votre nouveau solde est de {self.__solde}€")
            elif self.__solde < montant:
                print(f"Vous ne pouvez pas retirer {self.__solde}€")

        elif choix == 4:
            self.__solde = self.__solde
            print(f"Le solde de votre compte est de {self.__solde}€")
            
compte = CompteBancaire("Amath", "Thiare", 4830917843038596, 0)
compte.action(int(input()))
