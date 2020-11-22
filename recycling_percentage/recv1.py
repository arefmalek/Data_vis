import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("recycling_percentage\data\household_waste.csv")

print(df.head())

weight = df["HholdWasteCollectedPerPersonKg"]
percents = df["HholdWasteRecycledPercentage"]

plt.scatter(df["HholdWasteCollectedPerPersonKg"], df["HholdWasteRecycledPercentage"], c="cyan", label="plots")

plt.plot(np.unique(weight), np.poly1d(np.polyfit(weight, percents, 1))(np.unique(weight)),label="best fit")
plt.legend()


plt.show()