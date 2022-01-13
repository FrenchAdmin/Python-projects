from googlesearch import search

#Récupération d'une URL en fonction d'un mot clé et d'un tld renseigné manuellement dans un terminal et envoi de l'URL dans un fichier texte.
i= 1
while i < 592:
    keyword=(input(str("Entrez le site web: ")))
    dom=(input(str("Entrez le tld: ")))
    res= search(keyword, num_results=1, lang=dom)
    temp= res
    f= open("list_url.txt", 'a')
    print(temp, file=f)
    i= i+1