import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df_read = pd.read_csv("canola_seed_yield.csv")
print("Data read from CSV:")
print(df_read)


fig, ax = plt.subplots(figsize=(10, 7))


locations = df_read["Location"]
seed_yield_cultivar1 = df_read["Cultivar1_SeedYield"]
seed_yield_cultivar2 = df_read["Cultivar2_SeedYield"]


ax.scatter(seed_yield_cultivar1, locations, label="Cultivar 1", color="green", s=100)

ax.scatter(seed_yield_cultivar2, locations, label="Cultivar 2", color="purple", s=100)


for i in range(len(locations)):
    ax.plot(
        [seed_yield_cultivar1[i], seed_yield_cultivar2[i]],
        [locations[i], locations[i]],
        color="gray",
        linestyle="--",
    )


ax.set_xlabel("Seed Yield (tonnes per hectare)")
ax.set_title("Cleveland Dot Plot: Seed Yield of Two Canola Cultivars Across Locations")
ax.legend()


plt.tight_layout()
plt.show()
