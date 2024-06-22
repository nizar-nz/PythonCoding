class Contact:
    contacts = []

    @classmethod
    def ajout_contact(cls, nom, prenom, numero):
        assert nom.isalpha() and nom.strip(), "Erreur : Le nom doit contenir uniquement des lettres alphabétiques et ne doit pas être vide."
        assert prenom.isalpha() and prenom.strip(), "Erreur : Le prénom doit contenir uniquement des lettres alphabétiques et ne doit pas être vide."
        assert len(numero) == 8 and numero[0] in ['9', '7', '5', '4', '2'], "Erreur : Le numéro de téléphone doit avoir une longueur de 8 chiffres et commencer par 9, 7, 5, 4 ou 2."

        for contact in cls.contacts:
            if contact.nom == nom:
                print("Erreur : Un contact avec le même nom existe déjà.")
                return

        contact = cls(nom, prenom, numero)
        cls.contacts.append(contact)
        print("Le contact a été ajouté avec succès !")

    @classmethod
    def afficher_contacts(cls):
        if not cls.contacts:
            print("La liste des contacts est vide.")
        else:
            print("\nListe des contacts :")
            for contact in cls.contacts:
                print(contact)

    @classmethod
    def modifier_contact(cls, nom, adresse=None, email=None, numero=None):
        for contact in cls.contacts:
            if contact.nom == nom:
                if adresse:
                    contact.adresse = adresse
                if email:
                    contact.email = email
                if numero:
                    assert len(numero) == 8 and numero[0] in ['9', '7', '5', '4', '2'], "Erreur : Le numéro de téléphone doit avoir une longueur de 8 chiffres et commencer par 9, 7, 5, 4 ou 2."
                    contact.numero = numero
                print("Le contact a été modifié avec succès !")
                return

        print("Erreur : Contact non trouvé.")

    @classmethod
    def supprimer_contact(cls, nom):
        for i, contact in enumerate(cls.contacts):
            if contact.nom == nom:
                del cls.contacts[i]
                print("Le contact a été supprimé avec succès !")
                return

        print("Erreur : Contact non trouvé.")

    def __init__(self, nom, prenom, numero, adresse=None, email=None):
        self.nom = nom
        self.prenom = prenom
        self.numero = numero
        self.adresse = adresse
        self.email = email

    def __repr__(self):
        return f"Contact: {self.prenom} {self.nom} - {self.numero}"


while True:
    print("\nMenu :")
    print("1. Ajouter un contact")
    print("2. Modifier un contact")
    print("3. Supprimer un contact")
    print("4. Afficher la liste des contacts")
    print("5. Quitter")

    choix = input("\nChoisissez une option : ")

    if choix == "1":
        nom = input("Nom du contact : ")
        prenom = input("Prénom du contact : ")
        numero = input("Numéro de téléphone : ")

        try:
            Contact.ajout_contact(nom, prenom, numero)
        except AssertionError as e:
            print(str(e))

    elif choix == "2":
        nom = input("Nom du contact à modifier : ")
        adresse = input("Nouvelle adresse (appuyez sur Entrée pour ne pas modifier) : ")
        email = input("Nouvel email (appuyez sur Entrée pour ne pas modifier) : ")
        numero = input("Nouveau numéro de téléphone (appuyez sur Entrée pour ne pas modifier) : ")

        try:
            Contact.modifier_contact(nom, adresse, email, numero)
        except AssertionError as e:
            print(str(e))

    elif choix == "3":
        nom = input("Nom du contact à supprimer : ")
        Contact.supprimer_contact(nom)

    elif choix == "4":
        Contact.afficher_contacts()

    elif choix == "5":
        print("Programme terminé.")
        break

    else:
        print("Choix invalide. Veuillez réessayer.")
