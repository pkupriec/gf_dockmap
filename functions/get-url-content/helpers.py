from bs4 import BeautifulSoup, NavigableString

def strip_html(src):
    p = BeautifulSoup(src)
    text = p.findAll(text=lambda text:isinstance(text, NavigableString))

    return u" ".join(text)