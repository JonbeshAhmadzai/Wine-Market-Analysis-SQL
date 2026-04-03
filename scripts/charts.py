import sqlite3
from pathlib import Path
from collections import Counter
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "vivino.db"
QUERIES_DIR = BASE_DIR / "queries" / "business_questions"
FIGURES_DIR = BASE_DIR / "outputs" / "figures"

FIGURES_DIR.mkdir(parents=True, exist_ok=True)


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


def save_figure(filename: str):
    plt.savefig(FIGURES_DIR / filename, dpi=300, bbox_inches="tight")


def plot_top_wines():
    columns, rows = run_query("01_top_10_wines.sql")

    wine_names = [row[0] for row in rows]
    ratings = [row[3] for row in rows]

    plt.figure(figsize=(10, 6))
    plt.barh(wine_names, ratings)
    plt.gca().invert_yaxis()
    plt.title("Top 10 Wines by Rating")
    plt.xlabel("Average Rating")
    plt.ylabel("Wine")
    plt.tight_layout()
    save_figure("top_10_wines.png")
    plt.show()


def plot_country_priority_rating():
    columns, rows = run_query("02_country_priority.sql")

    country_names = [row[0] for row in rows]
    avg_ratings = [row[1] for row in rows]

    plt.figure(figsize=(8, 5))
    plt.bar(country_names, avg_ratings)
    plt.title("Average Wine Rating by Country")
    plt.xlabel("Country")
    plt.ylabel("Average Rating")
    plt.xticks(rotation=45)
    plt.tight_layout()
    save_figure("country_priority_rating.png")
    plt.show()


def plot_country_priority_bubble():
    columns, rows = run_query("02_country_priority.sql")

    country_names = [row[0] for row in rows]
    avg_ratings = [row[1] for row in rows]
    wine_counts = [row[2] for row in rows]
    avg_prices = [row[3] for row in rows]

    plt.figure(figsize=(8, 6))
    plt.scatter(avg_prices, avg_ratings, s=[count * 2 for count in wine_counts])

    for i, country in enumerate(country_names):
         plt.text(avg_prices[i], avg_ratings[i], country)

    plt.title("Country Positioning: Price vs Rating")
    plt.xlabel("Average Price")
    plt.ylabel("Average Rating")
    plt.tight_layout()
    save_figure("country_priority_bubble.png")
    plt.show()


def plot_winery_awards():
    columns, rows = run_query("03_winery_awards.sql")

    winery_names = [row[0] for row in rows]
    ratings = [row[2] for row in rows]

    plt.figure(figsize=(10, 5))
    plt.bar(winery_names, ratings)
    plt.title("Winery Awards")
    plt.xlabel("Winery")
    plt.ylabel("Average Rating")
    plt.xticks(rotation=45)
    plt.tight_layout()
    save_figure("winery_awards.png")
    plt.show()


def plot_keyword_cluster_distribution():
    columns, rows = run_query("04_keywords_cluster.sql")

    matched_counts = [row[3] for row in rows]
    count_distribution = Counter(matched_counts)

    x = sorted(count_distribution.keys())
    y = [count_distribution[k] for k in x]

    plt.figure(figsize=(8, 5))
    plt.bar(x, y)
    plt.title("Distribution of Keyword Matches per Wine")
    plt.xlabel("Matched Keyword Count")
    plt.ylabel("Number of Wines")
    plt.tight_layout()
    save_figure("keyword_cluster_distribution.png")
    plt.show()


def plot_top_grapes_wines():
    columns, rows = run_query("05_top_grapes_wines.sql")

    labels = [f"{row[0]} - {row[1]}" for row in rows]
    ratings = [row[3] for row in rows]

    plt.figure(figsize=(12, 8))
    plt.barh(labels, ratings)
    plt.gca().invert_yaxis()
    plt.title("Top 5 Wines for Each of the Top 3 Grapes")
    plt.xlabel("Average Rating")
    plt.ylabel("Grape - Wine")
    plt.tight_layout()
    save_figure("top_grapes_wines.png")
    plt.show()


