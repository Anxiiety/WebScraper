import pandas as pd
from ..core.http import fetch
from ..core.parsers import select_text

def fetch_items(url: str) -> pd.DataFrame:
    html = fetch(url)
    titles = select_text(html, ".product-card .title")
    prices = select_text(html, ".product-card .price")
    clean = []
    for t, p in zip(titles, prices):
        try: v = float(p.replace("€","").replace(",","." ).strip())
        except: v = None
        clean.append({"title": t, "price": v})
    return pd.DataFrame(clean)
import pandas as pd
from ..core.http import fetch
from ..core.parsers import select_text

def fetch_items(url: str) -> pd.DataFrame:
    html = fetch(url)
    titles = select_text(html, ".product-card .title")
    prices = select_text(html, ".product-card .price")
    clean = []
    for t, p in zip(titles, prices):
        try: v = float(p.replace("€","").replace(",","." ).strip())
        except: v = None
        clean.append({"title": t, "price": v})
    return pd.DataFrame(clean)
