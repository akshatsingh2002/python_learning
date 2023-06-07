import pandas as pd
df = pd.read_csv("pokemonData.csv")
print(df.info())
newdf= df.loc[1:10,]
print(newdf)