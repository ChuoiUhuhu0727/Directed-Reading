import pandas as pd
import numexpr

# Load & Overview data
pop_df = pd.read_csv('state-population.csv')
area_df = pd.read_csv('state-areas.csv')
abb_df = pd.read_csv('state-abbrevs.csv')
print(pop_df.head()); print(area_df.head()); print(abb_df.head())

abb_df['state'].unique()

# Merge 2 dataframe
pop_merged = pop_df.merge(abb_df, how='outer', left_on='state/region', right_on='abbreviation').drop(columns='abbreviation')
pop_merged

# Check nulls after merging
pop_merged.isnull().any()
pop_merged[pop_merged['population'].isnull()]['state/region'].unique()
pop_merged[pop_merged['population'].isnull()]

# Fill in missing values
# after predicting reasons 
# because of merging 
pop_merged.loc[pop_merged['state/region'] == 'PR', 'state'] = 'Puerto Rico'
pop_merged.loc[pop_merged['state/region'] == 'USA', 'state'] = 'United States'
pop_merged.isnull().any()

# Left join on "state" column
all_merged = pop_merged.merge(area_df, on='state', how='left')
all_merged.head()

# Filter data
data2010 = all_merged.query("year == 2010 & ages == 'total'")
data2010.head()

# Assign new indices
data2010 = all_merged.query("year == 2010 & ages == 'total'").copy() 
data2010.set_index('state', inplace=True)
# Calculate population density
density = data2010['population'] / data2010['area (sq. mi)']

density.sort_values(ascending=False, inplace=True)

# Merge area_df and abb_df 
area_merged = area_df.merge(abb_df, how='left', on='state')
area_merged.head()

missing_area = area_merged[area_merged['area (sq. mi)'].isnull()]
missing_area[['state', 'abbreviation']]

pop_merged = pop_df.merge(abb_df, how='left', left_on='state/region', right_on='abbreviation').drop(columns='abbreviation')
pop_merged.isna().sum() # Output: state: 96
pop_merged[pop_merged['population'].isnull() == True]

# Total number of years in pop_df
pop_merged['year'].unique()

# list all null values in state column
missing_state = pop_merged[pop_merged['state'].isnull()]
missing_state[['state/region', 'ages', 'year']].drop_duplicates()

# Handle missing data in the 'state' column 
# by mapping from 'state/region'
pop_merged.loc[pop_merged['state'].isnull(), 'state'] = pop_merged.loc[pop_merged['state'].isnull(), 'state/region']
pop_merged.isna().sum()

# null state in which region
missing_state['state/region'].unique()

# null state in which ages
missing_state['ages'].unique()

# null state in which year
missing_state['year'].unique()

# Handling Special Cases
pop_merged.loc[pop_merged['state'].isnull(), 'state'] = pop_merged.loc[pop_merged['state'].isnull(), 'state/region']
pop_merged.isna().sum()

all_merged = pop_merged.merge(area_merged, how='left', on='state').drop(columns='abbreviation')
all_merged = all_merged.set_index('state')
all_merged = all_merged.rename(columns={"area (sq. mi)": "area"})

all_merged['density'] = all_merged['population'] / all_merged['area'] 
all_merged.sort_values(by=['density'], ascending=False).head(5)
all_merged.sort_values(by=['density'], ascending=True).head(5)
