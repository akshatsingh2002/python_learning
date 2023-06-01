import pandas as pd
# df = pd.read_csv("pokemonData.csv",usecols=["Pokemon"]).squeeze()

# s1 = pd.read_csv("pokemonData.csv",usecols=["Pokemon"])
# s1 = pd.read_csv("pokemonData.csv")
# print(s1)
# print(s1.get("Pokemon"))

# print(s1)
# print(sorted(s1))
# print(type(s1))


s1 = pd.read_csv("pokemonData.csv",index_col=["Pokemon"]) # makes pokemon name as index+
# s1["Bulbasaur"]= "Evolved" it creates new column and give the default value to it 
s1 = s1.squeeze()
s1["Bulbasaur"]= "Evolved"
print(s1)
print(s1.head(5))
# print(s1["Charmander"])