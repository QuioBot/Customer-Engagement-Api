from requests_html import HTMLSession
from bs4 import BeautifulSoup

s = HTMLSession()


url = "https://www.amazon.com/Munchkin-Sponge-Bottle-Brush-Pack/product-reviews/B082PNG759/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"

def getdata(url):
    r = s.get(url)
    r.html.render(sleep=1)
    soup = BeautifulSoup(r.html.html, 'html.parser')
    return soup

print(getdata(url))

