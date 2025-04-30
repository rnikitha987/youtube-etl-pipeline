# 🎥 YouTube ETL Pipeline with Python, BigQuery & GitHub Actions

This project automates the extraction of YouTube video data related to a specific topic (e.g., "data engineering"), transforms the data, and loads it into Google BigQuery — all on a daily schedule using GitHub Actions.

## 🚀 Features
- ⏱️ Scheduled daily ETL pipeline via GitHub Actions
- 🔍 Fetches YouTube videos using the YouTube Data API v3
- 🧼 Cleans and structures data with pandas
- ☁️ Loads data to BigQuery using Google Cloud service account
- 📈 Ready for dashboard integration (Looker Studio or Streamlit)

## 📊 Technologies Used
- Python
- Pandas
- YouTube Data API v3
- Google BigQuery
- GitHub Actions
- PyArrow (for DataFrame upload)

## 🛠 How It Works
1. **Python script** fetches videos on a keyword (e.g. `"data engineering"`)
2. Results are transformed into a pandas DataFrame
3. The data is uploaded to a BigQuery table:  
   `youtubeetlproject-456420.youtube_data.youtube_videos`
4. **GitHub Actions** automates daily execution at 9AM EST

## 📎 Sample Query in BigQuery

```sql
SELECT channel, COUNT(*) AS video_count
FROM `youtubeetlproject-456420.youtube_data.youtube_videos`
GROUP BY channel
ORDER BY video_count DESC
LIMIT 10;
