import pandas as pd

from datetime import datetime
import time
import logging

logging.basicConfig(
    filename="hotstar_automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

file_path = r"C:\Users\nishi\OneDrive\DA training\3. Disney + Jiohotstar\jiohotstar_sample_dataset.csv"

df = pd.read_csv(file_path)
print(df.head())
print("Dataset Shape:", df.shape)
print("Column Names:", df.columns.tolist())
df.info()

print(df.isnull().sum())
print("Total Duplicate Rows:", df.duplicated().sum())
print(df.describe())

print(df["content_type"].value_counts())
print(df["genre"].value_counts())
print(df["language"].value_counts())

print(df.groupby("content_type")["imdb_rating"].mean())

print(df.groupby("genre")["imdb_rating"].mean().sort_values(ascending=False))
print(df[["title", "content_type", "genre", "imdb_rating"]].sort_values(by="imdb_rating",ascending=False).head(10))

print(df[(df["content_type"] == "Movie") & (df["imdb_rating"] > 8)])

print(df[(df["release_year"] >= 2018) & (df["release_year"] <= 2022)])
print(df[(df["imdb_rating"]>=7)&(df["imdb_rating"]<=8)])

print(df[(df["content_type"] == "Movie")&(df["duration_minutes"]>=90)&(df["duration_minutes"]<=150)])

print(df[df["duration_minutes"].isnull()])
print(df["duration_minutes"].isnull().sum())
print(df["duration_minutes"].notnull().sum())

print(df.groupby("language")["imdb_rating"].mean().sort_values(ascending=False))

print(df["country"].value_counts())
print(df["country"].value_counts().head(3))

print(df["release_year"].sort_values(ascending=True))

print(df.sort_values(by="release_year", ascending=True))
print(df.sort_values(by="imdb_rating", ascending=False))

print(df[(df["content_type"] == "TV Show") & (df["seasons"] > 2)])
print(df[(df["content_type"] == "TV Show") & (df["episodes"] > 20)])
print(df[(df["content_type"] == "Movie") & (df["imdb_rating"] > 8.5)])

print(df[df["release_year"] > 2020])
print(df[df["imdb_rating"] < 6])


def run_analysis():
    print(df.describe())

run_analysis()


def validate_data():

    print("\n--- DATA QUALITY CHECK ---")

    total_rows = len(df)

    missing_titles = df["title"].isnull().sum()

    duplicate_ids = df["content_id"].duplicated().sum()

    invalid_ratings = (
        (df["imdb_rating"] < 0) |
        (df["imdb_rating"] > 10)
    ).sum()

    print("Total Rows:", total_rows)
    print("Missing Titles:", missing_titles)
    print("Duplicate Content IDs:", duplicate_ids)
    print("Invalid IMDb Ratings:", invalid_ratings)

    if (
        missing_titles == 0
        and duplicate_ids == 0
        and invalid_ratings == 0
    ):
        print("Data Quality: PASSED")
    else:
        print("Data Quality: NEEDS REVIEW")

validate_data()


def export_quality_report():

    total_rows = len(df)
    missing_titles = df["title"].isnull().sum()
    duplicate_ids = df["content_id"].duplicated().sum()

    invalid_ratings = (
        (df["imdb_rating"] < 0) |
        (df["imdb_rating"] > 10)
    ).sum()

    quality_data = {
        "Check": [
            "Total Rows",
            "Missing Titles",
            "Duplicate Content IDs",
            "Invalid IMDb Ratings"
        ],
        "Result": [
            total_rows,
            missing_titles,
            duplicate_ids,
            invalid_ratings
        ]
    }

    quality_df = pd.DataFrame(quality_data)

    quality_df.to_excel(
        "hotstar_data_quality_report.xlsx",
        index=False
    )

    print("Data Quality Report Exported Successfully!")


def generate_kpis():

    # Existing KPI calculations
    total_titles = len(df)
    total_movies = (df["content_type"] == "Movie").sum()
    total_tvshows = (df["content_type"] == "TV Show").sum()
    avg_imdb = round(df["imdb_rating"].mean(), 2)
    max_imdb = df["imdb_rating"].max()

    # Existing KPI DataFrame
    kpi_data = {
        "KPI": ["Total Titles", "Total Movies", "Total TV Shows",
                "Average IMDb Rating", "Highest IMDb Rating"],
        "Value": [total_titles, total_movies, total_tvshows,
                  avg_imdb, max_imdb]
    }

    kpi_df = pd.DataFrame(kpi_data)

    # Timestamp code 
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Updated Excel filename 
    filename = f"hotstar_report_{timestamp}.xlsx"

    # Export
    try:
        kpi_df.to_excel(filename, index=False)
        print("Report generated successfully!")
        print("Report saved as:", filename)
        logging.info("KPI report generated successfully: %s", filename)


    except Exception as e:
        print("Report generation failed:", e)
        logging.error("Report generation failed: %s", e)

# Function call 
generate_kpis()


while True:
   generate_kpis()
time.sleep(10)


def automation_pipeline():
    try:
        print("Automation started")

        generate_kpis()

        logging.info("Automation completed successfully")
        print("Automation completed successfully")

    except Exception as e:
        logging.error("Automation failed: %s", e)
        print("Automation failed:", e)

    validate_data()
    export_quality_report()
    generate_kpis()


automation_pipeline()

