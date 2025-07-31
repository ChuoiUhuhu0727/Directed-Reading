import seaborn as sns
import pandas as pd
import numpy as np

# Way 1 to load dataset
sns.load_dataset("titanic")
# Way 2 to load dataset
!curl -o titanic.csv https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
titanic = pd.read_csv('titanic.csv')
titanic.head()
titanic['Age'].max()
titanic['Age'].min()
# Step 2: Create a new column "age_group" that bins the "Age" into decades (0–9, 10–19, etc.).
titanic['Age_bin'] = pd.cut(titanic['Age'], 8)
titanic['Age_bin'].unique()
titanic
titanic['SibSp'].unique()
titanic['family_size'] = titanic['SibSp'] + titanic['Parch'] + 1
titanic['family_size'].unique()
titanic.pivot_table('Survived', index=['Age_bin', 'Sex'])
titanic.pivot_table('family_size', index=['Pclass', 'Sex'], aggfunc='mean')
titanic[titanic['Age'].isnull()]
titanic = titanic.query('Age.isnull() == False')
titanic.count()
quartile = np.percentile(titanic['Fare'], [25,50,75])
mu = quartile[1]
sig = 0.74 * (quartile[2] - quartile[0])

# filter out passengers whose "Fare" 
# is more than 3 sigmas from the median.

titanic = titanic.query('Fare < 3*@sig + @mu')
titanic
titanic.pivot_table('Survived', ['Age_bin', 'Sex', 'Pclass']).plot()
titanic.pivot_table('Survived', ['Sex', 'Pclass']).plot()
titanic.pivot_table('Fare', index='Embarked', aggfunc='mean').plot()
