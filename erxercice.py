from tracemalloc import start
import requests
from bs4 import BeautifulSoup


#1-extraire tous les categorie du site
    #----------------cat1----
url_principal='https://just-scrape-it.com/collections/'
url='https://just-scrape-it.com/collections/hoodie-sweat'
url1='https://just-scrape-it.com/collections/tshirt-t-shirt-tee-shirt'
url2='https://just-scrape-it.com/products/cagoule-scrape-original'
url3='ttps://just-scrape-it.com/collections/gants'
url4='https://just-scrape-it.com/collections/maillots-ete'
url5='https://just-scrape-it.com/collections/sticke'

urls=['hoodie-sweat','tshirt-t-shirt-tee-shirt','cagoule-scrape-original','gants','maillots-ete','sticke']
ind=0

reponse1 = requests.get(url)
# print(reponse1)
# while  ind <6:
#     reponse=requests.get(url_principal+'hoodie-sweat')
#     reponse.ok 
#     soup =BeautifulSoup(reponse.text,"html.parser")
#     for (i, cate)in enumerate(soup.find('title')):
#             print("categorie:",i)
#             print("\n Nom de la categorié: ",cate.text)
#     ind+1
if reponse1.ok:
    #print(reponse1)#headers,bodys,text
    soup =BeautifulSoup(reponse1.text,"html.parser")

    #l'image du div 
    title_categorie=soup.find('title')
    info_div=soup.find('ul',class_='grid grid--uniform grid--view-items')
    
    info_img=soup.find_all('li', class_='grid__item grid__item--collection-template small--one-half medium-up--one-quarter')
    title_image=soup.find('div',class_='h4 grid-view-item__title product-card__title')
    price_title=soup.find('span',class_='visually-hidden visually-hidden--inline')
    price=soup.find('span',class_='price-item price-item--regular')
    

    #--------les infos à afficher-----------
    #print("\ninfo:",info_div,"\n")
    #print("\n-le title de la categorie:\n","\t",title_categorie.text,"\n")
    #for info_title_img in title_images.text:
    if info_div:
       
        print("\n-le title de la categorie:\n",title_categorie.text,"\n")

        #print(len(info_img))
        for (i,u) in enumerate(info_img):
            price_regular=u.find('span',class_='price-item price-item--regular')
            if price_regular.text !='Épuisé':
                print("Article:***********", i, "************")
                
                titre_image = u.find('div',class_='h4 grid-view-item__title product-card__title')
                print("\n_Le title des images:",titre_image.text,"\n")
                price_image=u.find('span',class_='price-item price-item--sale')
                
                print("\nLe prix est: ",price_image.text)
                img=u.find('img')
                print("https:" + img['src'],'\n')
            
                print("-------------")
                #div_image_title=titre_categorie.find_all('div',class_='grid-view-item__image-wrapper product-card__image-wrapper js')
                #print("\n_Le src des images:",div_image_title,"\n")
                # for o in div_image_title.find_all('img'):
                #     print("\n_Le src des images:",o['src'],"\n")

            
            
    # print("\n-le src de l'image:",info_img['src'],"\n")
    # print("\n_Le title de l'image:",title_image.text,"\n")
    # print("\n_Le price title:",price_title.text,"& le prix:",price.text,"\n")
    #----------------cat2----
url1='https://just-scrape-it.com/collections/hoodie-sweat'
reponse1 = requests.get(url)

if reponse1.ok:
    #print(reponse)#headers,bodys,text
    soup =BeautifulSoup(reponse1.text,"html.parser")
    title=soup.find('title')
    #print("\nle titre:",title,"\n")
# 2- Ensuite, extraire les articles de chaque categories
#     donnés à extraire:
#     - titre
#     - prix
#     - images
# nb: Ces articles doivent etre en stock
