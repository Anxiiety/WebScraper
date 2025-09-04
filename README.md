# scraping-plus

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
