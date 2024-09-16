from bs4 import BeautifulSoup
import requests 
import re


items_found = {}



def newegg(search_term):
    url = f"https://www.newegg.com/p/pl?d={search_term}&N=4131"

    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    page_text = doc.find(class_ = "list-tool-pagination-text").strong
    pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])

    for page in range(1, pages + 1):
        url = f"https://www.newegg.com/p/pl?d={search_term}&N=4131&page={page}"
        page = requests.get(url).text
        doc = BeautifulSoup(page, "html.parser")
        div = doc.find(class_="item-cells-wrap border-cells short-video-box items-grid-view four-cells expulsion-one-cell")
        #own filter as some would not be actually the thing
        items = div.find_all(string = re.compile(search_term))
        for item in items:
            link = None
            parent = item.parent
            if parent.name != "a":
                continue
            
            link = parent['href']
            next_parent = item.find_parent(class_ = "item-container")
            try:
                price = next_parent.find(class_ = "price-current").strong.string
                items_found[item] = {"price" : int(price.replace(",", "")), "link" : link}
            except:
                pass
    return

def ebay(search_term):
    url = f"https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw={search_term}&_sacat=0&rt=nc&LH_ItemCondition=3"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    # page_text = doc.find(class_ = )

    return
     



search_term = "3080" #input("What product do you want to search for? ")
newegg(search_term)
sorted_items = sorted(items_found.items(), key = lambda x:x[1]['price'])



for item in sorted_items:
	print(item[0])
	print(f"${item[1]['price']}")
	print(item[1]['link'])
	print("-------------------------------")



        

        
