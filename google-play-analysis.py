import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# load the google play store app data
df=pd.read_csv("C://Users//Shilpa Kumari//Downloads//googleplaystore.csv")
df
# display the first few rows of dataset

print("Dataset Sample:")
print(df.head())
df.head(5)
# Basic data exploration
print("\nDataset Information:")s
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())
# Data cleaning( handling missing values)
df = df.dropna()  # Drop rows with missing values
df
# Analysis 1: Most popular categories
popular_categories = df['Category'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=popular_categories.values, y=popular_categories.index, palette='viridis')
plt.title('Top 10 Most Popular App Categories')
plt.xlabel('Number of Apps')
plt.show()
 # Analysis 2: Average rating per category
avg_rating_per_category = df.groupby('Category')['Rating'].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 8))
sns.barplot(x=avg_rating_per_category.values, y=avg_rating_per_category.index, palette='plasma')
plt.title('Average Rating per App Category')
plt.xlabel('Average Rating')
plt.show()
# Analysis 3: Free vs Paid apps
free_vs_paid = df['Type'].value_counts()
plt.figure(figsize=(6, 4))
plt.pie(free_vs_paid, labels=free_vs_paid.index, autopct='%1.1f%%', startangle=140, colors=['#66b3ff', '#99ff99'])
plt.title('Free vs Paid Apps')
plt.show()

# Analysis 4: Correlation between Rating, Reviews, and Installs
plt.figure(figsize=(8, 6))
sns.heatmap(df[['Rating', 'Reviews', 'Installs']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation between Rating, Reviews, and Installs')
plt.show()
