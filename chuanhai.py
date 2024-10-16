import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt

df = pd.read_csv("bike_dataset.csv")

# print(len(df[df["name"].isna()]))

# df1 = df[df["name"].str.contains(r'\d{3,}$', na=False)]
# #df1 = df[df["name"].str.contains(r'\d{3}$', na=False)]

# def extract_cc(name):
#   result = re.search(r'(\d{3})$', name)
#   return result.group(0) if result != None else np.nan

# df = df.copy()
# df["CC"] = df["name"].apply(extract_cc)

# df = df[df["CC"].notna()]

# df.plot(x='CC', y='selling_price', kind='line')
# plt.xlabel('CC')
# plt.ylabel('selling price')
# plt.title('selling price vs CC')
# plt.show()

print(df["selling_price"].describe())