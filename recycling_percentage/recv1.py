import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# df = pd.read_csv("recycling_percentage\data\household_waste.csv")

# print(df.head())

# weight = df["HholdWasteCollectedPerPersonKg"]
# percents = df["HholdWasteRecycledPercentage"]

# plt.scatter(df["HholdWasteCollectedPerPersonKg"], df["HholdWasteRecycledPercentage"], c="cyan", label="plots")

# plt.plot(np.unique(weight), np.poly1d(np.polyfit(weight, percents, 1))(np.unique(weight)),label="best fit")

# plt.legend()

# plt.show()


df = pd.read_csv("recycling_percentage\data\\reuse.csv")

df.Value = df.Value.str.rstrip(' %').astype('float')
v = df.Value.to_numpy()

swag = [v[i] - v[i-1] for i in range(1, len(v))]

swag = np.insert(swag, 0, 0)



plt.plot(df.StartDate, swag)

plt.xticks(rotation=60)

plt.xlabel("Start Date")
plt.ylabel("Percent Change over 1 year")


plt.show()
