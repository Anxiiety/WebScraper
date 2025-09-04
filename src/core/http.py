import httpx
from fake_useragent import UserAgent
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from ..settings import SETTINGS
from .robots import is_allowed

ua = UserAgent()

@retry(stop=stop_after_attempt(4), wait=wait_exponential(1, 4),
       retry=retry_if_exception_type(httpx.HTTPError))
def fetch(url: str) -> str:
    if not is_allowed(url):
        raise PermissionError(f"Disallowed by robots.txt: {url}")
    headers = {"User-Agent": ua.random}
    proxies = {"all://": SETTINGS.proxy} if SETTINGS.proxy else None
    with httpx.Client(http2=True, timeout=SETTINGS.timeout, proxies=proxies, headers=headers) as c:
        r = c.get(url)
        r.raise_for_status()
        return r.text
