import pandas as pd
# df = pd.read_csv("pokemonData.csv",usecols=["Pokemon"]).squeeze()

s1 = pd.read_csv("pokemonData.csv",usecols=["Pokemon"]).squeeze()
print(s1)
print(type(s1))