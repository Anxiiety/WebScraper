from bs4 import BeautifulSoup

def select_text(html: str, css: str):
    soup = BeautifulSoup(html, "lxml")
    return [el.get_text(strip=True) for el in soup.select(css)]
