import mysql.connector
from datetime import datetime,timedelta
from post import Post

def connection_function():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'mysql',
        'port': '3306',
        'database': 'blog_DB'
    }
    myDatabase = mysql.connector.connect(**config)
    return myDatabase


def fetch_posts():
    myDatabase = connection_function()
    cursor = myDatabase.cursor()

    cursor.execute('SELECT * FROM posts')
    results = cursor.fetchall()
    #Récupère toutes les lignes d'un résultat de requête
    #Renvoie toutes les lignes sous forme de liste de tuples
    #Une liste vide est renvoyée s'il n'y a pas de data à récupérer

    list_of_posts = []
    for post in results:
        #on récupère les valeurs dans le tuple
        contenu = post[1]
        ip_auteur = post[2]
        date_heure_post = post[3]

        #je mets la date sous le format que je veux
        date_heure_post.strftime('%Y-%m-%d %H:%M:%S')
        #conversion de la date et heure (je rajoute 1 heure car j'ai un décalage)
        date_heure_post = date_heure_post + timedelta(hours=1)

        #création d'un post
        temp_post = Post(contenu,ip_auteur, date_heure_post)
        
        list_of_posts.append(temp_post)
    
    cursor.close()
    myDatabase.close()

    return list_of_posts


def create_post(contenu,ip_auteur):
    myDatabase = connection_function()
    cursor = myDatabase.cursor()

    query = "INSERT INTO posts(contenu, ip_auteur) VALUES (%s,%s);"
    values = (contenu,ip_auteur)
    cursor.execute(query,values)

    myDatabase.commit()
    
    return