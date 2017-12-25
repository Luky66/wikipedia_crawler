# Safety note: This is ugly as hell and I know. Use at your own risk
# This was actually a project after I haven't touched python in about 7 years.

# Current Bugs:
# Doesn't work when having to search more than one page to find the target link

# To resolve I will need to restructure this and make it call recursively

"This module crawls the web for you."

import re
import requests
from bs4 import BeautifulSoup


def wikipedia_links_to_page(start_page, target_page, max_link_jumps):
    """
        This function counts the link jumps needed
        from a Wikipedia start page to a Wikipedia target page.
    """

    depth = 0
    links_of_same_depth = []
    child_links = []
    done = False

    links_of_same_depth.append(start_page)

    while not done:

        for link in links_of_same_depth:
            new_links = crawl_wikipedia_page(link)

            for new_link in new_links:
                if new_link == target_page:
                    done = True
                    break

            if done:
                break
            else:
                child_links.append(new_links)

        if done:
            print("Found the page "+str(depth+1)+" link(s) away!")
        else:
            if depth+1 >= max_link_jumps:
                print("Exiting... Page not found at max depth "+depth)
                done = True
            else:
                if not child_links:
                    print("Going deeper...")
                    links_of_same_depth = child_links
                    child_links = []
                    depth += 1
                else:
                    print("Exiting... Came to a dead end.")
                    done = True





def crawl_wikipedia_page(page_link):
    """
        returns a list with all the the links of a wikipedia page to different wikipedia pages
    """

    print("Crawling "+str(page_link))
    html = requests.get(page_link)
    plain_text = html.text
    soup = BeautifulSoup(plain_text, "html.parser")
    wiki_text = soup.body.find("div", {"id": "mw-content-text"}).div

    link_items = wiki_text.findAll("a", {"href": re.compile("/wiki/.*")})

    links = []
    for item in link_items:
        links.append("https://en.wikipedia.org"+item["href"])

    print("Found "+str(len(links))+" links crawling")
    return links


wikipedia_links_to_page(
    "https://en.wikipedia.org/wiki/World_War_II",
    "https://en.wikipedia.org/wiki/Adolf_Hitler",
    3)
