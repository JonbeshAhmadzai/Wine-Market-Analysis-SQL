import csv
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "vivino.db"
QUERIES_DIR = BASE_DIR / "queries" / "business_questions"
TABLES_DIR = BASE_DIR / "outputs" / "tables"

TABLES_DIR.mkdir(parents=True, exist_ok=True)


def run_query(query_filename: str):
    query_path = QUERIES_DIR / query_filename

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    with open(query_path, "r", encoding="utf-8") as f:
        query = f.read()

    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description] if cursor.description else []

    conn.close()
    return columns, rows


def save_table_csv(query_filename: str, output_filename: str):
    columns, rows = run_query(query_filename)
    filepath = TABLES_DIR / output_filename

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(columns)
        writer.writerows(rows)

    print(f"Saved: {filepath}")


if __name__ == "__main__":
    save_table_csv("01_top_10_wines.sql", "top_10_wines.csv")
    save_table_csv("02_country_priority.sql", "country_priority.csv")
    save_table_csv("03_winery_awards.sql", "winery_awards.csv")
    save_table_csv("04_keywords_cluster.sql", "keywords_cluster.csv")
    save_table_csv("05_top_grapes_wines.sql", "top_grapes_wines.csv")
    save_table_csv("06_country_leaderboard.sql", "country_leaderboard.csv")
    save_table_csv("07_vintage_leaderboard.sql", "vintage_leaderboard.csv")
    save_table_csv("08_insight1_rating_vs_popularity.sql", "insight1_rating_vs_popularity.csv")
    save_table_csv("08_insight2_countries_with_high_engagement.sql", "insight2_countries_with_high_engagement.csv")
    save_table_csv("08_insight3_keyword_popularity.sql", "insight3_keyword_popularity.csv")
    save_table_csv("09_cabernet_sauvignon_top5.sql", "cabernet_sauvignon_top5.csv")
 