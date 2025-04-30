from googleapiclient.discovery import build
from google.cloud import bigquery
import pandas as pd
import matplotlib.pyplot as plt

# 🔑 YouTube API Key
API_KEY = "AIzaSyD1mmTcKoMkp-uCVapXWoGjrCnjYBW6yMU"  

# 🔍 Fetch data from YouTube API
youtube = build("youtube", "v3", developerKey=API_KEY)
request = youtube.search().list(
    q="data engineering",
    part="snippet",
    maxResults=10,
    type="video"
)
response = request.execute()

# 📊 Transform response into a DataFrame
videos = [{
    'videoId': item['id']['videoId'],
    'title': item['snippet']['title'],
    'channel': item['snippet']['channelTitle'],
    'publishedAt': item['snippet']['publishedAt']
} for item in response['items']]

df = pd.DataFrame(videos)
df['publishedAt'] = pd.to_datetime(df['publishedAt'], errors='coerce')

# 🟦 Upload to BigQuery
project_id = "youtubeetlproject-456420"
client = bigquery.Client.from_service_account_json("key.json")

table_ref = f"{project_id}.youtube_data.youtube_videos"
job_config = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")

job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
job.result()

print(f"✅ Uploaded {job.output_rows} rows to {table_ref}")

# 📈 Optional: Plot video uploads over time
df['publishedAt'].dt.date.value_counts().sort_index().plot(kind='bar', figsize=(12, 4), title="YouTube Videos by Date")
plt.xlabel("Date")
plt.ylabel("Video Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 📊 Optional: Top channels
df['channel'].value_counts().head(5).plot(kind='bar', title="Top 5 Channels by Video Count")
plt.xlabel("Channel")
plt.ylabel("Videos")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


