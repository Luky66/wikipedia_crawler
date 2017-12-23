# Safety note: This is ugly as hell and I know. Use at your own risk
# This was actually a project after I haven't touched python in about 7 years.

# Current Bugs:
# Doesn't work when having to search more than one page to find the target link

# To resolve I will need to restructure this and make it call recursively


import requests
from bs4 import BeautifulSoup


def wikipedia_links_to_page(startPage, targetPage):
    jumps = 0
    jump_points = []
    uncrawled_pages = []
    done = False

    uncrawled_pages.append(crawl_wikipedia_page(startPage))
    print("Started with "+str(len(uncrawled_pages[0]))+" links")

    while not done or not uncrawled_pages:

        # add the links of the start page to the list

        for item in uncrawled_pages[0]:
            link = item["href"]
            
            if link == targetPage:
                done = True
                break
            
        if not done:
            print("Crawling new page: "+str(uncrawled_pages[0][0]))
            jumps += 1

            uncrawled_pages.append(crawl_wikipedia_page(uncrawled_pages[0][0]["href"]))
            del uncrawled_pages[0][0]
            if not uncrawled_pages[0]:
                del uncrawled_pages[0]
    
    if done:
        print("The target page '"+targetPage+"' was found with "+str(jumps+1)+" jumps")
    else:
        print("the target page wasn't found")



def crawl_wikipedia_page(page):
    print("Crawling "+page)
    html = requests.get(page)
    plain_text = html.text
    soup = BeautifulSoup(plain_text, "html.parser")
    wiki_text = soup.body.find("div", {"id": "mw-content-text"}).div

    return wiki_text.findAll("a", {"href": True})


wikipedia_links_to_page("https://en.wikipedia.org/wiki/World_War_II", "/wiki/Adolf_Hitler")