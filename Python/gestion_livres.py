from typing import Optional,List
from dataclasses import dataclass




@dataclass
class Livre:
    titre : str
    auteur : str
    annee : Optional[int] = None
    disponible : Optional[bool] = True

    def __init__(self,titre,auteur,annee,disponible=True) -> None:
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = disponible
    def __str__(self):
        return f"{self.titre} par {self.auteur} ({self.annee}) - {'Disponible' if self.disponible else 'Non disponible'}"
    
    def emprunter(self) -> str:

        if self.disponible :
            self.disponible = False
            return f"Le livre '{self.titre}' a été emprunté."
        return f"Le livre '{self.titre}' n'est pas disponible."
    def retourner(self) -> str :
        if not self.disponible:
            self.disponible = True
            return f"Le livre '{self.titre}' a été retourné."
        return f"Le livre '{self.titre}' n'est pas emprunté."
    


@dataclass
class  Bibliotheque :
    nom : str
    livres : list[Livre]

    def __init__(self,nom,livres) -> None:
        self.nom = nom
        self.livres = livres
    
    def ajouter_livre(self,livre) -> str:
        self.livres.append(livre)
        return f"{livre.titre} a été ajouté à la bibliothèque."

    def rechercher_par_auteur(self, auteur) -> list:
        return [livre for livre in self.livres if livre.auteur == auteur]
    
    def  livres_disponibles(self) -> list :
        return[l for l in self.livres if l.disponible]
    
    def statistiques(self) -> str :
        i,j = 0,0
        while i < len(self.livres):
            if self.livres[i].disponible:
                j += 1
            i += 1
        return f"Nombre de livres : {len(self.livres)}, Livres disponibles : {j}"
    


def main() -> None:
    """
    Programme principal :
    - Crée une bibliothèque
    - Ajoute 5 livres de 3 auteurs différents
    - Emprunte 2 livres, retourne 1
    - Affiche les statistiques et les livres disponibles
    """

    nom_biblio = input("Entrez le nom de la bibliothèque : ")

    livres: List[Livre] = []
    for i in range(1, 6):
        print(f"\n--- Livre {i} ---")
        titre = input("Titre : ")
        auteur = input("Auteur : ")
        annee = int(input("Année de publication : "))
        reponse = input("Disponible ? (oui/non) : ").strip().lower()
        disponible = reponse == "oui"

        livre = Livre(titre, auteur, annee, disponible)
        livres.append(livre)


    bibliotheque = Bibliotheque(nom_biblio, livres)


    if len(livres) >= 2:
        print("\n" + livres[0].emprunter())
        print(livres[1].emprunter())

    # Retourner 1 livre (le premier, s'il a été emprunté)
    if len(livres) >= 1:
        print(livres[0].retourner())

    print("\n" + bibliotheque.statistiques())

   
    print("\nLivres disponibles :")
    for livre in bibliotheque.livres_disponibles():
        print(f"  - {livre.titre}")

   
    print("\nRecherche par auteur (exemple : 'Victor') :")
    auteur_test = input("Auteur : ")  
    resultats = bibliotheque.rechercher_par_auteur(auteur_test)
    if resultats:
        for livre in resultats:
            print(f"  - {livre}")
    else:
        print(f"Aucun livre de {auteur_test} trouvé.")


if __name__ == "__main__":
    main()   


    
    






