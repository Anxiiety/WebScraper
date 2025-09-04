import argparse, pandas as pd
from pathlib import Path
from .providers import example_site
from .core.pipeline import to_csv, to_parquet, to_sqlite

def cmd_fetch(provider: str, out: str, url: str):
    if provider == "example_site":
        df = example_site.fetch_items(url or "https://example.com/shop")
    else:
        raise SystemExit(f"Unknown provider {provider}")
    to_csv(df, out)

def cmd_process(inp: str, out: str, to_sql=False):
    df = pd.read_csv(inp)
    to_parquet(df, out)
    if to_sql:
        to_sqlite(df, "data/db.sqlite", Path(out).stem)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    f = sub.add_parser("fetch")
    f.add_argument("--provider", required=True)
    f.add_argument("--out", required=True)
    f.add_argument("--url", default="")

    p = sub.add_parser("process")
    p.add_argument("--in", dest="inp", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--to-sqlite", action="store_true")

    args = ap.parse_args()
    if args.cmd=="fetch": cmd_fetch(args.provider, args.out, args.url)
    else: cmd_process(args.inp, args.out, args.to_sqlite)
