import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(
    "API_SP.POP.TOTL_DS2_en_csv_v2_406129.csv",
    skiprows=4
)

# Extract 2024 population values
population_2024 = df["2024"].dropna()

# Create histogram
plt.figure(figsize=(10, 6))
plt.hist(population_2024, bins=20, edgecolor="black")

plt.title("Distribution of Country Populations (2024)", fontsize=14)
plt.xlabel("Population")
plt.ylabel("Number of Countries")

plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig("histogram.png", dpi=300)

plt.show()