from bs4 import BeautifulSoup


#--------LECTURE DES DONNEES HTML-------------
        #noustravaillons en local dont: ouvrir le site local

f=open("recette.html","r")
html_content= f.read()
f.close()

soup = BeautifulSoup(html_content, "html.parser")

#recherde tag(balise)
titre_h1= soup.find("h1")# atrributs:", class_="""
titre_html = titre_h1.text#.text pur afficher le contenu
#print("letitre de notre html:",titre_html)

#---------------------exercice-------------------------
texte_p= soup.find("p", class_="description" )
titre_html = titre_h1.text

#print("letitre de notre html:",texte_p.text)

#-------------recherche de attrib src de <img>-----------
div_info=soup.find("div", class_="info" )
img_info=div_info.find("img")
#print("le src de l'mage:",img_info["src"])