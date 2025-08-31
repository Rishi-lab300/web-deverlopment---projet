import pandas as pd
import matplotlib.pyplot as plt
#load the csv file
df = pd.read_csv("spotify_songs.csv")
df.dropna(subset=["track_name","artist_name","genre","duration_ms","year","popularity"])


genre_count = df['genre'].value_counts().head(5)
plt.figure(figsize=(6,4))
plt.bar(genre_count.index ,genre_count.values , color = ['skyblue'])
plt.title("Top 5 generes by number of songs")
plt.xlabel("Genres")
plt.ylabel("Number of songs")
plt.tight_layout()
plt.savefig("Genres_count.png")
plt.show()

songs_df = df.copy()
songs_df['duration_min'] = (df['duration_ms']/60000).round(2)
plt.figure(figsize=(8,6))
plt.hist(songs_df['duration_min'],bins=30,color='purple',edgecolor = 'black')
plt.title("Histogram of song duration")
plt.xlabel("Duration[minutes]")
plt.ylabel("Number of Songs")
plt.tight_layout()
plt.savefig("songs_duration_hist.png")
plt.show()

average_popularity = df.groupby('year')['popularity'].mean()
plt.figure(figsize=(7,4))
plt.plot(average_popularity.index,average_popularity.values,marker = 'o',color = 'gold')
plt.title("Popularity of songs per year")
plt.xlabel("Year")
plt.xticks(rotation=45)
plt.ylabel("Popularity of Songs")
plt.show()
# Make a copy of the dataset
songs_df = df.copy()

# Convert duration from ms to minutes
songs_df['duration_min'] = (songs_df['duration_ms'] / 60000).round(2)

# Scatter plot: duration vs popularity
plt.figure(figsize=(10,6))
plt.scatter(songs_df['duration_min'], songs_df['popularity'], color='black', alpha=0.6)
plt.title("Song Duration vs Popularity")
plt.xlabel("Duration [minutes]")
plt.ylabel("Popularity")
plt.tight_layout()
plt.savefig("duration_vs_popularity.png")
plt.show()




