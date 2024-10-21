import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
import scipy.stats as stats

df = pd.read_csv("bike_dataset.csv")

# print(len(df[df["name"].isna()]))

# df1 = df[df["name"].str.contains(r'\d{3,}$', na=False)]
# #df1 = df[df["name"].str.contains(r'\d{3}$', na=False)]

def extract_cc(name):
  result = re.search(r'(\d{3})$', name)
  return result.group(0) if result != None else np.nan

df = df.copy()
df["CC"] = df["name"].apply(extract_cc)
df["CC"] = df["CC"].astype("Int64")

temp_df = df[df["CC"].notna()]

temp_df.plot.scatter(x='CC', y = 'selling_price', c=temp_df["year"], cmap=plt.cm.plasma)
plt.xlabel('CC')
plt.ylabel('selling price')
plt.title('selling price vs CC')

m, b = np.polyfit(temp_df["CC"], temp_df["selling_price"], 1)
plt.plot(temp_df["CC"], m*temp_df["CC"]+b, color="red")

correlation = temp_df["CC"].corr(temp_df["selling_price"])
print(f"Correlation between CC and Selling Price: {correlation:.3f}")

plt.show()


temp_df = df[df["CC"].notna()]
temp_df = temp_df[temp_df["CC"] < 300]
temp_df.plot.scatter(x='CC', y = 'selling_price', c=temp_df["year"], cmap=plt.cm.plasma)
plt.xlabel('CC')
plt.ylabel('selling price')
plt.title('selling price vs CC')

m, b = np.polyfit(temp_df["CC"], temp_df["selling_price"], 1)
plt.plot(temp_df["CC"], m*temp_df["CC"]+b, color="red")

correlation = temp_df["CC"].corr(temp_df["selling_price"])
print(f"Correlation between CC and Selling Price for CC < 300: {correlation:.3f}")

correlation = temp_df["year"].corr(temp_df["selling_price"])
print(f"Correlation between year and selling price for CC < 300: {correlation:.3f}")

plt.show()

correlation = df["year"].corr(df["selling_price"])
print(f"Correlation between year and selling price: {correlation:.3f}")




grouped_data = df.groupby('owner')['km_driven'].mean()

grouped_data.plot.bar()
plt.xlabel('owner')
plt.ylabel('Mean km_driven')
plt.title('Bar Plot of Mean km driven by owner')
plt.show()


print(df[df["owner"] == "4th owner"])

df.drop(642, inplace=True)

print(df[df["owner"] == "4th owner"])


grouped_data = df.groupby('owner')['km_driven'].mean()

grouped_data.plot.bar()
plt.xlabel('owner')
plt.ylabel('Mean km_driven')
plt.title('Bar Plot of Mean km driven by owner')
plt.show()

#owner1 = df[df[""]]
grouped_data = [group['km_driven'].values for name, group in df.groupby('owner')]
print(stats.f_oneway(*grouped_data).pvalue)