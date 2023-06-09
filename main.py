import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com/"
r=requests.get(url)
html= r.content
# print(html)
# print("ehllo")
soup=BeautifulSoup(html,'html.parser')
# print(soup.prettify)
# title=soup.title
# #html tree traversal

# # tag
# print("tag type")
# print(type(title))
# print("navgation string")
# # navigablestring
# print(type(title.string))
# print("beutiful soup")
# # BeautifulSoup
# print(type(soup)) 
# print("comment")
# #comment
# markup = "<p><!-- this is a comment --></p>"
# soup2=BeautifulSoup(markup)
# print(soup2.p.string)


# #print all paragarh
# para=soup.find_all("p")  
# print(para)
# #print all anchor 
# anc=soup.find_all("a")
# print(anc)
# #first p tag
# print(soup.find("p"))
# print(soup.find("p")['class'])

# #find all the element with class lead
# print(soup.find_all("p",class_="mt-2"))
# #get text from the element
# print("first p ele text")
# print(soup.find("p").get_text())
# print("all text")
# print(soup.get_text())


# #get all the anchor 
# anchors= soup.find_all('a')

# all_link=set()
# for link in anchors:
#     if(link.get('href') !='#'):
#      all_link.add("https://codewithharry.com"+link.get('href'))
     
# for link in all_link:
#    print(link)
# print("BY ID SCRAPING")
id=soup.find(id="__next")
# for ele in id.children:
#     print(ele)
#CHINDRAN IS NOT STORE IN MEMORY this iterable but not direct print although both are same kind of nature
#CONTANT STORE IN MEMORY

# print("SOME INTERATION MATHOD RUN THIS LOOP WITH ONLY STRING METHODS")
# for item in id.stripped_strings:
#     print(item)
# print("PRINT PARENT TAG")
# print(id.parent)
# print("parants method is a  like gentrator can be iterable")
# for ele in id.parents:
#     print(ele.name)
# print("sibling")
# print(id.next_sibling)
# print(id.previous_sibling)
#print("CSS SELECTOR")
# ele =soup.select('#loginmodal')
# print(ele)