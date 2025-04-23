class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def afficher_nom_prenom(self):
        print(f"Prénom : {self.prenom}")
        print(f"Nom : {self.nom}")

personne1 = Personne("NDAW", "Daour")
personne1.afficher_nom_prenom()
