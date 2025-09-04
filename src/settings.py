from dataclasses import dataclass
import os

@dataclass
class Settings:
    timeout: int = int(os.getenv("HTTP_TIMEOUT", "20"))
    max_conc: int = int(os.getenv("MAX_CONCURRENCY", "4"))
    proxy: str | None = os.getenv("PROXY_URL") or None

SETTINGS = Settings()
