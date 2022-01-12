from googlesearch import search

#Permet d'importer et réorganiser la liste des sites web dans un tableau Python

file= open("list-websites.txt", "r")
keywords= file.readlines()

#Fonction de récupération d'une URL en fonction d'un mot clé et envoi de celle-ci dans un fichier texte.
def get_url(keywords):
    i= 1
    while i < 592:
        res= search(keywords, num_results=1, lang="fr")
        temp= res
        f= open("list_url.txt", 'a')
        print(temp, file=f)
        i= i+1

get_url(keywords)
