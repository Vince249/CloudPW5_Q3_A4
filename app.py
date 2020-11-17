#https://medium.com/@shamir.stav_83310/dockerizing-a-flask-mysql-app-with-docker-compose-c4f51d20b40d

import flask
from db_functions import *

app = flask.Flask(__name__)


@app.route('/')
def index():
    list_of_posts = fetch_posts()
    return flask.render_template('index.html', list_of_posts = list_of_posts) 
    #pas besoin de spécifier le chemin jusqu'à "index.html" puisque python va aller chercher dans le folder "templates" par défaut 
    #(faut donc penser à bien créer ce folder avec ce nom là et pas un autre)


@app.route('/addPost',methods=['POST'])
def addPost():
   #récupération des informations
   contenu = flask.request.form['contenu']
   ip_auteur = flask.request.remote_addr
   create_post(contenu,ip_auteur)

   return flask.redirect(flask.url_for('index'))



if __name__ == '__main__':
    app.run(host='0.0.0.0')
    #ne fonctionne pas sur localhost (127.0.0.1)
    #en effet, quand je lance le serveur, je vois sur le terminal que l'IP à l'air d'être 172.22.0.1 (visible aussi quand je crée un post sur le site)
    #le fait de mettre '0.0.0.0' va permettre de dire à notre application d'écouter sur toutes les adresses IP. Comme j'ai bind un port de mon ordi
    #avec le port 5000 du container, elle va donc écouter sur le port 5000 de toutes les adresses IP. 
    #J'imagine qu'elle va donc run sur le port 5000 du localhost du container 