def plot_country_leaderboard():
    columns, rows = run_query("06_country_leaderboard.sql")

    country_names = [row[0] for row in rows]
    avg_ratings = [row[1] for row in rows]

    plt.figure(figsize=(8, 6))
    plt.barh(country_names, avg_ratings)
    plt.gca().invert_yaxis()
    plt.title("Country Leaderboard: Average Wine Rating")
    plt.xlabel("Average Rating")
    plt.ylabel("Country")
    plt.tight_layout()
    save_figure("country_leaderboard.png")
    plt.show()


def plot_vintage_leaderboard():
    columns, rows = run_query("07_vintage_leaderboard.sql")

    clean_rows = [
        (int(row[0]), row[1])
        for row in rows
        if row[0] is not None and str(row[0]).isdigit()
    ]
    clean_rows = sorted(clean_rows, key=lambda x: x[0])

    years = [row[0] for row in clean_rows]
    ratings = [row[1] for row in clean_rows]

    plt.figure(figsize=(10, 5))
    plt.plot(years, ratings)
    plt.title("Average Rating by Vintage Year")
    plt.xlabel("Year")
    plt.ylabel("Rating")
    plt.xticks(years[::5], rotation=45)
    plt.tight_layout()
    save_figure("vintage_leaderboard.png")
    plt.show()


def plot_rating_vs_popularity():
    columns, rows = run_query("08_insight1_rating_vs_popularity.sql")

    ratings = [row[1] for row in rows]
    review_counts = [row[2] for row in rows]

    plt.figure(figsize=(8, 5))
    plt.scatter(review_counts, ratings)
    plt.title("Rating vs Popularity")
    plt.xlabel("Number of Ratings")
    plt.ylabel("Average Rating")
    plt.grid(True)
    plt.tight_layout()
    save_figure("rating_vs_popularity.png")
    plt.show()


def plot_country_engagement():
    columns, rows = run_query("08_insight2_countries_with_high_engagement.sql")

    country_names = [row[0] for row in rows]
    total_reviews = [row[2] for row in rows]

    plt.figure(figsize=(10, 5))
    plt.bar(country_names, total_reviews)
    plt.title("Countries with Highest User Engagement")
    plt.xlabel("Country")
    plt.ylabel("Total Reviews")
    plt.xticks(rotation=45)
    plt.tight_layout()
    save_figure("country_engagement.png")
    plt.show()


def plot_keyword_popularity():
    columns, rows = run_query("08_insight3_keyword_popularity.sql")

    keyword_names = [row[0] for row in rows[:10]]
    total_mentions = [row[1] for row in rows[:10]]

    plt.figure(figsize=(10, 6))
    plt.barh(keyword_names, total_mentions)
    plt.gca().invert_yaxis()
    plt.title("Top 10 Most Popular Flavor Keywords")
    plt.xlabel("Total Mentions")
    plt.ylabel("Keyword")
    plt.tight_layout()
    save_figure("keyword_popularity.png")
    plt.show()


def plot_cabernet_top5():
    columns, rows = run_query("09_cabernet_sauvignon_top5.sql")

    wine_names = [row[0] for row in rows]
    ratings = [row[2] for row in rows]

    plt.figure(figsize=(10, 5))
    plt.barh(wine_names, ratings)
    plt.gca().invert_yaxis()
    plt.title("Top 5 Cabernet Sauvignon Wines")
    plt.xlabel("Average Rating")
    plt.ylabel("Wine")
    plt.tight_layout()
    save_figure("cabernet_sauvignon_top5.png")
    plt.show()


if __name__ == "__main__":
    plot_top_wines()
    plot_country_priority_rating()
    plot_country_priority_bubble()
    plot_winery_awards()
    plot_keyword_cluster_distribution()
    plot_top_grapes_wines()
    plot_country_leaderboard()
    plot_vintage_leaderboard()
    plot_rating_vs_popularity()
    plot_country_engagement()
    plot_keyword_popularity()
    plot_cabernet_top5()