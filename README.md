# SCT_DS_4
# 🚧 Task 4: Exploratory Data Analysis on US Accidents Dataset

## 📌 Objective
The goal of this task is to perform **Exploratory Data Analysis (EDA)** on a large-scale accident dataset. This helps uncover patterns in road accidents based on time, day, weather, and location.

---

## 📂 Dataset
- **Source**: Provided as `task4.csv`
- **Size**: ~658MB
- **Sample Size Used**: 100,000 rows (due to performance constraints)

---

## 🔍 Analysis Performed
- Conversion of timestamps into useful features like **hour of day** and **day of week**
- Filtering and cleaning of relevant data (e.g., handling nulls)
- Visualizations:
  - Accidents by **hour of day**
  - Accidents under **top 10 weather conditions**
  - Accidents across **days of the week**
- **Interactive map** showing 500 random accident locations

---

## 📊 Tools Used
- Python
- Pandas
- Matplotlib
- Seaborn
- Folium

---

## 📈 Key Insights
- Certain hours (e.g., rush hours) see more accidents.
- Specific weather conditions like *Clear*, *Rain*, and *Overcast* are more prone to accidents.
- Weekdays like *Friday* and *Thursday* see a higher number of incidents.

---

## 🌐 Output Files
- `accident_hotspots_map.html`: Interactive accident hotspot map.
- Visualization plots shown inline.

---

## 🏁 How to Run
1. Install required packages:
   ```bash
   pip install pandas matplotlib seaborn folium
