import requests
from bs4 import BeautifulSoup


def wikipedia_links_to_page(startPage, targetPage):
    jumps = 0
    jump_points = []
    uncrawled_pages = []
    done = False

    uncrawled_pages.append(crawl_wikipedia_page(startPage))

    while done != True and len(uncrawled_pages) != 0

        # add the links of the start page to the list
        

        for item in wikiText.findAll("a"):
            link = item["href"]
            
            if link == targetPage:
                print("We found the page with link: "+link)
                done = True
            
        if done == False:
            uncrawled_pages.append(crawl_wikipedia_page(uncrawled_pages[0][0]))
            del uncrawled_pages[0][0]
            if len(uncrawled_pages[0]) == 0:
                del uncrawled_pages[0]
    
    if done:
        print("The target page was found")
    else:
        print("the target page wasn't found")



def crawl_wikipedia_page(page):
    html = requests.get(startPage)
    plain_text = html.text
    soup = BeautifulSoup(plain_text, "html.parser")
    wikiText = soup.body.find("div", {"id": "mw-content-text"}).div

    return wikiText.findAll("a")


findWikiPageFromLinks("https://en.wikipedia.org/wiki/World_War_II", "https://en.wikipedia.org/wiki/Adolf_Hitler")