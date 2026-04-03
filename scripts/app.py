import sqlite3
from pathlib import Path
import streamlit as st

# ----------------------------
# Paths
# ----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "vivino.db"
QUERIES_DIR = BASE_DIR / "queries" / "business_questions"
FIGURES_DIR = BASE_DIR / "outputs" / "figures"

# ----------------------------
# Page config
# ----------------------------
st.set_page_config(
    page_title="Vivino Market Analysis",
    page_icon="🍷",
    layout="wide",
)

# ----------------------------
# Helpers
# ----------------------------
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


def render_table(columns, rows):
    if not rows:
        st.warning("No results found.")
        return

    table_data = [dict(zip(columns, row)) for row in rows]
    st.dataframe(table_data, use_container_width=True, hide_index=True)


def show_chart(filename: str):
    figure_path = FIGURES_DIR / filename
    if figure_path.exists():
        st.image(str(figure_path), use_container_width=True)
    else:
        st.info(f"Chart not found: {filename}. Run `python scripts/charts.py` first.")


def metric_card(label: str, value: str):
    st.metric(label=label, value=value)


# ----------------------------
# Content maps
# ----------------------------
query_map = {
    "Executive Summary": None,
    "Top 10 Wines": "01_top_10_wines.sql",
    "Country Priority": "02_country_priority.sql",
    "Winery Awards": "03_winery_awards.sql",
    "Keyword Cluster": "04_keywords_cluster.sql",
    "Top 3 Grapes and Best Wines": "05_top_grapes_wines.sql",
    "Country Leaderboard": "06_country_leaderboard.sql",
    "Vintage Leaderboard": "07_vintage_leaderboard.sql",
    "Insight 1: Rating vs Popularity": "08_insight1_rating_vs_popularity.sql",
    "Insight 2: Countries with High Engagement": "08_insight2_countries_with_high_engagement.sql",
    "Insight 3: Keyword Popularity": "08_insight3_keyword_popularity.sql",
    "Cabernet Sauvignon Top 5": "09_cabernet_sauvignon_top5.sql",
}

figure_map = {
    "Top 10 Wines": "top_10_wines.png",
    "Country Priority": "country_priority_rating.png",
    "Winery Awards": "winery_awards.png",
    "Keyword Cluster": "keyword_cluster_distribution.png",
    "Top 3 Grapes and Best Wines": "top_grapes_wines.png",
    "Country Leaderboard": "country_leaderboard.png",
    "Vintage Leaderboard": "vintage_leaderboard.png",
    "Insight 1: Rating vs Popularity": "rating_vs_popularity.png",
    "Insight 2: Countries with High Engagement": "country_engagement.png",
    "Insight 3: Keyword Popularity": "keyword_popularity.png",
    "Cabernet Sauvignon Top 5": "cabernet_sauvignon_top5.png",
}

description_map = {
    "Top 10 Wines": "Top-rated wines selected using average rating and number of ratings.",
    "Country Priority": "Country comparison based on average rating, wine count, and average price.",
    "Winery Awards": "Creative award selection highlighting different dimensions of winery performance.",
    "Keyword Cluster": "Wines matching a specific taste cluster confirmed by more than 10 users.",
    "Top 3 Grapes and Best Wines": "Most common grapes worldwide and the best-rated wines associated with them.",
    "Country Leaderboard": "Average wine rating by country.",
    "Vintage Leaderboard": "Average wine rating by vintage year.",
    "Insight 1: Rating vs Popularity": "Explores the relationship between review volume and wine quality.",
    "Insight 2: Countries with High Engagement": "Shows which countries generate the most review activity.",
    "Insight 3: Keyword Popularity": "Highlights the most frequently mentioned flavor keywords.",
    "Cabernet Sauvignon Top 5": "Top recommendations for a Cabernet Sauvignon lover.",
}

insight_map = {
    "Top 10 Wines": "These wines combine high scores with strong review volume, making them strong commercial candidates.",
    "Country Priority": "This section helps identify the best country to prioritize by balancing quality, market size, and price positioning.",
    "Winery Awards": "The awards highlight quality, popularity, and discovery potential across wineries.",
    "Keyword Cluster": "This cluster helps identify wines aligned with a strong and specific customer taste profile.",
    "Top 3 Grapes and Best Wines": "These wines represent globally common grape styles and strong market accessibility.",
    "Country Leaderboard": "This ranking highlights which countries perform best on average.",
    "Vintage Leaderboard": "This timeline helps compare wine quality across years.",
    "Insight 1: Rating vs Popularity": "The scatter plot shows whether highly rated wines also tend to attract more reviews.",
    "Insight 2: Countries with High Engagement": "High review volumes indicate stronger customer activity and market interest.",
    "Insight 3: Keyword Popularity": "Frequent flavor notes reveal dominant consumer preferences.",
    "Cabernet Sauvignon Top 5": "These recommendations target a VIP client seeking strong Cabernet Sauvignon options.",
}

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.title("Navigation")
section = st.sidebar.radio(
    "Go to",
    list(query_map.keys()),
)

st.sidebar.markdown("---")
st.sidebar.caption("Data source: SQLite + dedicated SQL files")
st.sidebar.caption("Charts source: outputs/figures")

# ----------------------------
# Header
# ----------------------------
st.title("🍷 Vivino Market Analysis")
st.markdown(
    """
This dashboard presents the main business analysis built from the Vivino SQLite database.
All sections are powered directly by SQL queries stored in dedicated `.sql` files.
"""
)

# ----------------------------
# Executive Summary page
# ----------------------------
if section == "Executive Summary":
    c1, c2, c3 = st.columns(3)
    with c1:
        metric_card("Business Questions", "9")
    with c2:
        metric_card("Insights", "3")
    with c3:
        metric_card("VIP Recommendation", "1")

    st.markdown("---")

    left, right = st.columns([1.3, 1])

    with left:
        st.subheader("Project Scope")
        st.markdown(
            """
- Identify top wines to promote  
- Select the best country to prioritize  
- Create winery awards  
- Analyze customer taste clusters  
- Compare countries and vintages  
- Add useful market insights  
- Recommend top Cabernet Sauvignon wines  
"""
        )

        st.subheader("Important Limitation")
        st.markdown(
            """
The dataset does **not** contain a direct wine-to-grape relationship.
For grape analysis, wines are associated through country-level grape prevalence or name-based approximation.
"""
        )

    with right:
        summary_chart = FIGURES_DIR / "country_priority_rating.png"
        if summary_chart.exists():
            st.image(str(summary_chart), caption="Example: country priority view", use_container_width=True)
        else:
            st.info("Run `python scripts/charts.py` to generate the saved charts.")

# ----------------------------
# Section pages
# ----------------------------
else:
    selected_query = query_map[section]
    columns, rows = run_query(selected_query)

    st.subheader(section)
    st.write(description_map[section])

    kpi1, kpi2, kpi3 = st.columns(3)

    with kpi1:
        metric_card("Rows Returned", str(len(rows)))

    with kpi2:
        st.markdown("**SQL File**")
        st.code(selected_query)

    with kpi3:
        metric_card("Chart Available", "Yes" if (FIGURES_DIR / figure_map[section]).exists() else "No")

    st.markdown("---")

    chart_col, table_col = st.columns([1.2, 1])

    with chart_col:
        show_chart(figure_map[section])

    with table_col:
        st.markdown("### Result Table")
        render_table(columns, rows)

    st.markdown("---")
    st.markdown("### Business Interpretation")
    st.write(insight_map[section])

    with st.expander("Show SQL file used"):
        st.code((QUERIES_DIR / selected_query).read_text(encoding="utf-8"), language="sql")
