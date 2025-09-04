import urllib.robotparser as rp
from urllib.parse import urlparse, urljoin
import functools

@functools.lru_cache(maxsize=256)
def _rp(base: str):
    rob = rp.RobotFileParser()
    rob.set_url(urljoin(base, "/robots.txt"))
    try: rob.read()
    except: pass
    return rob

def is_allowed(url: str, agent="*") -> bool:
    o = urlparse(url)
    base = f"{o.scheme}://{o.netloc}"
    return _rp(base).can_fetch(agent, url)
