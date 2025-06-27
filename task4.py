import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium

# Ensure UTF-8 encoding for terminals that support it
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Load dataset
print("Loading dataset...")
df = pd.read_csv(r"task4.csv", low_memory=False, nrows=100000)
print("Dataset loaded successfully!")
print("Shape:", df.shape)
print("Columns:", list(df.columns))

# Show sample data
print("\nSample Data:\n", df[['Start_Time', 'Weather_Condition']].head())

# Convert time and extract features
df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')
df['Hour'] = df['Start_Time'].dt.hour
df['Weekday'] = df['Start_Time'].dt.day_name()

# Drop rows with missing essential data
df = df.dropna(subset=['Start_Lat', 'Start_Lng', 'Weather_Condition', 'Start_Time'])

# Plot: Accidents by Hour
plt.figure(figsize=(10, 5))
sns.countplot(x='Hour', data=df, palette='mako')
plt.title('Accidents by Hour of the Day')
plt.xlabel('Hour (0–23)')
plt.ylabel('Number of Accidents')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# Plot: Top 10 Weather Conditions
plt.figure(figsize=(12, 6))
top_weather = df['Weather_Condition'].value_counts().nlargest(10).index
sns.countplot(y='Weather_Condition',
              data=df[df['Weather_Condition'].isin(top_weather)],
              order=top_weather,
              palette='coolwarm')
plt.title('Top 10 Weather Conditions During Accidents')
plt.xlabel('Number of Accidents')
plt.ylabel('Weather Condition')
plt.tight_layout()
plt.show()

# Plot: Accidents by Day of the Week
plt.figure(figsize=(10, 5))
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
sns.countplot(x='Weekday', data=df, order=weekday_order, palette='crest')
plt.title('Accidents by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Accidents')
plt.tight_layout()
plt.show()

# Accident Hotspot Map
print("\nGenerating accident hotspot map using 500 sample points...")
sample = df[['Start_Lat', 'Start_Lng']].dropna().sample(500)

accident_map = folium.Map(location=[sample['Start_Lat'].mean(), sample['Start_Lng'].mean()],
                          zoom_start=5, tiles='CartoDB positron')

for i in sample.itertuples():
    folium.CircleMarker(
        location=[i.Start_Lat, i.Start_Lng],
        radius=2,
        color='red',
        fill=True,
        fill_opacity=0.4
    ).add_to(accident_map)

accident_map.save("accident_hotspots_map.html")
print("Map saved as 'accident_hotspots_map.html'")

# Summary
print("\nSUMMARY OF INSIGHTS")
print("-" * 50)
print("Top 5 Weather Conditions:")
print(df['Weather_Condition'].value_counts().head(5))
print("-" * 50)
print("Most Accident-Prone Hours:")
print(df['Hour'].value_counts().sort_values(ascending=False).head(5))
print("-" * 50)
print("Accidents by Day of the Week:")
print(df['Weekday'].value_counts())
print("-" * 50)

input("\nTask Completed. Press Enter to exit...")
