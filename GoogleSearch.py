from googlesearch import search

#Récupération d'une URL en fonction d'un mot clé et envoi de celle-ci dans un fichier texte.
i= 1
while i<592:
    res= search("Carrefour", num_results=1, lang="fr")
    temp= res
    f= open("list_url.txt", 'a')
    print(temp, file=f)
    i= i+1
