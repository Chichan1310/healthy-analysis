import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure output folder exists
os.makedirs("output", exist_ok=True)

# Load dataset
df = pd.read_csv("healthy_eating_dataset.csv")

# 1️⃣ Top 10 Meals by Calories
plt.figure(figsize=(12,6))
sns.barplot(
    x='meal_name',
    y='calories',
    data=df.sort_values(by='calories', ascending=False).head(10)
)
plt.xticks(rotation=45, ha='right')
plt.title("Top 10 Meals by Calories")
plt.tight_layout()
plt.savefig("output/top_10_meals_calories.png")
plt.close()

# 2️⃣ Healthy vs Unhealthy Meals Count
plt.figure(figsize=(6,4))
sns.countplot(x='is_healthy', data=df)
plt.xticks([0,1], ['Unhealthy', 'Healthy'])
plt.title("Count of Healthy vs Unhealthy Meals")
plt.tight_layout()
plt.savefig("output/healthy_vs_unhealthy.png")
plt.close()

# 3️⃣ Meal Type Distribution
if 'meal_type' in df.columns:
    plt.figure(figsize=(10,5))
    sns.countplot(y='meal_type', data=df, order=df['meal_type'].value_counts().index)
    plt.title("Meal Type Distribution")
    plt.tight_layout()
    plt.savefig("output/meal_type_distribution.png")
    plt.close()

print("Graphs generated in output/ folder!")
