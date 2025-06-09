# MINI-PROJECT: STATE STATISTICS DASHBOARD
import pandas as pd
import numpy as np

# State population data (2023 estimates)
population_dict = {
    'California': 39144818,
    'Texas': 30801506,
    'Florida': 23001442,
    'New York': 19299981,
    'Illinois': 12419293,
    'Pennsylvania': 12742923,
    'Ohio': 11780017
}

# State area data (square kilometers)
area_dict = {
    'California': 423967,
    'Texas': 695662,
    'Florida': 170312,
    'New York': 141297,
    'Illinois': 149995,
    'Pennsylvania': 119280,
    'Ohio': 116098
}

# Convert them to Pd Series
population = pd.Series(population_dict)
area = pd.Series(area_dict)

# Build a dataframe
df = pd.DataFrame({
    "population": population,
    "area": area
})

df["population_density"] = round((df["population"]/df["area"]), 2)

dense_pop_df = pd.DataFrame(df[df["population_density"] > 100])
dense_pop_df

top3_largest = pd.DataFrame(df.sort_values(by=["area"], ascending=False).head(3))
top3_largest

pop_dens_df = pd.DataFrame(
    df.sort_values(by=["population_density"], ascending=False)
)
pop_dens_df["rank"] = range(1, len(pop_dens_df)+1)
pop_dens_df

dense_pop_ind = pd.Index(df[df["population"] > 20000000].index)
dense_pop_ind

large_area_ind = pd.Index(df[df["area"] > 150000].index)
large_area_ind

dense_pop_ind.intersection(large_area_ind)
dense_pop_ind.union(large_area_ind)
dense_pop_ind.symmetric_difference(large_area_ind)

# Add a new state (Georgia)
df.loc["Georgia"] = [10545000, 153910, round(10545000/153910, 2)]

df
