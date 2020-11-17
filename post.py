class Post:
    def __init__(self, contenu, ip_auteur, date_heure_post):
        self.contenu = contenu
        self.ip_auteur = ip_auteur
        self.date_heure_post = date_heure_post
        #on n'a pas besoin de l'heure pour créer le post car lors de la création, SQL va se charger de mettre la date de création (paramètre de la date)
        #cependant on a besoin de l'attribut pour pouvoir l'afficher sur la page web