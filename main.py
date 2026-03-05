import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("netflix_titles.csv")
# print(df.head(5))
# print(df.shape)
# print(df.info())
# print(df.isna().sum().sort_values(ascending=False).head())
# print(df.duplicated(subset=['title']))
# print(df["date_added"].dtype)
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
# print(df["date_added"].dtype)
df.insert(7, "year_added", df['date_added'].dt.year)
df.insert(8, "month_added", df['date_added'].dt.month)
# print(df.groupby("type").size()
# print(df["country"].dropna().str.split(",").explode().str.strip().value_counts().head(10))
# print(df.groupby("year_added").size().sort_values(ascending=False))
# print(df.groupby("year_added")["type"].value_counts())
# print(df["listed_in"].dropna().str.split(",").explode().str.strip().value_counts().head(10))



#visualization


# df["type"].value_counts().plot(kind="bar")
# plt.title("Movies vs TV Shows on Netflix")
# plt.xlabel("Type")
# plt.ylabel("Count")
# plt.grid()
# plt.show()

# df.groupby("year_added").size().plot(kind="line")
# plt.title("contetnt added per Year")
# plt.xlabel("Years")
# plt.ylabel("Counts")
# plt.grid()
# plt.show()


# df["country"].dropna().str.split(",").explode().str.strip().value_counts().head(10).plot(kind="bar")
# plt.xlabel("Contries")
# plt.ylabel("Show counts")
# plt.grid()
# plt.show()

# df["listed_in"].dropna().str.split(",").explode().str.strip().value_counts().head(10).plot(kind="bar")
# plt.xlabel("Genres")
# plt.ylabel("Genere counts")
# plt.grid()
# plt.show()