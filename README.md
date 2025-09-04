<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  <img src="https://img.shields.io/badge/Status-Alpha-orange" alt="Status">
  <img src="https://img.shields.io/github/stars/<TUO_USER>/scraping-plus?style=social" alt="Stars">
</p>


# Scraping-Plus

Toolkit di scraping modulare e robusto in **Python**:
- Rispetta `robots.txt`
- Retry & backoff (tenacity)
- User-Agent rotation + supporto proxy
- Parsing HTML con BeautifulSoup + lxml
- Pipeline dati verso **CSV**, **Parquet**, **SQLite**
- CLI con provider plug-in

## 🚀 Installazione
```bash
git clone https://github.com/<TUO_USER>/scraping-plus.git
cd scraping-plus
python -m venv .venv
source .venv/bin/activate   # su Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
