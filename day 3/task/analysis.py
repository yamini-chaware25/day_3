import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load dataset
df = pd.read_csv("data/facility_dataset.csv")

# Create charts folder
charts = Path("charts")
charts.mkdir(exist_ok=True)

# Convert numeric columns
numeric_columns = [
    "cleanliness_score",
    "odor_score",
    "waste_level",
    "footfall",
    "complaints"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")


# ==========================================
# 1. BAR CHART - Cleanliness by Location
# ==========================================

cleanliness = df.groupby("location")["cleanliness_score"].mean()

plt.figure(figsize=(10, 6))
cleanliness.plot(kind="bar")

plt.title("Average Cleanliness Score by Location")
plt.xlabel("Location")
plt.ylabel("Average Cleanliness Score")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(charts / "bar_chart_1.png")
plt.close()


# ==========================================
# 2. BAR CHART - Complaints by Location
# ==========================================

complaints = df.groupby("location")["complaints"].sum()

plt.figure(figsize=(10, 6))
complaints.plot(kind="bar")

plt.title("Total Complaints by Location")
plt.xlabel("Location")
plt.ylabel("Total Complaints")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(charts / "bar_chart_2.png")
plt.close()


# ==========================================
# 3. HISTOGRAM - Footfall
# ==========================================

plt.figure(figsize=(10, 6))

plt.hist(
    df["footfall"].dropna(),
    bins=15
)

plt.title("Distribution of Facility Footfall")
plt.xlabel("Footfall")
plt.ylabel("Number of Facilities")

plt.tight_layout()

plt.savefig(charts / "histogram.png")
plt.close()


# ==========================================
# 4. SCATTER PLOT
# ==========================================

plt.figure(figsize=(10, 6))

plt.scatter(
    df["footfall"],
    df["complaints"]
)

plt.title("Footfall vs Complaints")
plt.xlabel("Footfall")
plt.ylabel("Complaints")

plt.tight_layout()

plt.savefig(charts / "scatter_plot.png")
plt.close()


# ==========================================
# 5. BOX PLOT
# ==========================================

plt.figure(figsize=(8, 6))

plt.boxplot(
    df["cleanliness_score"].dropna()
)

plt.title("Cleanliness Score Distribution")
plt.ylabel("Cleanliness Score")

plt.tight_layout()

plt.savefig(charts / "additional_chart.png")
plt.close()


print("================================")
print("5 CHARTS CREATED SUCCESSFULLY!")
print("================================")

print("1. bar_chart_1.png")
print("2. bar_chart_2.png")
print("3. histogram.png")
print("4. scatter_plot.png")
print("5. additional_chart.png")

print("\nCheck the charts folder.")