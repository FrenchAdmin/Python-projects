import re #Importation de la librairie permettant de faire des regex.

with open("list_url.txt") as file: #Ouvre le fichier list_url.txt sous le nom file.
        for line in file:
            urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
            f= open("list_url_clean.txt", "a")
            print(urls, file=f)